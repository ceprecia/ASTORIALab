---
name: redactor
description: >-
  Creates multi-format redaction and de-identification candidates from exact
  user-named files, pasted content, or bounded batches. Inventories visible,
  embedded, metadata, and hidden surfaces; inspects the surfaces supported in
  the current environment and marks every other surface partial or uninspected;
  transforms a separate copy; and produces a redacted candidate, an annotated
  review copy, and a compact manifest, leaving final validation and release to
  the user. Never modifies the source, retrieves protected private files, follows
  vault links recursively, sends material, or claims an output is safe,
  compliant, anonymous, or finally de-identified. Triggers: redact this
  document, de-identify this, scan this for sensitive information, make a
  share-safe version.
metadata:
  level: skill
  system: Capture and Writing Helpers
  dependencies: ""
  created: "2026-07-17"
  updated: "2026-11-01"
---

# Redactor

Create the strongest practical redaction candidate, expose what remains uncertain, and give the user a precise package for final human review.

## Steps

Start the run:

1. Load `me.md`, the Skill Map, and the relevant format support only after Redactor has triggered.
2. Identify the exact source or bounded batch. If the user already supplied it, do not delay the run with another confirmation.
3. Infer the transformation goal from the request:
   - `redact` favors destructive removal or destructive content replacement that renders as an opaque block;
   - `de-identify` favors consistent pseudonyms, generalization, recoding, or suppression when those preserve useful information;
   - `sanitize` or `shareable` uses the least destructive supported transformation consistent with the requested goal; the result remains a review candidate.
   - `scan this for sensitive information` means a detection-plus-candidate run, not a report-only mode. If no finding requires transformation, still preserve the source and produce a separate unchanged-content candidate plus the annotated review and manifest.
4. Ask at most one short content-preservation question only when two plausible transformations would materially change usefulness. Never ask an authority or compliance questionnaire.
5. State the source scope and output destination. Disclose material support limits that affect the transformation. Include the optional support overview below when requested or needed. Then begin the transformation immediately.

### 1. Preserve And Inventory

- Compute a SHA-256 hash for each source before doing any work.
- Inspect the filename and filesystem metadata as possible identifying surfaces.
- Detect the source format and enumerate visible, hidden, embedded, and metadata surfaces that the format can contain.
- Mark every surface as `inspected`, `partial`, or `uninspected`.
- Keep temporary extraction, OCR, conversion, rendering, and QA material outside the vault.

### 2. Detect In Complementary Passes

Run all applicable passes. Do not rely on one detector.

**Structured pattern pass**

- Contact data such as email addresses, phone and fax numbers, street addresses, and precise coordinates.
- Government, medical, student, employee, license, device, vehicle, account, certificate, and record identifiers.
- Dates, ages, times, URLs, IP addresses, usernames, handles, geocodes, UUIDs, and other unique codes.
- Credentials and secrets such as passwords, API keys, access tokens, private-key blocks, connection strings, and recovery codes.

**Semantic and contextual pass**

- Names, initials, relatives, household members, employers, schools, sites, teams, and relationships.
- Precise geography, chronology, rare events, occupations, diagnoses, treatments, accommodations, grades, and unusual characteristics.
- Indirect or quasi-identifier combinations that become identifying together even when each field appears ordinary alone.
- Free-text narratives, quotations, anecdotes, and distinctive wording that can link a person or organization to outside information.
- Public figures or public institutional facts that may be intentionally retained. Do not remove them automatically when the context clearly depends on them.

**Container and hidden-surface pass**

- Metadata, properties, comments, tracked changes, deleted revisions, notes, hidden sheets or slides, hidden rows or columns, formulas, caches, named ranges, alt text, object names, and filenames.
- Headers, footers, footnotes, endnotes, fields, hyperlinks, bookmarks, annotations, forms, layers, attachments, scripts, actions, and external relationships.
- Embedded files, chart data, cropped-image originals, images of text, QR codes, barcodes, faces, name tags, screens, reflections, landmarks, and other visible identity clues.

For every finding record:

- a neutral finding ID such as `R001`;
- its precise location;
- category;
- proposed transformation;
- `risk_level` as `low`, `medium`, or `high`, used only as qualitative review priority and not as a formal re-identification-risk estimate;
- `detection_confidence` as `low`, `medium`, or `high`;
- `inspection_status` as `inspected`, `partial`, or `uninspected`.

Do not reproduce the sensitive value in the saved manifest.

### 3. Transform The Candidate

- Apply the least destructive transformation that removes or weakens the identifying signal while preserving the requested usefulness.
- Use destructive removal or destructive content replacement that renders as an opaque block when content must disappear.
- Use labeled placeholders such as `[PERSON_01]`, `[SITE_01]`, or `[DATE_REDACTED]` when context should remain legible.
- Reuse the same placeholder for the same entity across a bounded batch so relationships remain interpretable without retaining the original value.
- Use consistent pseudonyms across a bounded batch when relationships or longitudinal structure matter. Record that consistent pseudonyms preserve linkage and do not by themselves make material anonymous or finally de-identified.
- Use generalization, binning, top or bottom coding, recoding, aggregation, or suppression for dates, geography, numeric values, small groups, and rare categories.
- Use cell or row suppression only when needed; preserve row, column, delimiter, formula, and schema integrity wherever possible.
- Never save a reversible original-to-placeholder key unless the user explicitly requests one. If requested, save it separately from the candidate package at a user-approved location.
- Do not use visual overlays, white text, blur, or pixelation as redaction. Remove the underlying content or permanently replace the relevant pixels in a newly encoded file.
- When a format cannot preserve both editability and reliable removal, prioritize reliable removal and record the lost features in the manifest.

### 4. Produce The Review Package

Create three artifact classes unless the user explicitly requests fewer:

1. **Redacted candidate** containing the applied transformations.
2. **Annotated review copy** built from the redacted candidate, with numbered findings that correspond to the manifest. Show where each transformation occurred without reproducing the removed sensitive value. This copy is a review aid and is not the release candidate.
3. **Review manifest** containing coverage, transformations, flags, residual tests, and the final human checklist without repeating removed values.

Use these fallback paths when no established workflow or explicit destination applies:

- `<owning folder>/YYYY-MM-DD_<source>_redaction_candidate.<ext>`
- `<owning folder>/YYYY-MM-DD_<source>_redaction_annotated.<ext-or-pdf>`
- `<owning folder>/YYYY-MM-DD_<source>_redaction_review.md`
- `<owning folder>/YYYY-MM-DD_<batch>_redaction_review/` for a batch, where the owning folder is the verified location for the owner of the source under `me.md`, or the destination the user names; ask once when no owner is clear

Use authorized selected names or follow the applicable verified naming policy. Use snake case for fallback names when neither specifies a name. If the source filename contains an identifier, use a neutral stem such as `document_001`. If a candidate already exists, create `_v2`, `_v3`, and later versions rather than overwriting it.

Before placing the run date in a generated basename or manifest, compare it with dates being transformed from the source. If the run date would reintroduce withheld chronology, omit the date prefix, use a neutral stem such as `document_001`, and record creation time only at a non-disclosing precision.

Use this manifest frontmatter:

```yaml
---
type: redaction_review
source_id:
source_sha256:
candidate_file:
annotated_file:
candidate_status:
review_status: human_review_required
created:
created_precision:
---
```

Use these body sections:

- `# Inspection Coverage`
- `# Transformations`
- `# High-Risk Review Flags`
- `# Partial Or Uninspected Surfaces`
- `# Residual QA Results`
- `# Human Final Review`

For a batch, create one candidate and one annotated review copy per source plus one batch manifest unless the user explicitly requests a different package. Set `source_id` to a neutral batch identifier. Represent `source_sha256` as a mapping keyed by neutral source ID, and represent `candidate_file` and `annotated_file` as lists or mappings using the same source IDs. Do not place identifying source names or values in those fields. Fill `created` at the finest non-disclosing ISO precision and set `created_precision` to `day`, `month`, `year`, or `withheld`.

### 5. Reopen And Test The Result

