---
name: mindmap
description: >-
  Creates and edits source-grounded visual mindmaps, handling organization and
  rendering with at most one brief missing-information checkpoint. Produces
  portable interactive HTML or an editable Obsidian Canvas at a verified
  authorized destination. Any note link needs its own edit scope. Supports conversational revisions, optional deeper
  organization review, exports, and an atlas of explicitly selected maps. Study
  Planner, Study Companion, and Research Companion may invoke it without
  transferring session ownership. Does not own MOCs, study progress, general brainstorming, or
  research conclusions. Triggers: create a mind map of this, turn this into a
  mind map, update this mind map, show my mindmap atlas.
metadata:
  level: skill
  system: Productivity and Study System
  dependencies: ""
  created: "2026-09-13"
  updated: "2026-10-29"
---

# Mindmap

Turn supplied material and ideas into a useful visual map. Do the organizing and building, not a long interview about how the user should build it.

## Purpose

Use for a requested visual mindmap with an authorized file save, an authorized revision to an existing map, or a bounded handoff for either. Preserve the invoking companion's session ownership. Work from the supplied material and verified current owner; follow me.md for access and placement.

Do not capture general brainstorming, `show my study map`, MOC construction, or an ordinary explanation. Those retain their existing owners. An unsaved concept map stays with the active session owner in the selected response form.

## Steps

1. **Start from what is already known.** Use at most one brief upfront checkpoint, combining only genuinely missing information needed to build. If the request or companion handoff is sufficient, start immediately. Infer a useful initial organization and layout; do not ask the user to supply branches, labels, colors, or a complete outline. Once per session mention that interactive HTML and editable Obsidian Canvas are available without turning that mention into a format-selection gate.
2. **Organize the content.** Identify the central topic, meaningful branches, details, source references, and supported cross-links. Preserve construct names, uncertainty, disagreements, and user-proposed ideas. Use short labels with fuller details rather than deleting meaningful content. Branch counts and depth are flexible, not quotas. Mark a gap as an open question, not evidence of absence; do not invent sources, causal links, conclusions, or new hypotheses.
3. **Build and check.** Verify the authorized map destination and choose the format below, instantiate the embedded renderer or Canvas representation, render it, and repair clipping, collisions, broken links, or controls. Do not add an organization approval, draft approval, export approval, save approval, or post-review gate within this requested local workflow. Do not delegate this serial organization/build/check sequence to subagents.
4. **Deliver.** Return a verified link or locator for the saved artifact and accurately state its completion and verification status. Use the selected reporting form for substantive content, including useful organization explanations and any source or rendering limitations. If reporting is open, use the applicable verified reporting policy. For file-only delivery, include substantive content in the authorized map or a separately authorized report, and keep the response to status and verified locator. For a companion handoff, return the artifact, verification status, source and rendering limitations, and current study/research return point to the invoking companion. Preserve the same user-facing reporting scope. Do not create study progress files or change scientific decisions.

### Optional deeper review and revisions

Only when requested, compare thematic, functional/process, and audience/question-centered organizations internally. Build the best-fitting structure and include a brief explanation in the reporting form used for delivery. Do not ask for another selection, display arbitrary quality scores, expose private deliberation, or claim the organization is scientifically validated.

For edits, read the actual named map, apply the requested content or layout change, preserve unaffected user content and working controls, then check and save. Do not restart intake. Update the named map when an edit was requested; use a distinct filename for a new map or explicitly requested alternate version. Never overwrite an unrelated file merely because its title matches.

## Outputs

| Context | Default output and location |
| --- | --- |
| Explicit format or destination | Use the verified eligible selection, then the applicable verified policy for any open choice |
| Existing relevant vault class/topic note | Use the verified eligible selected destination or applicable owner policy. When open, use the established course or topic location. Canvas is the fallback format for a relevant vault note |
| Established scientific package layout | Use the verified eligible destination selected for the task, then applicable placement policy. Otherwise preserve the established package location. Use HTML when format remains open |
| Standalone request with no owner | Use the verified eligible destination, then applicable placement policy. Ask once if the destination remains unresolved. Use self-contained HTML when format remains open |

Resolve the actual project or note already in context when it is needed to place the map. For placement, use the one upfront checkpoint only if the required file destination or an authorized link location is unresolved. The map save and any note edit have distinct write scopes. An exact class/topic locator may be checked without recursively following its links. Verify the destination against `me.md` and applicable project instructions. Do not create a new class note just to house the map.

