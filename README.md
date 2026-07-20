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

### Implementation plan

The plan is to use the expanded catalog in [data/songs.csv](data/songs.csv) and a concrete example user profile with the following preferences:

- favorite genre: `pop`
- favorite mood: `happy`
- target energy: `0.80`
- likes acoustic: `False`

The recommender will read the CSV, evaluate every song one by one, and assign a score using the finalized algorithm recipe below.

### Finalized algorithm recipe

The recommendation rule is a simple weighted recipe built from the song catalog in [data/songs.csv](data/songs.csv):

- +2.0 points for a genre match
- +1.0 point for a mood match
- +1.0 point scaled by energy similarity, where a perfect energy match earns the full point and a larger gap earns less
- smaller bonus points for valence and acousticness to keep the system interpretable

This recipe gives genre a stronger influence than mood, while still letting the energy profile steer results when two songs share the same genre and mood. In practice, a song that matches the user’s favorite genre and mood and also sits near the target energy will rise to the top of the ranking.

### Expected biases

This system may over-prioritize genre, which could cause it to miss some strong songs that match the user’s mood or energy very well but use a different genre. It also relies on a small handcrafted feature set, so it will not understand deeper musical context such as lyrics, artist identity, or listening history.

### Visualizing the data flow

A quick Mermaid flowchart showing how one song moves from the CSV into the ranked recommendation list is available in [docs/recommendation_flow.md](docs/recommendation_flow.md).

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

Here is a sample result from the current recommender for a user who likes pop, happy songs, and an energetic feel near 0.8:

```text
User profile: favorite_genre=pop, favorite_mood=happy, target_energy=0.80, likes_acoustic=False

Top recommendations:
1. Sunrise City - Score: 4.46
   Because: matched preferred genre; matched preferred mood; energy close to target 0.80; valence aligned with mood; acousticness was not overly bright

2. Gym Hero - Score: 3.33
   Because: matched preferred genre; mood did not match; energy close to target 0.80; valence aligned with mood; acousticness was not overly bright

3. Rooftop Lights - Score: 2.42
   Because: genre did not match; matched preferred mood; energy close to target 0.80; valence aligned with mood; acousticness was not overly bright
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



