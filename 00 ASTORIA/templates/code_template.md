---
related:
created: "{{date}}"
---

# Code template

Use this optional reference when a project needs a source-file header or execution outline. Adapt the
comment syntax, fields and body sections to the language and task. Keep project
layout and specialized application structure; this is a file template, not a
new pipeline or framework. Existing files are not bulk-reformatted.

## Compact file prolog

Adapt the supplied style guide prolog. Prefer one language-appropriate documentation or comment block so example commands can be copied without a comment marker on every line. Keep shebangs, encoding declarations and other required machine directives in their correct positions. Do not leave empty fields, invented names/paths, large decorative boxes or a growing history table. Keep the prolog simple and easy to read.

Choose valid syntax for the source language:

| Language | Top-header style |
| --- | --- |
| Python | A single raw triple-quoted module docstring, `r""" ... """`, after any shebang/encoding declaration and before imports. It supplies `__doc__`; the raw prefix preserves backslashes in multiline command examples. |
| C, C++, Java, JavaScript, TypeScript, CSS | A native `/* ... */` block, with plain interior lines rather than a leading `*` on every example line. |
| MATLAB | A `%{` / `%}` block, with opening and closing delimiters on separate lines. |
| PowerShell | A native `<# ... #>` block. |
| Bash, Zsh, R and languages without a native block comment | Use native line comments. Do not imitate Python triple quotes or add executable strings, no-op commands or heredocs merely to simulate a comment block. Put unprefixed copyable examples in existing project documentation or supported usage output when needed; do not create an extra file just for the header. |

For other languages, use their valid native documentation/comment syntax. A Python docstring is a string literal used for documentation, not a general-purpose block-comment syntax. Keep only one top header; do not duplicate it as both a block and line comments. The Step 0–4 section comments below it remain ordinary native line comments.

Where a block is supported, adapt these fields inside it. Otherwise prefix the fields with the language's native line-comment marker.

```text
<open native documentation/comment block>
File: <name> | Purpose: <one sentence>
Inputs/outputs: <relevant file or interface names and roles>
Requires/run: <runtime/dependencies and useful invocation>
Example run commands:
    <normal full-run command>
    <a few useful alternatives>
Updated: <YYYY-MM-DD> | Author: <known author NOT AI> | Change: <brief>
Assumptions/errors: <material units, limits or validation failures>
References: <very short relevant specification, source or external interface>
<close native documentation/comment block>
```

Keep the file name and brief purpose for ordinary files; combine them if useful.
Other fields are optional choices, not six mandatory lines. The source's external
variables/references, notes, requirements references, development history and
algorithm fields can be included when useful. Explain an algorithm through the
body's numbered steps when that avoids repeating it in the prolog.

## Header scope

Keep documentation proportionate to the file's purpose. Follow the language and project's established documentation conventions. Do not add code or comments merely to meet a length ratio.

## Readable body scaffold

The following outline illustrates one batch-processing script. Select or omit sections to suit the actual program; numbering, helper placement and configuration layout are project choices.

```text
<comment> Step 0. Setup
<imports and package loading>
<load the existing project environment/configuration when needed>
<establish the project root so paths work across supported computers>

<comment> Step 1. Visible choices and paths
<input and output paths, grouped together>
<scope selection: participants, runs, files or conditions, as applicable>

<processing/model options with descriptive names and valid choices>
<thresholds and parameters with units where relevant>

<clearly grouped output/display toggles, for example:
 SAVE_TABLES, SAVE_QC_REPORT, SAVE_PLOTS, SHOW_PLOTS>

<execution options when supported:
 serial/parallel, worker count, resume or refit>

<parse command-line options so explicit arguments override script defaults>
<print a short startup message with the selected scope, main settings,
 execution mode and output location>

<comment> Step 2. Validate inputs
<check requirements needed for the selected operation>
<give understandable errors identifying the affected input>
<flag item-specific problems without stopping independent valid work>
<stop when a shared problem prevents correct processing>

<comment> Step 3. Process
<visible processing calls and readable loops in execution order>
<use the effective settings selected in Step 1 consistently>
<show useful progress by participant, run or file>
<preserve supplied identities, metadata and QC flags>
<record failures against affected items and continue where valid>

<comment> Step 4. Save outputs
<save requested outputs in the project's established output folder>
<apply export/display toggles without changing the underlying analysis>
<use descriptive filenames and retain metadata needed to identify outputs>
<remove temporary files created by this script>
<print a brief completion summary: completed, skipped, failed and output paths>

```

Use the project's established style and architecture. Make input assumptions, effective settings, errors and output identity discoverable. Keep examples executable for the actual language. Document side effects and preserve scientific settings. Choose modules, functions, comments and configuration interfaces according to maintainability and the recipient's supplied preferences. This outline does not require top-of-file toggles, repeated code, a particular abstraction level or numbered stages.

## Source

Adapted from: Doland, J., & Valett, J. (1994). *C style guide*
(SEL-94-003; NASA-CR-189408), §4.1, Figure 5, pp. 18–19.
https://ntrs.nasa.gov/search.jsp?R=19950022400