Use `<topic>_mindmap.html` or `<topic>_mindmap.canvas`, following local naming conventions; add `YYYY-MM-DD` when a date is useful. For a new-name collision, choose a free `_v2` or later suffix. Create the Canvas before adding any backlink. When the note edit is separately authorized, add one backlink in the verified authorized location, using the relevant links section or a single line at the end when placement is open. Use the selected link syntax when the receiving app supports it. If the choice is open, use the applicable verified and supported convention for the receiving note. Use a supported note-relative Markdown link when neither sets a form. Use a vault-relative wiki-link when selected or configured and supported by the receiving app. Retain the `.canvas` extension and verify that the link resolves from the note to the exact saved file. If the chosen syntax is unsupported or the target is unresolved, omit the backlink and report the issue under the delivery rule above. Avoid duplicate links. Do not rewrite the note. No automatic wrapper note, sidecar JSON, library folder, or catalog.

HTML is one portable file with embedded data and scripts, no CDN, server, plugin, browser storage, installation, or archive dependency. Browser controls say **Download copy** and save a downloadable file, not an alleged vault write. The agent performs actual destination writes. Downloads containing relative links belong beside the original to retain those links.

## Rendering and exports

Before creating a new HTML source file, read and adapt the vault-root `00 ASTORIA/templates/code_template.md` using nonvisible HTML comments; preserve the doctype and specialized renderer below. Canvas JSON remains valid JSON without a comment prolog.

Use the embedded template as the portable baseline. Replace its JSON data, not the entire renderer on each conversational edit. Keep semantic content in the data block and create DOM text with text nodes, not interpolated source HTML. Serialize embedded JSON with `<` escaped as `\u003c` so source text cannot terminate its script element.

- Choose radial for associative overview, semicircle for a broad fan, tree for hierarchy, or flow for an actual sequence. Users may switch layouts. A flow layout alone does not justify causal arrows.
- Retain pan, zoom, fit, collapse, focus/back, details, fullscreen, four palettes, source links, and labeled cross-links. Connect at node edges and use opaque nodes. Check long labels and contrast. Keep detail and source attribution accessible by click as well as hover.
- A node's optional `weight` represents a stated count or prominence only, not reliability or scientific consensus. Record its meaning in `detail`. Do not infer evidence strength from frequency.
- Export only the requested formats. SVG and PNG contain the complete map, not a clipped viewport. PDF uses print-to-PDF or a supported local browser PDF export; a print dialog is not a saved PDF. Markdown/Markmap preserves hierarchy, details, sources, and a cross-link list. Markmap Markdown needs a compatible renderer to become interactive. Mermaid is an optional text export, not the primary interactive renderer.
- HTML retains its own controls. Canvas uses native Obsidian behavior and is not promised equivalent HTML controls or every export button.

### Canvas representation

Generate JSON Canvas 1.0 with unique node/edge IDs, integer `x`, `y`, `width`, `height`, and valid endpoints. Use text nodes containing the complete label, detail, uncertainty, and applicable source references in Markdown. Use file nodes only for verified vault-relative files and link nodes for actual URLs. Include labels on nonhierarchical edges. Set `fromEnd` and `toEnd` to `none` for associative/hierarchical connections so the format's default arrow does not imply an unsupported direction.

The embedded renderer exposes `Mindmap.canvas()` to obtain a full-map Canvas representation using its checked positions. For Canvas-only work, a temporary HTML rendering outside the vault may supply layout and QA; save only the final Canvas. Increase node height to fit its Markdown content and lay out using those full dimensions, not the smaller HTML pill dimensions. Verify linked files and any authorized link added to the owning note. During later Canvas edits, read the native nodes and edges as authoritative; do not restore stale embedded data or erase manual changes.

## Selected-map atlas

On an atlas request, use only the exact maps selected in the request, supplied by the companion, or explicitly selected earlier in the current chat. If no maps are selected, the one upfront checkpoint asks for them. Do not enumerate the vault or create an index in order to find maps.

Read each selected HTML data block or native Canvas nodes/edges. Make an overview with map titles, verified links, and shared-concept cross-links labeled with the shared terms. Label matching is a navigation aid, not a claim of scientific agreement. Keep unresolved or ambiguous matches visible instead of asserting equivalence. Opening a map follows its file link; it does not recursively load its sources. Use the same format, destination and note-edit authorization rules as for a single map. The atlas uses the existing storage layout. Treat it as a snapshot and regenerate it from selected files when requested. If a selected file moved or is missing, identify that gap without reconstructing it from memory.

