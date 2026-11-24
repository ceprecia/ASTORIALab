---
name: verify-removal
description: >-
  Removes named local items directly and verifies app uninstalls on macOS,
  Windows, and Linux. Use for targeted inspection, removal of confirmed app
  leftovers, or a follow-up check after removal. Triggers:
  uninstall this Mac app, check for uninstall leftovers, verify an app is gone,
  delete these specific files.
metadata:
  level: skill
  system: Janitor System
  dependencies: ""
  created: "2026-11-21"
  updated: "2026-11-21"
---

# Verify Removal

Check the right places, remove the confirmed items, and verify the result after the last step.

## Purpose

Inspect or uninstall a named app, remove its confirmed leftovers, or remove specifically named local files or folders on macOS, Windows, or Linux. Use the same checks to verify work already done by the user. For vault filing, organization, or path repairs, use Folder Janitor.

## Inputs

- The named app, item, or path, and whether the user wants an inspection, a removal, or verification.
- The current operating system, account, volume, and installation method. Establish these from live evidence where possible.
- User-supplied locations or screenshots as starting points. Resolve each candidate to its actual location and owner.

## Steps

1. **Handle a specific item directly.** If the user names a path or an unambiguous local item and asks to remove it, resolve the entry, move it to the OS Trash or Recycle Bin, and check the original path once. Move a selected symlink as a link. If the entry is absent, report it as already gone. For a check-only request, report whether it is present. Then continue to any other requested items. The platform inventory below is for discovering app installations and leftovers. Folder names such as Library or CloudStorage alone are no reason to scan apps, diagnose sync, or ask again.
2. **Inspect a named app or discover its leftovers.** Run one targeted pass through the relevant platform locations. Use the bundle or package ID, install record, job target, or shortcut to establish ownership. Check app files, running processes, and startup entries when relevant to the request. A check-only request stays read-only.
3. **Remove what the user requested.** Use the supported uninstaller for a managed app and Trash for confirmed loose files. Unload confirmed app jobs when they are part of the removal. Proceed on clear authorization. Keep unrelated apps and shared components in place. Ask about an optional removal only if it would extend the request.
4. **Handle concrete blockers and keep going.** A permission error, ambiguous target, or explicit notice that the action would affect something outside the requested scope can block that item. Use the shortest supported recovery or give the user the exact step they must take. Continue any independent checks or removals. When the user completes a handoff, verify that item and resume the rest.
5. **Verify each result once.** For a file, check the original path. For an uninstall, recheck the relevant paths, install record, and process or startup state. A registered job can remain when its process is idle. Retry or investigate when a check actually disagrees with the expected result.

## Locations to check

These are candidate locations. Expand placeholders, resolve redirected folders and environment variables for the target account, and follow the actual installer or job definition. Check app-specific entries inside shared locations.

### macOS

- **App and install records.** Check `/Applications/<app>.app`, `~/Applications/<app>.app`, or the observed bundle location. Read the bundle ID and any relevant installer receipt or Homebrew cask record. Use the vendor uninstaller when present and appropriate for the requested scope.
- **Support, settings, and data.** Look under `~/Library/Application Support`, `Caches`, `Preferences` (including `ByHost`), `Logs`, and `Saved Application State`. Check app-specific entries under `~/Library/Containers`, `Group Containers`, `Application Scripts`, `HTTPStorages`, and `WebKit`. Look in `/Library/Application Support`, `/Library/Caches`, and `/Users/Shared` when the installation used shared storage. Validate ownership even inside a vendor’s folder or app group.
- **Diagnostics and temporary files.** Check `~/Library/Logs/DiagnosticReports`, `/Library/Logs/DiagnosticReports`, and `~/Library/Application Support/CrashReporter` where present. Use Console to resolve report locations. For app-specific temporary files or caches, resolve the session’s roots with `getconf DARWIN_USER_TEMP_DIR` or `getconf DARWIN_USER_CACHE_DIR`.
- **Background jobs.** Check Login Items & Extensions, `~/Library/LaunchAgents`, `/Library/LaunchAgents`, and `/Library/LaunchDaemons`. Follow the job to its helper, such as `/Library/PrivilegedHelperTools/<helper-id>` or the bundle’s `Contents/Library/LaunchAgents`, `LaunchDaemons`, `LoginItems`, or `SystemExtensions`. Verify exact labels with `launchctl print` in the appropriate user or system domain and use `systemextensionsctl list` when a system extension is involved.

### Windows