- Reopen the generated candidate and annotated review copy through the relevant format adapter.
- Search the candidate, annotated review copy, review manifest, and generated basenames for every known identifier and plausible variant without writing those values into the manifest.
- Extract or OCR candidate text again and record whether any residual match appears on the surfaces those methods could inspect. A negative result is not proof about partial or uninspected surfaces.
- Reinspect metadata, comments, revisions, notes, hidden content, caches, embedded parts, links, attachments, and filenames.
- Render every relevant page, slide, sheet, or image and inspect at full size.
- Confirm every finding has one matching manifest entry and every visually locatable transformation has one matching annotation. Document metadata and other hidden-surface transformations in the manifest instead.
- Compare source and candidate structure, page or sheet counts, formulas, schemas, links, and media where preservation matters.
- Recompute the source hash and confirm it has not changed.

Return exactly one technical state:

- `ready_for_human_review` when all intended surfaces were inspected and no major unresolved signal remains;
- `ready_for_human_review_with_flags` when a candidate exists but the user should examine named high-risk or ambiguous areas closely;
- `partial_candidate` when a technical limitation left any surface `partial` or `uninspected`, or forced a lossy conversion.

Every state still requires the user's final review.

## Format Routes

| Format family | Candidate route | Annotated review and QA |
| --- | --- | --- |
| Markdown, TXT, YAML, HTML | Transform text while preserving valid structure; inspect frontmatter, comments, links, embeds, code, attributes, scripts, and hidden DOM content | Create a line-numbered annotated copy; parse when possible; run structural diff and residual search |
| JSON and XML | Transform keys, values, attributes, text, CDATA, comments, and processing instructions while preserving validity | Use JSON Pointer or XPath locations; reparse and compare structure |
| CSV and TSV | Transform cells or columns while preserving delimiter, quoting, encoding, multiline fields, and row structure | Create a highlighted review table or workbook; reconcile row and column counts |
| DOCX | Edit relevant OOXML parts; inspect body, headers, footers, notes, comments, revisions, hyperlinks, properties, images, charts, and embeddings | Create annotated DOCX or PDF; search the package; scrub metadata; render and inspect every page |
| PDF | Reconstruct clean content or rasterize affected pages, permanently replace pixels, and rebuild the PDF | Create annotated PDF; re-extract text; inventory metadata, forms, annotations, attachments, layers, scripts, actions, and links; render every page |
| PPTX | Transform slides, tables, charts, notes, comments, hidden slides, properties, links, image text, and inspect masters and embeddings | Create annotated deck or PDF; search the package; inspect notes and hidden content; render every slide |
| XLSX | Transform cells, formulas when required, comments, names, hidden sheets, rows, columns, charts, properties, caches, connections, and image text | Create a review workbook with highlighted cells and index; scan formulas; reopen and render every sheet |
| PNG, JPG, JPEG, TIFF | Use local OCR plus visual inspection and deterministic opaque pixel replacement; strip supported EXIF, XMP, IPTC, comment, and text chunks during re-encoding | Create a numbered annotated image; inspect at full resolution; rerun OCR; perform an independent metadata read; flag unsupported namespaces |
| DOC, RTF, ODT, XLS, ODS, PPT, ODP | Convert to a modern editable format before processing | Record the conversion and any fidelity loss |
| Other user-named formats | Attempt native inspection, reliable conversion, rasterization, or an extracted representation rather than rejecting from a fixed whitelist | Mark preservation gaps and uninspected surfaces as `partial_candidate` |

For a rasterized PDF candidate, explicitly record lost searchability, accessibility, forms, links, bookmarks, or signatures. For scanned or image-heavy sources, treat OCR as a proposal generator and preserve a visual human-review flag for low-confidence regions.

## Boundaries

Operating contract:

- Treat Redactor as a transformation and inspection tool, not a legal gatekeeper.
- Do not require the user to prove classification, sharing authority, or legal permission.
- Do not refuse material merely because it concerns research, participants, clinical work, patients, teaching, or students.
- Preserve every source unchanged. Work only on new candidate files.
- Process only exact user-named files, pasted material, embedded parts of those files, or a bounded user-named batch.
- Do not follow wiki-links, transclusions, external URLs, or neighboring folders unless the user explicitly adds them to the scope.
- Do not send, publish, upload, email, copy externally, or run [chat-handoff](../chat-handoff/SKILL.md).
- Stop only when a technical condition prevents useful inspection or transformation, such as encryption without a password, corruption, or an unreadable container. Produce every feasible artifact first and report the remaining gap as `partial_candidate`.
- Describe every output as a candidate requiring human review. Never call it safe, share-safe, compliant, anonymous, certified, or finally de-identified.

Edge cases:

- **Encrypted source**: Ask for the password or a decrypted copy. If other files in a batch remain workable, process them and return a partial candidate for the batch.
- **Corrupt or malformed container**: Extract every readable surface, create a representation candidate when feasible, and list the unreadable parts.
- **Unsupported native format**: Attempt conversion, rasterization, or structured extraction. Preserve a clear fidelity warning.
- **Digital signature or checksum**: Expect transformation to invalidate it. Preserve the original and record that consequence.
- **Embedded object cannot be inspected**: Flag it prominently. Remove or replace it only when doing so is the least destructive way to prevent the uninspected object from traveling with the candidate.
- **Public figure or public fact**: Retain it when it is clearly necessary and not the requested target. Flag ambiguous cases for human review.
- **Too many findings for a readable annotated copy**: Group repeated deterministic findings while preserving an exact occurrence count and location index.
- **Correction after review**: Create a new version, rerun every residual test, and keep the earlier candidate unchanged.

## Checks

End every run with a compact checklist tailored to the actual source:

- Compare the redacted candidate with the numbered annotated copy.
- Confirm every intended identifier or sensitive element was transformed.
- Check whether context, rare combinations, visuals, or filenames still identify someone indirectly.
- Search and copy text from the candidate to expose residual or concealed text.
- Inspect properties, comments, notes, hidden sheets or slides, attachments, and embedded items when the native format retains them.
- Confirm that utility, formulas, relationships, and meaning were not damaged beyond what the redaction required.
- Review `partial` and `uninspected` surfaces manually.
- Release only the redacted candidate after the user is satisfied. Do not release the annotated copy or review manifest by accident.

Redactor does not decide whether the candidate should be released. The user owns that decision.

## Modular Plugin Support

This is the only section that should contain plugin-specific details. If a support layer changes, update this section, then keep the rest of the skill generic.

When orientation is requested or needed, describe the available support layers in the selected form or under the applicable verified reporting policy. Use the example below when helpful. Disclose material capability limits whenever they affect the task.

```markdown
Available support layers: editable documents, PDFs, presentations, spreadsheets, structured text, and deterministic image inspection where the current environment supports them.
```

| Plugin | Skill support role | Read use | Candidate rule |
| --- | --- | --- | --- |
| Documents | Transform, render, and structurally audit DOCX files | Attempt to inspect OOXML content, revisions, comments, properties, headers, footers, images, and related parts; report per-surface coverage | Preserve the source; write a distinct DOCX candidate; render every page; disclose unsupported embedded surfaces |
| PDF | Extract, render, reconstruct, and verify PDFs | Attempt to inspect page text, images, metadata, annotations, forms, attachments, links, and other catalog surfaces; report per-surface coverage | Never use overlay-only redaction; rebuild or rasterize affected content; run independent extraction and rendering checks; report residual matches on inspected surfaces |
| Presentations | Transform, render, and audit PPTX decks | Attempt to inspect visible objects, notes, comments, hidden slides, masters, properties, links, charts, and embeddings; report per-surface coverage | Preserve the source; write a distinct deck; combine adapter inspection with package-level search and full-slide rendering |
| Spreadsheets | Transform, render, and audit XLSX, CSV, and TSV data | Attempt to inspect cells, formulas, hidden structures, comments, names, charts, images, caches, connections, and properties; report per-surface coverage | Preserve the source; write a distinct workbook or table; reconcile structure, formulas, and rendered sheets |

Plugin rules:

- Use configured format adapters only when they directly support the named source.
- Keep vault Markdown as the durable skill contract.
- Do not use source or destination connectors as redaction engines.
- No dedicated redaction plugin is required or installed by this skill.
- Do not install a plugin automatically during a Redactor run.
- If a configured adapter is unavailable, use a reliable local fallback and record the reduced inspection coverage. Do not invent a passed audit.

## Optional Detector Adapter

- Keep the core workflow independent of any one detector.
- Microsoft Presidio may later provide an additional text, image, or structured-data detection pass. OCR tooling such as Tesseract may later provide another image-text pass.
- Never install either automatically. Use them only after a separate approved configuration.
- Treat any future detector as complementary. Its missed detections or confidence scores never replace semantic review, format inspection, residual QA, or the user's final review.

Design references, not installed dependencies:

- [Microsoft Presidio](https://github.com/microsoft/presidio) informs the modular detector-adapter boundary and recognizer model.
- [Document Redaction](https://github.com/seanpedrick-case/doc_redaction) informs the multi-format pipeline and human-review package design.

## Operational Reference Matrix

Use these sources as detection and technique references, not as gates that decide whether processing may occur. Use regime-specific identifier categories and transformation examples only. Do not treat a Redactor run as HIPAA Safe Harbor, Expert Determination, FERPA de-identification, or another legal determination.

| Source | Operational use |
| --- | --- |
| [NIST IR 8053](https://csrc.nist.gov/pubs/ir/8053/final) | Use as a background survey of risks across structured data, free text, multimedia, and medical imagery; use SP 800-188 as the newer operational backbone |
| [NIST SP 800-188](https://csrc.nist.gov/pubs/sp/800/188/final) | Distinguish direct and quasi-identifiers; select removal, masking, pseudonymization, generalization, aggregation, or suppression; reassess residual linkage risk with an appropriate method when one is available, otherwise report qualitative flags only |
| [NIST SP 800-122](https://csrc.nist.gov/pubs/sp/800/122/final) | Identify contextual and linkable personally identifiable information |
| [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html) | Scan health identifiers, free text, relatives, dates, unique characteristics, and comparable images |
| [Department of Education de-identification terminology](https://studentprivacy.ed.gov/sites/default/files/resource_document/file/data_deidentification_terms_0.pdf) | Apply generalization, statistical coarsening sometimes described as data blurring, suppression, and other disclosure-limitation concepts to educational data; never use visual blur as redaction |
| [Department of Education disclosure avoidance](https://studentprivacy.ed.gov/content/disclosure-avoidance) | Evaluate indirect combinations and select a method appropriate to tables or individual records |
| [Census disclosure-avoidance guidance](https://www.census.gov/topics/business-economy/disclosure/about.html) | Use as a table-specific example of primary and complementary cell suppression and deduction risk; do not infer a universal minimum-cell threshold |
| [Federal quantitative-data preparation guidance](https://ndacan.acf.hhs.gov/contribute-data/Contributors_Guide_to_Preparing_and_Archiving_Quantitative_Data.pdf) | Inspect dates, geography, rare categories, free responses, binning, recoding, and top or bottom coding |
| [U.S. District Court electronic-document guidance](https://www.njd.uscourts.gov/content/personal-identity-and-metadata-redaction-techniques-e-filing) | Use the warning that cosmetic concealment is ineffective; omit content at the source or apply true redaction, then inspect hidden data and metadata |
| [DHS redaction guidance](https://www.dhs.gov/sites/default/files/publications/priv_cfoiao_cso_memo_redacting_sensitive_information_20100505_1.pdf) | Add an independent quality-control pass after transformation |
| [ODNI and DoD identity-protection guidance](https://www.odni.gov/files/NCSC/documents/campaign/DoD_IAPM_Guide_March_2021.pdf) | Remove and independently verify EXIF metadata, then inspect visible image content that may reveal people, locations, or history |
| [DOJ marking guidance](https://www.justice.gov/oip/oip-guidance/segregating-and-marking-documents-release-accordance-open-government-act) | Apply visible FOIA-style deletion labels only when the user explicitly requests that presentation style; use only exemption labels supplied by the user |

Longer legal or compliance explanations belong in future public documentation, not in this operational workflow.