## Checks

- Verify unique IDs, a connected acyclic parent tree, valid cross-links and sources, and source fidelity before rendering. Preserve important detail instead of enforcing a three-level maximum.
- Open the result and test layouts, long labels, pan/zoom, collapse, focus/back, details/source links, palette, fullscreen, download/reopen, and requested exports. Check Canvas JSON, full text fit, endpoints and paths. Verify any note link added within the authorized scope. Use synthetic files outside the vault when testing this skill itself.
- Missing source text stays missing. Build the supported portion and identify the limitation rather than filling it from memory. Distinguish a user-idea map from a sourced factual map.
- For large material, use collapsible branches, fit/zoom, and details; do not silently truncate it. Repair layout internally without another user gate.
- If browser rendering is unavailable, still deliver the supported HTML or validated Canvas. Record the missing visual or interactive checks under the delivery rule above and keep the completion status accurate. Never claim a tested export or a vault save from a download button alone.

## References

- Adapted from: 0x-man. (2026). *Mindmap* (Version 1.2.0) [Computer software]. GitHub. https://github.com/0x-man/mindmap-skill (MIT License)
- Obsidian. (2024, March 11). *JSON Canvas specification* (Version 1.0). https://jsoncanvas.org/spec/1.0/

## Appendix: Portable renderer

