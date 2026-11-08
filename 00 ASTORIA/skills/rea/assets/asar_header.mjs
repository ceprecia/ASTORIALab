// Decode the bounded ASAR header used by the upstream static reader.
import { openSync, readSync, closeSync, fstatSync } from 'node:fs';

export function getRawHeader(path) {
  const descriptor = openSync(path, 'r');
  try {
    const prefix = Buffer.alloc(8);
    if (readSync(descriptor, prefix, 0, 8, 0) !== 8 || prefix.readUInt32LE(0) !== 4) {
      throw new Error('Invalid ASAR header size record');
    }
    const headerSize = prefix.readUInt32LE(4);
    const total = fstatSync(descriptor).size;
    if (headerSize < 8 || headerSize > 16 * 1024 * 1024 || headerSize > total - 8) {
      throw new Error('Invalid or oversized ASAR header');
    }
    const bytes = Buffer.alloc(headerSize);
    if (readSync(descriptor, bytes, 0, headerSize, 8) !== headerSize) {
      throw new Error('Truncated ASAR header');
    }
    const length = bytes.readUInt32LE(4);
    if (bytes.readUInt32LE(0) > headerSize - 4 || length > headerSize - 8) {
      throw new Error('Invalid ASAR header string');
    }
    const headerString = new TextDecoder('utf-8', { fatal: true }).decode(bytes.subarray(8, 8 + length));
    return { headerString, header: JSON.parse(headerString), headerSize };
  } finally {
    closeSync(descriptor);
  }
}

export function uncache() {}
