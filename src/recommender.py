import csv
from typing import List, Dict, Tuple, Any
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """

    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        ranked = []
        for song in self.songs:
            score, _ = score_song(_profile_to_dict(user), _song_to_dict(song))
            ranked.append((song, score))
        ranked.sort(key=lambda item: item[1], reverse=True)
        return [song for song, _ in ranked[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = score_song(_profile_to_dict(user), _song_to_dict(song))
        return "; ".join(reasons) if reasons else "No strong matching signals."


def load_songs(csv_path: str) -> List[Dict[str, Any]]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict[str, Any]] = []
    with open(csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    print(f"Loading songs from {csv_path}...")
    return songs


def score_song(
    user_prefs: Dict[str, Any], song: Dict[str, Any]
) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    prefs = _coerce_user_prefs(user_prefs)
    song_data = _coerce_song(song)

    score = 0.0
    reasons: List[str] = []

    if prefs.get("favorite_genre") and song_data.get("genre"):
        if song_data["genre"].lower() == prefs["favorite_genre"].lower():
            score += 2.0
            reasons.append("matched preferred genre")
        else:
            reasons.append("genre did not match")

    if prefs.get("favorite_mood") and song_data.get("mood"):
        if song_data["mood"].lower() == prefs["favorite_mood"].lower():
            score += 1.0
            reasons.append("matched preferred mood")
        else:
            reasons.append("mood did not match")

    target_energy = float(prefs.get("target_energy", 0.5))
    if song_data.get("energy") is not None:
        energy_similarity = max(
            0.0, 1.0 - abs(float(song_data["energy"]) - target_energy)
        )
        score += 1.0 * energy_similarity
        reasons.append(f"energy close to target {target_energy:.2f}")

    mood_target_valence = _valence_target_for_mood(prefs.get("favorite_mood"))
    if song_data.get("valence") is not None:
        valence_similarity = 1.0 - abs(
            float(song_data["valence"]) - mood_target_valence
        )
        score += 0.25 * valence_similarity
        reasons.append("valence aligned with mood")

    if (
        prefs.get("likes_acoustic") is True
        and song_data.get("acousticness") is not None
    ):
        acoustic_target = 0.8
        acoustic_similarity = 1.0 - abs(
            float(song_data["acousticness"]) - acoustic_target
        )
        score += 0.25 * acoustic_similarity
        reasons.append("acousticness matched the user's preference")
    elif (
        prefs.get("likes_acoustic") is False
        and song_data.get("acousticness") is not None
    ):
        acoustic_target = 0.2
        acoustic_similarity = 1.0 - abs(
            float(song_data["acousticness"]) - acoustic_target
        )
        score += 0.25 * acoustic_similarity
        reasons.append("acousticness was not overly bright")

    return round(score, 4), reasons


def recommend_songs(
    user_prefs: Dict[str, Any], songs: List[Dict[str, Any]], k: int = 5
) -> List[Tuple[Dict[str, Any], float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored.append((song, score, explanation))
    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]


def _profile_to_dict(user: UserProfile) -> Dict[str, Any]:
    return {
        "favorite_genre": user.favorite_genre,
        "favorite_mood": user.favorite_mood,
        "target_energy": user.target_energy,
        "likes_acoustic": user.likes_acoustic,
    }


def _song_to_dict(song: Song) -> Dict[str, Any]:
    return {
        "id": song.id,
        "title": song.title,
        "artist": song.artist,
        "genre": song.genre,
        "mood": song.mood,
        "energy": song.energy,
        "tempo_bpm": song.tempo_bpm,
        "valence": song.valence,
        "danceability": song.danceability,
        "acousticness": song.acousticness,
    }


def _coerce_user_prefs(user_prefs: Any) -> Dict[str, Any]:
    if isinstance(user_prefs, UserProfile):
        return _profile_to_dict(user_prefs)
    if isinstance(user_prefs, dict):
        return user_prefs
    return {}


def _coerce_song(song: Any) -> Dict[str, Any]:
    if isinstance(song, Song):
        return _song_to_dict(song)
    if isinstance(song, dict):
        return song
    return {}


def _valence_target_for_mood(mood: Any) -> float:
    if not mood:
        return 0.6
    normalized = str(mood).lower()
    mood_targets = {
        "happy": 0.8,
        "chill": 0.6,
        "intense": 0.4,
        "relaxed": 0.7,
        "focused": 0.55,
        "moody": 0.45,
    }
    return mood_targets.get(normalized, 0.6)