Copy this single HTML code block to a temporary or final `.html` and replace the `mindmap-data` JSON with the actual map. The synthetic sample is schema illustration, not default content. Nodes have stable IDs and one root (`parent: null`); sources have stable IDs and verified labels/URLs. `crossLinks` records supported relationships separately from hierarchy. `view` retains palette/layout choices in downloaded copies. Set `kind` to `atlas` for selected-map overviews and use node `url` for verified links to those maps. No code needs to read this skill's source archive.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mindmap</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f4f6f8;color:#172637;font:14px system-ui,-apple-system,sans-serif}button,select{font:inherit;border:1px solid #c5cdd5;border-radius:6px;padding:7px 10px;background:white;color:#172637;cursor:pointer}button:focus-visible,select:focus-visible{outline:3px solid #4a6fa5}header{background:white;border-bottom:1px solid #d4dbe2;padding:14px 18px}h1{font-size:20px;margin:0 0 12px}nav{display:flex;gap:7px;flex-wrap:wrap;align-items:center}label{display:flex;gap:5px;align-items:center}.workspace{display:grid;grid-template-columns:minmax(0,1fr) 260px;height:calc(100vh - 154px);min-height:440px}#stage{width:100%;height:100%;touch-action:none;cursor:grab}aside{overflow:auto;background:white;border-left:1px solid #d4dbe2;padding:18px;line-height:1.5}aside h2{font-size:16px;margin-top:0}aside p{white-space:pre-wrap;overflow-wrap:anywhere}aside a{color:#245f89;overflow-wrap:anywhere}footer{padding:9px 18px;font-size:12px;color:#485969}#notice{min-height:20px}body.fullscreen{position:fixed;inset:0;z-index:9999}svg text{user-select:none}@media(max-width:720px){.workspace{grid-template-columns:1fr;height:auto}#stage{height:65vh;min-height:360px}aside{border-left:0;border-top:1px solid #d4dbe2;max-height:240px}}
</style>
</head>
<body>
<header><h1 id="title"></h1><nav aria-label="Mindmap controls">
<label>Layout <select id="layout"><option>radial</option><option>semicircle</option><option>tree</option><option>flow</option></select></label>
<label>Palette <select id="palette"></select></label>
<button id="zoom-out" aria-label="Zoom out">−</button><button id="zoom-in" aria-label="Zoom in">+</button><button id="fit">Fit</button>
<button id="collapse">Collapse / expand</button><button id="expand">Expand all</button><button id="focus">Focus selected</button><button id="back">Back to full map</button><button id="fullscreen">Fullscreen</button>
<label>Export <select id="format"><option value="html">HTML</option><option value="svg">SVG</option><option value="png">PNG</option><option value="pdf">PDF (print)</option><option value="md">Markdown / Markmap</option><option value="mmd">Mermaid</option><option value="canvas">Canvas</option></select></label><button id="download">Download copy</button>
</nav></header>
<main class="workspace"><svg id="stage" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Interactive mindmap"></svg><aside id="details" aria-live="polite"></aside></main>
<footer><div id="notice" role="status"></div>Drag to pan · Scroll or use buttons to zoom · Select a node for details · Double-click to collapse<br>Downloads are copies, not writes to your vault. Keep copies beside the original for relative links.</footer>
<script id="mindmap-data" type="application/json">
{"title":"Synthetic example","nodes":[{"id":"root","parent":null,"label":"Synthetic example"},{"id":"a","parent":"root","label":"First concept","detail":"Replace with supplied material.","sourceIds":["s1"]},{"id":"b","parent":"root","label":"Second concept"}],"crossLinks":[],"sources":[{"id":"s1","label":"Synthetic source, not research evidence"}],"view":{"layout":"radial","palette":"Bauhaus"}}
</script>
<script>
/* Palette/interaction design adapted from 0x-man Mindmap 1.2.0.
MIT License. Copyright (c) 2026 0x-man.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. Portable renderer and Canvas adaptation, 2026. */
(() => {
'use strict';
const $ = id => document.getElementById(id);
const data = JSON.parse($('mindmap-data').textContent);
const palettes = {
  Bauhaus:['#D64045','#1D3557','#E9B44C','#2D6A4F','#7B2D8E','#E07A5F','#457B9D'],
  'Ocean Sunset':['#E76F51','#2A9D8F','#E9C46A','#264653','#F4A261','#287271','#BC4749'],
  'Nordic Forest':['#5B8C5A','#4A6FA5','#C17C74','#7B6D8D','#D4A574','#4D8B8B','#8B6F47'],
  'Pastel Garden':['#7EB8DA','#B5C99A','#E8A87C','#9B8EC1','#F2CC8F','#81B29A','#E07A5F']
};
const nodes = data.nodes || [], sources = data.sources || [], links = data.crossLinks || [];
const byId = new Map(nodes.map(n => [n.id,n]));
const sourceById = new Map(sources.map(s => [s.id,s]));
const roots = nodes.filter(n => n.parent == null);
if (!nodes.length || roots.length !== 1 || byId.size !== nodes.length || sourceById.size !== sources.length) throw Error('Invalid root or duplicate IDs');
for (const n of nodes) {
  const seen = new Set(); let p = n;
  while (p) { if(seen.has(p.id)) throw Error('Parent cycle'); seen.add(p.id); if(p.parent != null && !byId.has(p.parent)) throw Error('Missing parent'); p=byId.get(p.parent); }
  if ((n.sourceIds || []).some(id => !sourceById.has(id))) throw Error('Missing source');
}
if(links.some(e=>!byId.has(e.from)||!byId.has(e.to))) throw Error('Missing cross-link endpoint');
const root = roots[0], children = id => nodes.filter(n=>n.parent===id);
const descendants = id => { const result = new Set([id]); for(const n of children(id)) for(const child of descendants(n.id)) result.add(child); return result; };
let layout = ['radial','semicircle','tree','flow'].includes(data.view?.layout) ? data.view.layout : 'radial';
let palette = palettes[data.view?.palette] ? data.view.palette : 'Bauhaus';
let selected = root.id, focused = null, collapsed = new Set(), view = null, drag = null;
const stage = $('stage'), meter = document.createElement('canvas').getContext('2d');
meter.font='14px system-ui';
function wrap(text, width=220, fontSize=14) {
  meter.font=`${fontSize}px system-ui`;
  const lines=[];
  for(const paragraph of String(text).split('\n')) {
    let line='';
    for(const word of paragraph.split(/\s+/).filter(Boolean)) {
      if(line && meter.measureText(line+' '+word).width>width){lines.push(line);line='';}
      if(meter.measureText(word).width>width){if(line){lines.push(line);line='';}for(const c of word){if(meter.measureText(line+c).width>width){lines.push(line);line='';}line+=c;}}
      else line+=(line?' ':'')+word;
    }
    lines.push(line);
  }
  return lines;
}
function dimensions(n, canvasMode=false) {
  const lines = wrap(canvasMode ? canvasText(n) : n.label,220,canvasMode?16:14);
  // Canvas renders Markdown with larger note text, paragraph margins, and padding.
  return {w:260,h:canvasMode?Math.max(120,lines.length*28+64):Math.max(52,lines.length*20+24),lines};
}
function branchIndex(n) {let p=n; while(p.parent && p.parent!==root.id) p=byId.get(p.parent); return Math.max(0,children(root.id).findIndex(c=>c.id===p.id));}
function color(n) {return n.id===root.id ? '#172637' : palettes[palette][branchIndex(n)%7];}
function ink(hex) {const c=hex.slice(1).match(/../g).map(v=>parseInt(v,16)/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4); return c[0]*.2126+c[1]*.7152+c[2]*.0722>.179?'#000000':'#ffffff';}
function positions(all=false, canvasMode=false) {
  let chosen=nodes;
  if(!all) {
    const allowed=focused ? descendants(focused) : new Set(nodes.map(n=>n.id));
    const hidden=new Set(); for(const id of collapsed) for(const d of descendants(id)) if(d!==id) hidden.add(d);
    chosen=nodes.filter(n=>allowed.has(n.id)&&!hidden.has(n.id));
  }
  const set=new Set(chosen.map(n=>n.id)), top=chosen.find(n=>!set.has(n.parent));
  const childrenHere=id=>chosen.filter(n=>n.parent===id);
  const metrics=new Map(chosen.map(n=>[n.id,dimensions(n,canvasMode)]));
  const spans=new Map(), depths=new Map();
  function measure(n,depth) {depths.set(n.id,depth); const kids=childrenHere(n.id); const own=(layout==='flow'?metrics.get(n.id).w:metrics.get(n.id).h)+60; const span=Math.max(own,kids.reduce((s,k)=>s+measure(k,depth+1),0)); spans.set(n.id,span); return span;}
  const total=measure(top,0), result=[];
  const maxDepth=Math.max(...depths.values());
  const levelSize=Array.from({length:maxDepth+1},(_,d)=>Math.max(...chosen.filter(n=>depths.get(n.id)===d).map(n=>layout==='flow'?metrics.get(n.id).h:metrics.get(n.id).w)));
  const depthOffset=d=>levelSize.slice(0,d).reduce((s,v)=>s+v+160,0);
  function place(n,start) {
    const d=depths.get(n.id), middle=start+spans.get(n.id)/2, m=metrics.get(n.id);
    let x=depthOffset(d), y=middle-total/2;
    if(layout==='flow') [x,y]=[middle-total/2,depthOffset(d)];
    if(layout==='radial'||layout==='semicircle') {
      const arc=layout==='radial'?2*Math.PI:Math.PI;
      const angle=(middle/total)*arc-(layout==='radial'?Math.PI/2:Math.PI);
      const radius=d*Math.max(190,total/arc/2); x=d?Math.cos(angle)*radius:0; y=d?Math.sin(angle)*radius:0;
    }
    result.push({...n,...m,x,y}); let cursor=start;
    for(const child of childrenHere(n.id)) {place(child,cursor); cursor+=spans.get(child.id);}
  }
  place(top,0);
  // Resolve label-box collisions without discarding content or changing the hierarchy.
  for(let pass=0;pass<80;pass++) {let moved=false; for(let i=0;i<result.length;i++) for(let j=i+1;j<result.length;j++) {
    const a=result[i],b=result[j],dx=(a.w+b.w)/2+28-Math.abs(a.x-b.x),dy=(a.h+b.h)/2+28-Math.abs(a.y-b.y);
    if(dx>0&&dy>0){const sign=b.y>=a.y?1:-1; b.y+=sign*(dy+1); moved=true;}
  } if(!moved)break;}
  return result;
}
function bounds(list) {const x=Math.min(...list.map(n=>n.x-n.w/2))-80,y=Math.min(...list.map(n=>n.y-n.h/2))-80; return {x,y,w:Math.max(...list.map(n=>n.x+n.w/2))-x+80,h:Math.max(...list.map(n=>n.y+n.h/2))-y+80};}
function element(tag,attrs={},text) {const e=document.createElementNS('http://www.w3.org/2000/svg',tag); for(const [k,v]of Object.entries(attrs))e.setAttribute(k,v); if(text!=null)e.textContent=text; return e;}
function endpoint(a,b) {const dx=b.x-a.x,dy=b.y-a.y,t=Math.min((a.w/2)/Math.max(Math.abs(dx),.001),(a.h/2)/Math.max(Math.abs(dy),.001)); return {x:a.x+dx*t,y:a.y+dy*t};}
function buildSvg(all=false) {
  const list=positions(all), map=new Map(list.map(n=>[n.id,n])), svg=element('svg',{xmlns:'http://www.w3.org/2000/svg','font-family':'system-ui, sans-serif'}), box=bounds(list);
  svg.setAttribute('viewBox',`${box.x} ${box.y} ${box.w} ${box.h}`);
  const labelBoxes=[];
  const edges=[...list.filter(n=>map.has(n.parent)).map(n=>({from:n.parent,to:n.id})),...links.filter(e=>map.has(e.from)&&map.has(e.to))];
  for(const e of edges) {
    const a=map.get(e.from),b=map.get(e.to),s=endpoint(a,b),t=endpoint(b,a);
    const group=element('g'); group.append(element('line',{x1:s.x,y1:s.y,x2:t.x,y2:t.y,stroke:'#788a9b','stroke-width':2,'stroke-dasharray':e.label?'7 5':'none'}));
    if(e.label){
      const lines=wrap(e.label,180,12),w=200,h=lines.length*17+12;
      const intersects=(candidate,n)=>Math.abs(candidate.x-n.x)<(candidate.w+n.w)/2+10&&Math.abs(candidate.y-n.y)<(candidate.h+n.h)/2+10;
      let labelBox=null;
      for(const fraction of [.5,.3,.7]){for(const offset of [-25,-65,65,-110,110,0]){const candidate={x:s.x+(t.x-s.x)*fraction,y:s.y+(t.y-s.y)*fraction+offset,w,h};if(![...list,...labelBoxes].some(n=>intersects(candidate,n))){labelBox=candidate;break;}}if(labelBox)break;}
      if(!labelBox)labelBox={x:box.x+box.w+w/2,y:box.y+labelBoxes.length*(h+25),w,h};
      labelBoxes.push(labelBox);
      group.append(element('line',{x1:(s.x+t.x)/2,y1:(s.y+t.y)/2,x2:labelBox.x,y2:labelBox.y,stroke:'#788a9b','stroke-width':1,'stroke-dasharray':'3 4'}));
      group.append(element('rect',{x:labelBox.x-w/2,y:labelBox.y-h/2,width:w,height:h,rx:5,fill:'#f4f6f8'}));
      const label=element('text',{'data-edge-label':'true','text-anchor':'middle','font-size':12,fill:'#26394c'});lines.forEach((line,i)=>label.append(element('tspan',{x:labelBox.x,y:labelBox.y-(lines.length-1)*8.5+i*17+4},line)));group.append(label);
    }
    svg.append(group);
  }
  for(const n of list) {
    const g=element('g',{'data-node':n.id,tabindex:0,role:'button','aria-label':n.label,transform:`translate(${n.x},${n.y})`});
    g.append(element('rect',{x:-n.w/2,y:-n.h/2,width:n.w,height:n.h,rx:16,fill:color(n),stroke:n.id===selected?'#172637':'#ffffff','stroke-width':n.id===selected?3:1}));
    const text=element('text',{'text-anchor':'middle','font-size':14,fill:ink(color(n))});
    n.lines.forEach((line,i)=>text.append(element('tspan',{x:0,y:-(n.lines.length-1)*10+i*20+5},line))); g.append(text);
    g.append(element('title',{},[n.label,n.detail,n.status].filter(Boolean).join('\n')));
    if(!all){g.addEventListener('click',()=>{selected=n.id;details();render(false);});g.addEventListener('dblclick',()=>toggle(n.id));g.addEventListener('keydown',e=>{if(e.key==='Enter'){selected=n.id;details();render(false);}if(e.key===' '){e.preventDefault();toggle(n.id);}});}
    svg.append(g);
  }
  const fullBox=bounds([...list,...labelBoxes]);svg.setAttribute('viewBox',`${fullBox.x} ${fullBox.y} ${fullBox.w} ${fullBox.h}`);return svg;
}
function setView() {stage.setAttribute('viewBox',`${view.x} ${view.y} ${view.w} ${view.h}`);}
function render(fit=true) {const svg=buildSvg();stage.replaceChildren(...svg.childNodes); if(fit||!view){const [x,y,w,h]=svg.getAttribute('viewBox').split(' ').map(Number);view={x,y,w,h};}setView();}
function safeLink(url) {try{const u=new URL(url,location.href);return ['https:','http:','file:','obsidian:'].includes(u.protocol)?u.href:null;}catch{return null;}}
function appendLink(parent,label,url) {const href=url&&safeLink(url); const e=document.createElement(href?'a':'span');e.textContent=label;if(href){e.href=href;e.target='_blank';e.rel='noopener noreferrer';}parent.append(e);}
function details() {
  const n=byId.get(selected), panel=$('details');panel.replaceChildren();const h=document.createElement('h2');h.textContent=n.label;panel.append(h);
  for(const text of [n.detail,n.status&&`Status: ${n.status}`,n.weight!=null&&`Weight: ${n.weight}`].filter(Boolean)){const p=document.createElement('p');p.textContent=text;panel.append(p);}
  if(n.url)appendLink(panel,'Open map',n.url);
  const relevant=n.sourceIds?.length?n.sourceIds.map(id=>sourceById.get(id)):(n.id===root.id?sources:[]);
  for(const s of relevant){const p=document.createElement('p');appendLink(p,s.label,s.url);panel.append(p);}
  if(!n.detail&&!relevant.length){const p=document.createElement('p');p.textContent='Select another node for its details and sources.';panel.append(p);}
}
function toggle(id) {if(!children(id).length)return;collapsed.has(id)?collapsed.delete(id):collapsed.add(id);render();}
function zoom(factor) {const w=Math.min(100000,Math.max(120,view.w*factor)),h=w*view.h/view.w;view={x:view.x+(view.w-w)/2,y:view.y+(view.h-h)/2,w,h};setView();}
function notice(text) {$('notice').textContent=text;}
function download(blob,extension) {const a=document.createElement('a'),url=URL.createObjectURL(blob);a.href=url;a.download=(data.title||'map').toLowerCase().replace(/[^\p{L}\p{N}]+/gu,'_').replace(/^_|_$/g,'')+'_mindmap.'+extension;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),30000);notice('Download requested. This did not write to your vault.');}
function sourceMarkdown(n) {return (n.sourceIds||[]).map(id=>{const s=sourceById.get(id);return s.url?`[${s.label}](${s.url})`:s.label;}).join('; ');}
function canvasText(n) {const refs=n.id===root.id?sources.map(s=>s.url?`[${s.label}](${s.url})`:s.label).join('; '):sourceMarkdown(n);return [n.label,n.detail,n.status&&`Status: ${n.status}`,n.weight!=null&&`Weight: ${n.weight}`,refs,n.url&&`[Open map](${n.url})`].filter(Boolean).join('\n\n');}
function canvas() {
  const list=positions(true,true), edges=[...nodes.filter(n=>n.parent!=null).map(n=>({from:n.parent,to:n.id})),...links];
  return {nodes:list.map(n=>({id:n.id,type:'text',x:Math.round(n.x-n.w/2),y:Math.round(n.y-n.h/2),width:n.w,height:n.h,color:color(n),text:canvasText(n)})),edges:edges.map((e,i)=>({id:`edge_${i}`,fromNode:e.from,toNode:e.to,fromEnd:'none',toEnd:'none',...(e.label?{label:e.label}:{})}))};
}
function markdown() {
  const lines=[`# ${data.title}`];function emit(n,depth){if(depth)lines.push(`${'  '.repeat(depth-1)}- ${n.label}`);for(const value of [n.detail,n.status&&`Status: ${n.status}`,n.weight!=null&&`Weight: ${n.weight}`,sourceMarkdown(n),n.url&&`[Open map](${n.url})`].filter(Boolean))lines.push(`${'  '.repeat(depth)}  ${value.replace(/\n/g,' ')}`);for(const child of children(n.id))emit(child,depth+1);}emit(root,0);
  if(links.length)lines.push('\n## Cross-links',...links.map(e=>`- ${byId.get(e.from).label} ↔ ${byId.get(e.to).label}: ${e.label||'related'}`));
  if(sources.length)lines.push('\n## Sources',...sources.map(s=>`- ${s.url?`[${s.label}](${s.url})`:s.label}`));return lines.join('\n')+'\n';
}
function mermaid() {const ids=new Map(nodes.map((n,i)=>[n.id,`n${i}`]));const label=s=>String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\n/g,' ');return ['flowchart LR',...nodes.map(n=>`  ${ids.get(n.id)}["${label(n.label)}"]`),...nodes.filter(n=>n.parent!=null).map(n=>`  ${ids.get(n.parent)} --- ${ids.get(n.id)}`),...links.map(e=>`  ${ids.get(e.from)} ---|"${label(e.label||'related')}"| ${ids.get(e.to)}`)].join('\n')+'\n';}
function html() {const copy=document.documentElement.cloneNode(true);copy.querySelector('#mindmap-data').textContent=JSON.stringify({...data,view:{layout,palette}}).replace(/</g,'\\u003c');copy.querySelector('body').classList.remove('fullscreen');return '<!doctype html>\n'+copy.outerHTML;}
function svgText() {const svg=buildSvg(true),[x,y,w,h]=svg.getAttribute('viewBox').split(' ').map(Number);svg.setAttribute('width',Math.ceil(w));svg.setAttribute('height',Math.ceil(h));svg.prepend(element('rect',{x,y,width:w,height:h,fill:'#f4f6f8'}));return new XMLSerializer().serializeToString(svg);}
async function exportFile(format) {
  if(format==='html')return download(new Blob([html()],{type:'text/html'}),'html');
  if(format==='md')return download(new Blob([markdown()],{type:'text/markdown'}),'md');
  if(format==='mmd')return download(new Blob([mermaid()],{type:'text/plain'}),'mmd');
  if(format==='canvas')return download(new Blob([JSON.stringify(canvas(),null,2)],{type:'application/json'}),'canvas');
  const xml=svgText(); if(format==='svg')return download(new Blob([xml],{type:'image/svg+xml'}),'svg');
  if(format==='png') {
    const url=URL.createObjectURL(new Blob([xml],{type:'image/svg+xml'}));
    try {const img=new Image();await new Promise((resolve,reject)=>{img.onload=resolve;img.onerror=reject;img.src=url;});const c=document.createElement('canvas');const scale=Math.min(2,12000/Math.max(img.width,img.height));c.width=Math.ceil(img.width*scale);c.height=Math.ceil(img.height*scale);c.getContext('2d').drawImage(img,0,0,c.width,c.height);const blob=await new Promise(resolve=>c.toBlob(resolve,'image/png'));if(!blob)throw Error('PNG encoding failed');download(blob,'png');}finally{URL.revokeObjectURL(url);}return;
  }
  if(format==='pdf') {
    const page=window.open('','_blank');if(!page)throw Error('Print window unavailable; use a local browser PDF export');
    page.document.title=data.title;const style=page.document.createElement('style');style.textContent='@page{size:landscape;margin:12mm}body{font:12px system-ui}svg{width:100%;height:82vh}';page.document.head.append(style);const title=page.document.createElement('h1');title.textContent=data.title;page.document.body.append(title);page.document.body.append(new DOMParser().parseFromString(xml,'image/svg+xml').documentElement);page.document.close();page.focus();page.print();notice('Print view opened. Choose Save as PDF; no PDF has been saved by this button.');
  }
}
$('title').textContent=data.title;document.title=data.title;
$('palette').replaceChildren();
for(const name of Object.keys(palettes)){const o=document.createElement('option');o.textContent=name;$('palette').append(o);}
$('palette').value=palette;$('layout').value=layout;
$('layout').onchange=e=>{layout=e.target.value;render();};$('palette').onchange=e=>{palette=e.target.value;render(false);};
$('zoom-in').onclick=()=>zoom(.8);$('zoom-out').onclick=()=>zoom(1.25);$('fit').onclick=()=>render();
$('collapse').onclick=()=>toggle(selected);$('expand').onclick=()=>{collapsed.clear();render();};
$('focus').onclick=()=>{focused=selected;collapsed.delete(selected);render();};$('back').onclick=()=>{focused=null;render();};
$('fullscreen').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else if(document.documentElement.requestFullscreen)await document.documentElement.requestFullscreen();else document.body.classList.toggle('fullscreen');}catch{document.body.classList.toggle('fullscreen');}};
document.addEventListener('keydown',e=>{if(e.key==='Escape')document.body.classList.remove('fullscreen');});
$('download').onclick=()=>exportFile($('format').value).catch(error=>notice(`Export failed: ${error.message||error}`));
stage.addEventListener('wheel',e=>{e.preventDefault();zoom(e.deltaY>0?1.1:.9);},{passive:false});
stage.addEventListener('pointerdown',e=>{if(e.button!==0||e.target.closest('[data-node]'))return;const point=new DOMPoint(e.clientX,e.clientY).matrixTransform(stage.getScreenCTM().inverse());drag={point,view:{...view},matrix:stage.getScreenCTM().inverse()};stage.setPointerCapture(e.pointerId);});
stage.addEventListener('pointermove',e=>{if(!drag)return;const point=new DOMPoint(e.clientX,e.clientY).matrixTransform(drag.matrix);view={...drag.view,x:drag.view.x-(point.x-drag.point.x),y:drag.view.y-(point.y-drag.point.y)};setView();});
stage.addEventListener('pointerup',()=>{drag=null;});stage.addEventListener('pointercancel',()=>{drag=null;});
window.Mindmap={data,positions,canvas,markdown,mermaid,html,svgText,exportFile};
render();details();notice(data.kind==='atlas'?'Selected-map atlas snapshot. Links connect only the maps supplied for this view.':'Select a node to inspect its details and sources.');
})();
</script>
</body>
</html>
```
