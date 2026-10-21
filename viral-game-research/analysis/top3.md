### Kill thresholds that apply to all three tests

These come from `model/dau_math.csv`. Reaching 1M DAU by day 90 from about 1,000 seed players takes a sustained 8–9-day doubling, which is **about +70–80% more new players week over week**. At small scale, that rate requires one of these pairs:
- D7 retention of at least 20% with at least **0.33 new players per active player per day**; or
- D7 retention of at least 40% (ritual-grade) with at least **0.21**.

Below that, the game can still be a fine business. It won't reach 1M DAU in 90 days without paid marketing.

### #1 Hide as a Painting (Roblox)
**What it is:** prop hunt in a haunted museum.
- Hiders pick a frame or pedestal and pose as a painting or statue. Guards with flashlights get three minutes and a limited number of accusations.
- A new gallery layout each day, the same for every server, with a "best hiding spot of the day" board.

**Why the model ranks it first or second:**
- Spectator value is high: hide-and-seek reveals make good clips.
- Failure comedy (a "painting" caught mid-twitch) and emergent output (absurd avatar portraits worth screenshotting).
- Borrowed rules: hide-and-seek and Statues.
- Real friends graph and a channel whose recommender rewards co-play.

**Risk:** prop hunts already exist on Roblox. The museum, the posing and the daily shared layout are the difference, and that difference has to show in the first 10 seconds of a clip.

**Cheapest demand test (about 10 days, $0–50):**
1. **Days 1–3: watchability test before building.** Record three 15-second greybox clips in Roblox Studio (catch moment, pose reveal, near miss) and post them to TikTok and YouTube Shorts. Compare share and completion rates with your own median post. **Kill if** none beats your median.
2. **Days 4–10: one map, one round loop, published.** Recruit 30–50 players from 2–3 Roblox Discord communities. **Pass** if Creator Dashboard shows D1 at least 35%, average session at least 10 minutes, and a third or more of sessions in parties.
3. **Optional measurement buy:** spend $50 on Roblox sponsored ads to get an unbiased retention cohort. This is a measurement, not growth marketing.
4. **Weeks 3–6:** count organic visits week over week once the recommender starts testing it. **Keep going** only at +70% a week or better for two consecutive weeks.

### #2 Pictionary Obby (Roblox)
**What it is:** the artist gets a secret word and draws it. The strokes become the platforms of an obstacle course that teammates run while guessing the word. Points go to fast guesses and finishes.

**Why it scores high:**
- Spectator value is high, and it produces emergent, funny output: every course is a bad drawing you have to run across.
- Borrowed rules (Pictionary) and co-play.

**Risks:**
1. **Moderation.** Freehand drawing on a kids' platform needs stroke limits, filtering and report/kick tools. Existing Roblox drawing games show it's possible, but budget time for it.
2. **Physics.** Turning arbitrary strokes into fair platforms is the technical risk, and it should be prototyped first.

**Cheapest demand test (about 2 weeks, $0–50):**
1. **Days 1–4:** build a stroke-to-platform prototype and run the same three-clip watchability test as #1.
2. **Days 5–14:** a private server with 4–8-player lobbies, recruited from Discord. **Pass** on the same retention and party thresholds as #1, plus at least 3 rounds per session.

### #3 Telephone Pictionary Chains (web)
**What it is:** an asynchronous telephone game built for group chats.
- One person gets a prompt and draws it in 60 seconds. A link passes to the next person, who captions the drawing. The next person draws the caption, and so on.
- After six steps the whole chain plays back to the group as a 6-second GIF.
- No accounts. Static front end plus a tiny key-value backend, so it costs almost nothing per player.

**Why it scores high:**
- Invite-needed loop, borrowed rules (the Telephone/Gartic Phone family), high spectator value, failure comedy and emergent output.
- Gartic Phone needs everyone online at once. Doing it asynchronously in group chats removes that coordination cost.

**Risk:** the web channel has weak evidence for zero-ad 1M-DAU breakouts, and Gartic Phone owns the synchronous version.

**Why test it first anyway:** it is the cheapest way to **measure the k-factor directly**. Every chain link carries the sender's ID, so new players per active player per day is counted, not estimated.

**Cheapest demand test (about 1 week, ~$10 hosting):**
1. Build the 6-step chain and GIF playback.
2. Seed it in 10 of your own group chats and 3 relevant subreddits.
3. Measure the share rate and D7 from the link graph. **Pass** if new players per active player per day is at least 0.33 with D7 of at least 20%. **Kill** below 0.2.

### Recommended order
1. Run #3's one-week test first. It gives you a real, measured share rate on day 7.
2. Run #1's clip test in parallel.
3. Build whichever Roblox concept passes the clip and retention tests.
4. If one breaks out, the Grow a Garden pattern applies: bring in a live-ops partner for a minority stake, and don't sell.
