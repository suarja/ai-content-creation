---
name: "designing-motion-promo-shorts"
description: "Make a silent, motion-designed vertical Short (TikTok, Reels, YouTube Shorts) that promotes an app through a creator tip, a user pain, a story or an outcome — infographics, kinetic type, a phone showing real app screens and the app's mascot, built in HyperFrames, music added at publication — then hand it over ready to post with its caption and translated versions. Use when asked for a promo video, a motion-design or infographic Short, a tips, POV or storytelling video for an app, a series of promo Shorts for one app, the English or Spanish version of one, or when a promo Short reads like a feature tour."
---

# Motion promo Shorts

A 16–26 s vertical Short, no voice, that presses on something the viewer feels (a pain, a story,
an outcome they want, or a tip they can use tonight) and ends on the app as the way out. The look
is the app's own design system and mascot. The author adds a trending sound in the TikTok or
Instagram editor when publishing.

Text-only slides do not work: the format is infographics and motion design, polished and
eye-catching, with real app screens as proof.

## Hard rule: narrative, never a feature tour

This is the most common mistake. Every Short presses on something the viewer feels. The app only
enters at the end, as the way out; it is never the subject of the scenes.

Before writing any HTML:

1. Write the spine in one line: the viewer's situation → what hurts or what they want → the turn
   → the app as the way out. Example: you film what you love → stuck at 300 views → your niche
   watches day-by-day challenges, the same recipe redone that way → the app's niche tab shows it.
2. Write each scene title. If a title says what the app does ("It reads your videos", "Type your
   handle"), the video has slid into a feature tour: rewrite the title around the viewer ("You've
   posted for 3 months without knowing what's wrong").
3. At most one scene, the last before the end card, may show the app working; the end card names
   the feature in one line.

A clean descriptive video can still go out, but it is a miss: tag it "to rework" (see below) with
the narrative angle to try next.

## Three formats that cover most needs

Make them as a set for one app; they share one kit (see "The kit").

| Format | Shape | Length |
| --- | --- | --- |
| Storytelling with the mascot | the mascot lives the problem the app solves, day by day, then the phone shows the app keeping track | 22–26 s |
| Educational tip | "note these 3 dates", "3 hooks to steal": each item has its name, the rule, an example in context and a "why it works" line; the app does the remembering at the end | 24–28 s |
| POV / before-after | "POV: your notes are everywhere" — the chaos piles up (sticky note, calendar alert, notebook, 2,431 photos), a counter ("5 places. 0 answers."), everything swept away, then one place: the app | 18–22 s |

## Angles for one feature

A feature video is not a tour of the screen. Each feature gets several videos, one angle each,
chosen before the script:

| Angle | The video shows |
| --- | --- |
| Pain | the user's problem, as a POV, before any app |
| Story | one user's week, a before and an after |
| Outcome | the result first, then how |
| Tips | a rule the viewer can use tonight, the app at the end |

Start a new feature with the pain or the outcome angle; the tips angle tends to slide into a
feature list. The pain shape that works: the viewer's own situation, what others do differently,
the same thing redone the other way, then the app screen that shows it. Across a week, vary the
shapes (POV, quiz, data story, carousel, timeline) so two days in a row never look the same.

Algorithm myths or factual tips ("true or false") need an official source for each answer
(platform newsroom, creator portal, public statement), quoted in the publication file. No source,
no card.

## The visual hook, without a voice

The first second carries everything. Before building, write the hook frame as one sentence a
viewer understands with the sound off and no context: who, what problem or what result. Then check
the draft's frame at 0.3 s against it. If it needs the next scene to make sense, it fails. A label
("01 What's rising") or an app screen is never a hook on its own.

## Guide the eye

Tell the viewer what to look at, at every moment, and make it jump out:

- One thing moves at a time. In a grid, reveal each item's key value one after another (about
  0.35 s apart), not all at once.
- The value being compared is the biggest, most contrasted element of the item (a large badge with
  an ink border, 46 px or more), not a small caption in a corner.
- Each value pops with an overshoot (scale up then settle) and counts up; its item gets a small
  punch.
- The odd one out comes last, in another colour, with a pause before it and a shake after it.
- Then one sentence names the comparison ("5 videos out of 6: a dated challenge").
- In a sheet of icons or buttons, fade the others to 0.3, grow the target with a pulse ring, then
  show the tap ripple.

## The kit

Before the first video of an app, build one kit that every video copies:

- **Tokens** from the app: its colours (read them from the app's theme file, never guess from a
  screenshot), its font files declared with @font-face, its corner radii.
