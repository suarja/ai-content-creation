---
name: explainer-script-and-beats
description: Write the 20–45 second voice-over script of a mascot explainer video and its beats.json — which pose, card, title or background lands on which phrase. Use when starting an explainer or app-promo video in the explainer-video-pipeline format, when its rhythm feels flat, when the script changes and the beats must follow, or when the video speaks for a real person and must sound like them (their bank, breath groups, hook, caption).
---

# Script and beats

## The script

script.txt, one line per phrase that deserves its own visual. Lines starting with `#`
are ignored. Aim for 90–130 words (≈ 30 s at 190–245 words/min). The author of the
format sums up what matters, in order: **subject, hook, rhythm**.

Structure that works for a product:

1. **Hook** (first 2 s): a situation the viewer recognises, or a number. "You're watching
   a forty-minute political debate…"
2. **Pain**: what goes wrong, in their words. One or two lines.
3. **Reveal**: "So we built <Product>." — one short line, it gets the title and
   a background change.
4. **How it works**: 3–5 lines, one concrete action each (paste the link, get the
   summary, tap a word…). Each line is a card.
5. **Offer**: the free trial, the price, the first-use gift. One line.
6. **CTA that asks for a comment**, not a like: "Tell me in the comments which video
   you want decoded." Comments feed the algorithm and the next video.

Rules:

- Spoken language, second person, short words. Read it aloud; cut every line that
  needs a breath in the middle.
- Speak outcomes, not features or internal vocabulary. A domain word the viewer has
  never heard is a defect.
- Every claim about the product must be true today. Mark a target ("in a minute")
  as something to verify before publishing.
- Write numbers in words when the voice must say them ("forty minutes"); the title
  can show "40 MIN".
- Keep the real spelling of the product name: captions print script.txt. If a
  synthetic voice mispronounces it, respell it only in the text sent to the voice
  (see `explainer-voiceover`).
- Write the script in the language of the video. The examples below are English; the
  rules hold in any language.

## Write in the author's voice

When the video speaks for a real person (their cloned voice, their avatar), the script
is written the way they talk, not the way an assistant writes.

- **Build their bank first**: transcripts of their own videos (`yt-dlp` + `npx hyperframes
  transcribe`, see `explainer-voiceover`), their captions, and their hooks ranked by
  views. Read it before writing. Keep the bank in the project's content folder, next to
  the episodes that use it.
- **One line = one breath group of 2–6 words**: "What I do / is I keep / Claude / for when
  I'm stuck." The voice is then generated line by line.
- **First person and a story beat**: "In January, I blamed Claude" beats a stated
  fact. A callback to one of their real past videos is both proof and story.
- **Their tics, sparingly**: the expressions that recur in their transcripts ("basically",
  "so yeah", "let's be honest") — two or three per video.
- **Every claim proven**: a personal claim ("I set autocompact to 400k") is checked with
  the person before recording.

## The hook

The first two seconds carry one idea, said like to a friend. Rank the author's own
hooks by views before writing one. On one creator account, the winners were a curiosity
("Everyone keeps asking me…", 57 k), a strong promise ("What you absolutely need to
know…", 23 k), a concrete image ("my whole life for the price of a coffee", 8.8 k) or a
contrarian slogan ("X is dead, long live Y"); the losers started in the middle of an
explanation (291 views). A descriptive hook ("Picking up yesterday's conversation?")
was rejected as too descriptive; "If you hit your limit on Claude Code, it's not Claude.
It's you." was accepted. Then pain in their words, then the proof.

Two more refusals from the same author:

- A metaphor the viewer has to decode: "Your Claude Code plan has a hole: your
  subagents" — the author could not follow what the hole was.
- A recap before the subject: "In part 1, we talked about the cache" pushed the first
  fact to 7 s; cut, the subject arrived at 3.8 s.

When a hook is refused, do not write a third one alone: offer five or six, each built on
one of the author's winning hooks and named after it ("What you absolutely need to
know…", 23 k), with a recommendation. The author picked "What you absolutely need to
know before running subagents on Claude Code."

## Caption

Write the caption from their own captions: their opening emoji habit, a series marker
("Part 1 |"), one line of promise, the one setting or takeaway, a "follow for part 2: …"
teaser, a question for comments, 4–5 hashtags. Sources go in a pinned comment, not the
caption.

## The beats

beats.json is an ordered array. Each beat is anchored on a phrase of the script with
`at` (whole words, punctuation ignored, searched after the previous beat). Never on
seconds: the same beats survive a new voice.

```json
[
  { "at": "You're watching", "pose": "bored", "card": "player", "props": { "tag": "DEBATE · LIVE", "total": "40:00" } },
  { "at": "forty-minute", "title": "<em>40</em> MIN" },
  { "at": "and at the end", "pose": "lost", "card": null },
  { "at": "built Recap", "pose": "proud", "title": "RECAP", "bg": "brand" },
  { "at": "Paste the link", "pose": "phone", "card": "input", "bg": null, "steps": ["YouTube", "TikTok"],
    "props": { "label": "VIDEO LINK", "text": "youtube.com/watch?v=debate", "button": "DECODE" } }
]
```

| Key | Effect | Holds until |
| --- | --- | --- |
| `pose` | swaps the mascot sticker (file character/cut/<pose>.png) | next `pose` |
| `card` + `props` + `steps` | a card from explainer-video-pipeline/references/cards.md; `null` clears | next `card` |
| `title` | a huge word replacing the caption; `<em>` = accent, `<sup>` allowed | next beat of any kind |
| `bg` | `brand`, `accent` or `ink` full-screen background; `null` returns to paper | next `bg` |

Rhythm rules, from the reference videos:

- A new pose, card, title or card step at least every ~1–1.5 s. The build prints the
  longest still stretch; above ~2 s add a pose beat or a step.
- The pose illustrates the words of its phrase, literally: "you" → pointing at the
  viewer, "free" → holding a gift, "stuck" → confused. If no pose fits, add one
  to character/poses.tsv rather than reusing a vague one.
- Titles only on 2–4 key nouns or numbers per video, ≤ 9 characters. A longer one
  ("SUBAGENTS") spills over the caption area and was seen as overlapping text.
- A title needs ~0.8 s on screen too: anchored on a short line, "A HOLE" showed for
  0.55 s and went unseen. Check the beat times in build/timing.json and move the next
  anchor later.
- One background change, at the reveal.
- A card needs at least ~0.8 s on screen; shorter, merge it with the next beat.
- Two titles on back-to-back beats inside one spoken phrase leak the caption under the
  second title (seen on "One hour… Five minutes"): keep one of them.
- A title on the `brand` background is drawn in ink on a dark ground and cannot be read;
  keep titles on paper.

Then list every pose the beats use: that list is the input of `explainer-mascot-poses`.
