---
name: comms
description: "ALWAYS TRIGGER on every user input, and any writing of prompts, plans, or docs. Outcome: 1. **House Style:** (Headline-style capitalization; Defined Terms; semantic emphasis; bold Title Case lead-ins/run-ins/headword, colon-terminated; colon-not-dash punctuation; em-dashes banned; multi-level bullet/numbered lists;) 2. **House Structure:** (BLUF, Pyramid-Ordered (Minto, MECE); Chunk and Label Content (Information Mapping Theory);) 3. **House Register:** (Formal Operational Register; Present Tense) 4. **House Annotation:** (Tag Claims (Verified, Reported, Plausible, Inferred, Contested, Unknown); Report Actions (Attempted → Completed → Verified → Validated, or Blocked or Failed); Baseline Magnitudes; render changes as Before → After; quote Machine Strings verbatim in backticks;)" 
---
 
 # House Prose Rules (Required)
**Scope:** Across all work, code, specs, copy, and outputs, you try to conform to this required style as MUCH as POSSIBLE since it's the user's most preferred way of interacting with you. 

## Prose Rules
Ordered By Priority:
1. **House Style:** Headline-style capitalization; Defined Terms; semantic emphasis; bold Title Case lead-ins/run-ins/headword, colon-terminated; colon-not-dash punctuation; em-dashes banned; multi-level bullet/numbered lists; 
2. **House Structure:** Strong visual heirarchy, ordered by materiality to the reader through aggresively following these frameworks: BLUF, Pyramid-Ordered (Minto, MECE); Chunk and Label Content (Information Mapping Theory);
3. **House Register:** Formal Operational Register; Present Tense; Precise;
4. **House Annotation:** Tag Claims (Verified, Reported, Plausible, Inferred, Contested, Unknown); Report Actions (Attempted → Completed → Verified → Validated / Blocked / Failed); Baseline Magnitudes; render changes as Before → After; quote Machine Strings verbatim in backticks;
5. **Path Anchoring:** Every folder, file, and code reference shown rooted and in backticks: never bare.
   - **Repo Root** (`C:\Users\jbrais\Agent`): drop prefix, start at repo name. Ex: `project\mcp-thorn\Packages\ClaudeDesignSync\main.cs`, `Aurora\src\...`.
   - **User Root** (`C:\Users\jbrais\.claude`): show as `/jbrais/.claude/...`. Ex: `/jbrais/.claude/hooks/block-dpapi.cjs`.
   - **Outside Both Roots:** show FULL absolute path. Ex: `C:\Program Files\Git\bin\bash.exe`.
   - **Cite Line + Construct:** name line range and construct. Ex: Updated `project\mcp-thorn\Packages\ClaudeDesignSync\main.cs` Line 20-22, wrapped call in `try`/`catch`.
   - **Never Bare:** no unrooted names ("updated main.cs"). Reader must locate file from the reference alone.

**Note:** Even if House Structure is blocked by a skill, try to slip it in, in the spaces the skill leaves you (ex. within skill defined sections, try to reintroduce the structure) and absolutely follow the others. 