- **The mascot**: the app's own, or one created with `explainer-mascot-poses` (one reference
  image, then a bank of 12–16 poses cut out on transparent backgrounds). Pick the pose that says
  the line: shrugging on a flop, a magnifier on "why", a light bulb on the lesson, cheering on the
  end card.
- **A phone frame** that holds real captures of the app, with a fake status bar (9:41) so the
  device notch never covers the capture.
- **Masks for test data**: captures from a test account often show impossible values (day 159 of
  21, a year 1425). Cover each one with a small absolutely placed patch in the capture's own
  background and text colours, its font size in container-query units (cqw) so it scales with the
  phone. Never edit the capture file itself.
- **One signature transition** tied to the app's subject, reused at every scene change (for an
  egg-incubation app: the next scene rises with a zigzag eggshell edge, a clip-path polygon).
- **One running motif** that carries the story across scenes (a row of 21 egg dots that light up
  day by day).
- Helpers: mascot pop from below, idle breathing (the mascot never stands still), word-by-word
  reveal, count-up, wipe.

Keep the kit in one folder (kit.css, kit.js, fonts, assets) and copy it into each video project:
renders stay reproducible and one video's change never breaks another.

## Look

- Cards in white with a 3–4 px ink border and a hard ink shadow; ink pills with a coloured dot;
  marker highlights drawn under a word; a light grain and a dot grid on the background; one
  oversized ghost word bleeding off the frame; blurred pastel blobs; one background colour per
  chapter, ink for the lesson. A dark "software" ground with a faint grid works too.
- An app screen can be rebuilt in HTML from a validated mockup when no capture is possible; a
  screen inside a dark scene needs its own text colour, or it inherits the scene's and disappears.

## Timing

- Hook on screen by 0.3 s, the question or promise readable within 1.5 s.
- Every text needs about 1 s per 3 words after it has landed, plus 0.5 s. A chapter ending on a
  "why it works" card needs about 6 s; a quiz card about 5 s (question, countdown, flip, verdict).
