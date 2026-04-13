# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

The system processes songs through a weighted scoring algorithm that compares each song's attributes against the user's preferences. Each song in the dataset is individually evaluated, scored, and then ranked to produce the final recommendations.

### Algorithm Recipe

**Highest Priority Attributes:**
- Genre Match: +3.0 points (exact), +1.5 points (related genre)
- Mood Match: +2.5 points (exact), +1.2 points (related mood)
- Energy Similarity: +2.0 points max, calculated as `2.0 * (1 - |energy - target_energy|)`

**Medium Priority Attributes:**
- Tempo Similarity: +1.5 points max, calculated as `1.5 * (1 - |tempo - target_tempo| / 120)`
- Valence Similarity: +1.5 points max, calculated as `1.5 * (1 - |valence - target_valence|)`
- Danceability Similarity: +1.0 point max, calculated as `1.0 * (1 - |danceability - target_danceability|)`

**Lowest Priority Attributes:**
- Artist Similarity: +0.5 points (if artist matches user's favorites)
- Acousticness Preference: +0.5 points (if matches user's likes_acoustic preference)

**Final Processing:**
- Apply 10.0 point cap per song
- Sort all songs by total score (descending)
- Return top K recommendations (typically 3-5 songs)

### Potential Biases

This system might over-prioritize genre matches, potentially overlooking great songs that perfectly match the user's mood and energy preferences but belong to different genres. The heavy weighting on genre (+3.0 points) could create filter bubbles where users are rarely exposed to music outside their preferred genres. Additionally, the binary acousticness preference may oversimplify user taste, as some users might prefer acoustic versions of certain songs but not others.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo

 Values such as the genre, mood, and energy will be the ones with the highest weight. Then values like valence, dancability, and tempo_bpm will follow. Lastly, values such as the artist and the acousticness will have the least weight.


- What information does your `UserProfile` store

favorite_genre, favorite_mood, target_energy, likes_acoustic

- How does your `Recommender` compute a score for each song

The recommendor uses the features detected from the songs and compares them to the user's preferences to calculate a score for each song. High weightages are assigned to factors such as genre that have a high impact on the user's preference.

- How do you choose which songs to recommend

The ones closest to the values that the user prefers in their favorite_genre, favorite_mood, target_energy, and likes_acoustic will be recommended. This is determined through the average of their 3 favorite songs.

You can include a simple diagram or bullet list if helpful.

---

## Example Output

The system successfully recommends songs based on user preferences. Here's an example output for a user who likes **pop** music with **happy** mood and **0.8 energy**:

```
Loading songs from ../data/songs.csv...
Loaded songs: 20

============================================================
MUSIC RECOMMENDATIONS
============================================================
User Profile: pop / happy / Energy: 0.8
============================================================

1. Sunrise City by Neon Echo
   Genre: pop | Mood: happy | Energy: 0.82
   Score: 7.46/10.0
   Reasons: genre match (+3.0), mood match (+2.5), energy similarity (+1.96)

2. Gym Hero by Max Pulse
   Genre: pop | Mood: intense | Energy: 0.93
   Score: 4.74/10.0
   Reasons: genre match (+3.0), energy similarity (+1.74)

3. Rooftop Lights by Indigo Parade
   Genre: indie pop | Mood: happy | Energy: 0.76
   Score: 4.42/10.0
   Reasons: mood match (+2.5), energy similarity (+1.92)

4. Night Drive Loop by Neon Echo
   Genre: synthwave | Mood: moody | Energy: 0.75
   Score: 1.90/10.0
   Reasons: energy similarity (+1.90)

5. Salsa Fuego by Los Ritmos
   Genre: latin | Mood: energetic | Energy: 0.86
   Score: 1.88/10.0
   Reasons: energy similarity (+1.88)

============================================================
```

**Analysis of Results:**
- **#1 Sunrise City** perfectly matches the profile (pop + happy + high energy)
- **#2 Gym Hero** matches genre preference but has intense mood instead of happy
- **#3 Rooftop Lights** matches mood preference but is indie pop instead of pop
- The system correctly prioritizes exact genre and mood matches while still considering energy similarity

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