- **App and install records.** Check Settings → Installed Apps, WinGet inventory, or the relevant `HKCU` and `HKLM` views of `Software\Microsoft\Windows\CurrentVersion\Uninstall`. Check both registry views where applicable. Follow the verified install location; common leads are the resolved `%ProgramFiles%`, `%ProgramFiles(x86)%`, and `%LOCALAPPDATA%\Programs`. Use these inventories for read-only checks, since `Win32_Product` can trigger MSI repair.
- **Support, settings, and data.** Check app-owned entries under the resolved `%APPDATA%`, `%LOCALAPPDATA%`, `%USERPROFILE%\AppData\LocalLow`, and `%ProgramData%`. Check `%LOCALAPPDATA%\CrashDumps` if applicable. For MSIX or Store packages, check `Get-AppxPackage` in the selected profile and app data such as `%LOCALAPPDATA%\Packages\<PackageFamilyName>\LocalState` or `LocalCache`. Use the package manager for the managed install location.
- **Startup and jobs.** Check `shell:startup`, `shell:common startup`, and app-specific entries under the relevant `HKCU` or `HKLM` `Software\Microsoft\Windows\CurrentVersion\Run` and `RunOnce` keys. Inspect matching services and scheduled tasks. Check where each shortcut or job points, then verify its registration and process state separately.

### Linux

- **User support, settings, and data.** Check the target account’s `$XDG_CONFIG_HOME/<app>`, `$XDG_DATA_HOME/<app>`, `$XDG_STATE_HOME/<app>`, and `$XDG_CACHE_HOME/<app>`. Defaults are `~/.config`, `~/.local/share`, `~/.local/state`, and `~/.cache`. Check `~/.<app>` and `~/.local/bin` when install evidence points there. Check desktop entries in the XDG `applications` and `autostart` locations, including `/etc/xdg/autostart` on default setups.
- **Packages and system files.** Use the installed tool’s inventory and ownership records, such as `dpkg-query`, `rpm`, or `pacman`. Package removal may retain config or home data. Manual installs can leave app-owned entries under `/opt`, `/usr/local`, `/etc/<app>`, `/etc/opt/<app>`, or app-specific subfolders under `/var/lib`, `/var/cache`, `/var/log`, and `/var/opt`.
- **Startup and jobs.** Where systemd is present, query the actual system and user unit search paths. Typical leads are `/etc/systemd/system`, `/usr/lib/systemd/system`, and `$XDG_CONFIG_HOME/systemd/user`. Check installed unit files, drop-ins, sockets or timers if associated, and loaded state.
- **Flatpak, Snap, and AppImage.** Check Flatpak registration by app ID and installation scope and inspect `~/.var/app/<app-id>` for app data. Check the exact Snap instance and the corresponding `~/snap/<name>` and `/var/snap/<name>` directories, distinguishing recovery snapshots from active data. For an AppImage, locate the executable the user chose and follow any associated desktop entry. Use the relevant manager for managed files.

## Outputs

Report what was removed, which checks passed, what remains, and anything that could not be verified. Use the current request's reporting form; for choices left open, follow the recipient's applicable verified reporting policy, with chat as the fallback. Honor explicit current chat-only or no-save instructions. Save or send a report only within applicable authorized scope and a verified destination or recipient; a reporting preference alone supplies no such authority. Mention Trash or Recycle Bin when used. If a user action is pending, name that step and the verification still needed.

## Checks

- Confirm the outcome for each requested item. Report removed, already absent, still present, or inaccessible.
- For app removal, verify the relevant files and registrations. Treat history and recovery copies separately from an installed app.
- Report a blocked item individually and say what was completed for the rest of the request.

## References

- Apple. (n.d.). *Delete or uninstall apps on Mac*. https://support.apple.com/en-us/102610
- Apple. (n.d.). *macOS library directory details*. https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/MacOSXDirectories/MacOSXDirectories.html
- Apple. (n.d.). *Updating helper executables from earlier versions of macOS*. https://developer.apple.com/documentation/servicemanagement/updating-helper-executables-from-earlier-versions-of-macos
- Microsoft. (n.d.). *Known folder IDs*. https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid
- Microsoft. (n.d.). *Configure startup applications in Windows*. https://support.microsoft.com/en-us/windows/experience/startup-boot/configure-startup-applications-in-windows
- Microsoft. (n.d.). *MSIX troubleshooting guide*. https://learn.microsoft.com/en-us/windows/msix/msix-troubleshooting-guide
- freedesktop.org. (n.d.). *XDG Base Directory Specification*. https://specifications.freedesktop.org/basedir/latest/
- freedesktop.org. (n.d.). *Desktop Application Autostart Specification*. https://specifications.freedesktop.org/autostart/latest/
- Linux Foundation. (n.d.). *Filesystem Hierarchy Standard*. https://specifications.freedesktop.org/fhs/latest/
- systemd. (n.d.). *systemd.unit*. https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html
- Flatpak. (n.d.). *Conventions*. https://docs.flatpak.org/en/latest/conventions.html
- Canonical. (n.d.). *Data locations*. https://snapcraft.io/docs/reference/administration/data-locations/
- AppImage. (n.d.). *Running AppImages*. https://docs.appimage.org/user-guide/run-appimages.html
