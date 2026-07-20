# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project builds a small music recommender that simulates how a streaming service might connect a user’s taste profile to songs in a catalog. The system uses a simple content-based approach: it looks at song features like genre, mood, energy, and acousticness, compares them to a user’s preferences, and ranks songs by how well they match.

---

## How The System Works

Real recommendation systems usually combine many signals, such as what a user has listened to, what similar users enjoy, and what the content itself looks like. In this simulation, I focus on the content-based side: the recommender compares a user’s taste profile to the attributes of each song and tries to find songs that feel like the right fit. The system prioritizes clear, interpretable features such as genre, mood, energy, valence, and acousticness, because those are easy to connect to a user’s stated preferences and to a listener’s idea of a song’s "vibe".

### Features used in the simulation

- `Song` features:
  - `genre`
  - `mood`
  - `energy`
  - `tempo_bpm`
  - `valence`
  - `danceability`
  - `acousticness`

- `UserProfile` features:
  - `favorite_genre`
  - `favorite_mood`
  - `target_energy`
  - `likes_acoustic`

The recommender scores each song by rewarding strong matches for categorical preferences like genre and mood, and by rewarding numerical closeness for values such as energy and valence. Songs are then ranked from highest to lowest score and returned as recommendations.

### Step 3: Recommendation algorithm recipe

The recommendation rule is a simple weighted recipe built from the song catalog in [data/songs.csv](data/songs.csv):

- +2.0 points for a genre match
- +1.0 point for a mood match
- +1.0 point scaled by energy similarity, where a perfect energy match earns the full point and a larger gap earns less
- smaller bonus points for valence and acousticness to keep the system interpretable

This recipe gives genre a stronger influence than mood, while still letting the energy profile steer results when two songs share the same genre and mood. In practice, a song that matches the user’s favorite genre and mood and also sits near the target energy will rise to the top of the ranking.

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

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

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



