---
name: "decoding-trends-in-shorts"
description: "Make a silent vertical promo Short in which the app's mascot decodes a trending creator's video or account with the app's real analysis, then invites the viewer to try it on their own. Use when producing a product Short for TikTok, Instagram Reels or YouTube Shorts from a trending video, when picking the trending video of the week, or when such a Short feels static."
---

# App decode Shorts

The product account posts a 15–20 s Short: a few seconds of a creator's trending video, then the
app's mascot shows what the app's analysis found, then "and yours?". The proof is the real analysis
on screen. No voice: text on screen, music added by the author at publication (the platform
handles the rights).

This format suits an app that analyses something the viewer also has: a video, an account, a
recipe, a photo. The steps below use video analysis as the example.

## 1. Find the video (read only, in the author's signed-in browser)

- TikTok web search has no date filter and favours old videos. Decode the date from the video id:
  creation time in seconds is `id >> 32` (use BigInt). Keep videos of 10 days or less.
- Queries that surface recent creator videos: a niche word plus the month ("recipe october",
  "grwm october", "small business october") or format words ("storytime", "recipe", "morning
  routine"). Read the like count on the card; search shows likes, not views.
- Get each title from `https://www.tiktok.com/oembed?url=<video url>` (fetch from the TikTok tab).
- The Creative Center trend pages need an account: not usable. Scrolling the For You feed with a
  script froze the tab.
- Skip politics, news outlets and accounts outside the target language. Prefer a niche the app's
  users share. Offer five with age, likes and niche, recommend one, the author picks.
- Never like, follow, comment or post from the author's account.

## 2. The real analysis

The analysis runs inside a signed-in account. The author launches it in the app; never sign in for
them. With their permission, open the result on a simulator and capture each screen while
scrolling (`xcrun simctl io booted screenshot` after each swipe; stop when two captures are
identical). Touch nothing else in the app.

Ask before downloading the creator's video (filename, source, size), keep it out of git, and use
only 2–3 s of it, with the creator named on screen.

## 3. The edit (1080 × 1920)

1. Opening, 2–3 s: the creator's first seconds, a big line with the striking number ("4 million
   likes on a recipe.") and the handle.
2. The mascot introduces itself in the first person ("I'm <mascot>. I took their account apart.").
3. Three findings, one per beat: a short title that carries the message, the result screen as proof.
4. End: the mascot pointing at the viewer, "And yours?", the app name and "link in bio".

A phone screen shown whole is too small to read: the title says the finding, the screen proves it.
Still slides read as static. Animate: record the result scrolling (`xcrun simctl io booted
recordVideo`), push in on the key sentence and draw a marker highlight over it, count the numbers
up, slide the cards in, pop the mascot's poses in rhythm. Build it with HyperFrames; the kit and
traps are in `designing-motion-promo-shorts`, the mascot poses in `explainer-mascot-poses`.

## 4. Caption and hand-over

Caption (see `captioning-short-videos`): "I decoded @creator's account" plus one emoji and the
striking number on line 1; one action on line 2; four or five hashtags. Pinned comment: the
analysis was made on a public account, a compliment to the creator, a question about which account
to decode next, then the app line.

Cite the creator only; no private message unless the author says so. Never mock the creator.

Keep one episode folder: the render project, sources out of git, the result captures, and a
publication file with proofs (video link, date, likes, every number shown on screen).