- A chart holds at least 2 s after its last element lands.
- No dead time: something new (pose, card, word, counter) at least every 1–1.5 s.
- Total 16–26 s. Safe zones: nothing important above 200 px or below 1620 px; keep the right
  140 px clear of key data (the platform's buttons).

## Component library

| Component | How |
| --- | --- |
| Count-up number with growing scale | proxy tween with onUpdate writing textContent, locale formatting, tabular-nums |
| Fill bar, time counter (0 h → "2 days") | scaleX from 0 on a left-origin bar, same timing as the counter |
| Sparkline, retention curves | SVG path, stroke-dasharray = length, dashoffset from length to 0 |
| Highlighted zone on a chart | rect scaleY from 0, dashed line, ink label |
| Burst of rays | ten rotated bars in a container, scale in then out |
| Mascot pop with speech bubble | back.out entrance from below with rotation; reset x too, or an earlier slide leaves it off-frame |
| Wipe, circle reveal, slide-up | clip-path inset, clip-path circle from a focal point, yPercent |
| Story progress bars | one segment per chapter, scaleX 0 → 1 over the chapter |
| Carousel push | incoming scene x 1080 → 0 while the outgoing one goes to −1080 |
| Outlined number slam | text-stroke and hard text-shadow, scale 2.6 → 1; fade it out before the next big title lands |
| Template with a blank | underline span drawn with scaleX, then pulsing |
| Phone with typed overlay | ink frame, typewriter via onUpdate and a blinking caret |
| Hand-drawn arrow | SVG path draw, then the head |
| "Why it works" card | white card, grey label, marker sweep under the second sentence |
| 3D flip number, stamp | rotationX from −95 with transformPerspective; stamp drops from scale 2.4 |
| Editing timeline (ruler, clips, waveform, playhead) | a 2400 px world at 80 px per second; deterministic sine waveform bars |
| Camera zoom per part | one proxy object tweened with fromTo; onUpdate sets scaleX and re-places labels, so text never stretches |
| Checklist that ticks itself | SVG check path draw plus a box pop |
| Quiz countdown ring | SVG circle dashoffset over 1.7 s while a "?" pulses |
| 3D card flip with verdict stamp | perspective on the wrapper, preserve-3d inner, two faces with backface hidden; stamp outside the 3D layer |
| Grid with one free slot | tiles pop with stagger, a dashed tile pulses, then fills with the answer |
| Values popping one by one in a grid | badge scale 0 → 1.25 → 1, count-up, tile punch 1.06; tiles without overflow hidden so the overshoot shows |
| Multi-line marker highlight | inline span with a linear-gradient background, box-decoration-break clone, backgroundSize 0% → 100% |
| Crossed-out old line, typed new one | strike bar scaleX 0 → 1, then the new line typed |
| Share sheet, target icon singled out | sheet slides up, icons pop one by one, others fade to 0.3, target scales 1.22 with a pulse ring, tap ripple |
| A or B duel with reveal | two cards slide in from both sides, countdown ring, the winner punches; the loser fades to 0.45 and shakes |
| Piling chaos | sticky note, alert, notebook, photo counter drop in at slight angles, each with a small shake; one sweep clears them |

## Build loop

1. Copy the closest previous video folder (kit, fonts, assets, hyperframes.json), or
   `npx hyperframes init` and copy the kit in.
2. Write index.html: scenes as clips on separate tracks, overlapping by the transition length,
   one paused GSAP timeline registered on window.__timelines.
3. `npx hyperframes lint` until 0 errors (pin the CLI version in the project for reproducible
   renders).
4. Render a draft (`--quality draft`), pull six key frames with ffmpeg into one contact sheet, and
   look: overlaps, orphan words, dead space, unreadable holds, where the eye goes in each frame.
5. Fix, then render with `--quality high`, delete the draft.

Several videos can be built in parallel by separate agents from one shared kit; give each its own
temporary folder, or one overwrites the other's contact-sheet script.

HyperFrames traps:

- Tweening top, left or letterSpacing is a lint error: use x, y, scale.
- A later fromTo on the same element needs immediateRender false, or it overwrites the entrance's
  starting state.
- A round line cap shows a dot before a path draws: animate opacity with the dashoffset.
- z-index −1 under a word needs a stacking context on the parent (isolation isolate).
- A phone entering from below must start fully out of frame (y 1400, not 900).
- Clips generated by script from one data array render correctly: use it when chapters share a
  template.
- Measure a clipped viewport with clientWidth at build time, never a hand-typed width.
- preserve-3d flips render correctly; keep stamps and mascots outside the flipping element.
- A short word wraps alone after a number or at the end of a title: glue it with a non-breaking
  space, also before a French colon. Big display titles often need a manual line break.
- A badge over a card's top edge covers its first line: put it on the bottom edge.
- Two stacked cards of unknown height: leave 40 px or more between them and check the contact
  sheet when one gains a line.
- Dots or motifs in a light colour vanish on a dark scene: give them a mid-tone that reads on
  both.
- Nested-structure lint warnings (scenes with nested divs) are expected and do not block.

## Translated versions

Each language gets the same video with its on-screen text redone; the same video never goes out
unchanged on two accounts.

1. Copy the folder to the same name with -en or -es, delete its renders, rename the id, set lang
   on the html tag.
2. Replace only the strings, with one replacement list in a short script that prints every source
   string it did not find; animation and timings stay identical. Then grep for leftover accents
   and words of the source language.
3. Formats. EN: 1.2M and 640K, 80,412, $5, "Mon, Oct 19". ES: neutral Spanish with tú, 1,2 M and
   640 mil, opening ¿ and ¡. Change the number formatter too, not only the labels.
4. Real app captures must be in the target language: capture the app again in that language,
   or rebuild the screen from the app's own translation files. A French screen in an English video
   is a defect.
5. Translated lines are longer or shorter and rewrap: check the contact sheet again, and shorten
   the line rather than shrink the type.
6. The caption is written again from the video with `captioning-short-videos`, not translated.

## Claims

- The end-card promise must be true in the shipped app today. Check the app code, not only its
  strings: when two screens disagree, the code wins.
- Know what a free account sees; an end card promises nothing that is paid only.
- Feature videos go out only once the feature is in the store.
- Invented POV numbers are a scenario; the publication file says so, the video never presents them
  as real data and never promises a view count after using the app.
- Dates and numbers in an educational tip come from a source (the app's own guide, an official
  page), named in the publication file.

## Weak videos: the "to rework" tag

A video that goes out but does not make its point clearly gets a quality line at the top of its
publication file: "Quality: to rework · <why, in one line> · <angle to try>". The next video for
that feature starts from it.

## Hand-over, every video

1. A publication file in the video folder: status, quality line if weak, target accounts, video
   path, duration, music note, hook frame sentence, sources, caption and pinned comment (from
   `captioning-short-videos`).
2. The high-quality render, plus one per translated version.
3. Never publish or schedule on the author's accounts without being asked; drafts only, and only
   in a session the author signed in to.
