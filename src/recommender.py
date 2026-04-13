from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

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
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    songs = []
    
    with open(csv_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numerical values to proper types for math operations
            song_dict = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness'])
            }
            songs.append(song_dict)
    
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences using weighted algorithm."""
    
    # Algorithm Recipe:
    # - Genre Match: +3.0 points (exact), +1.5 points (related genre)
    # - Mood Match: +2.5 points (exact), +1.2 points (related mood)
    # - Energy Similarity: +2.0 points max, calculated as 2.0 * (1 - |energy - target_energy|)
    # - Tempo Similarity: +1.5 points max, calculated as 1.5 * (1 - |tempo - target_tempo| / 120)
    # - Valence Similarity: +1.5 points max, calculated as 1.5 * (1 - |valence - target_valence|)
    # - Danceability Similarity: +1.0 point max, calculated as 1.0 * (1 - |danceability - target_danceability|)
    # - Artist Similarity: +0.5 points (if artist matches user's favorites)
    # - Acousticness Preference: +0.5 points (if matches user's likes_acoustic preference)
    # - Apply 10.0 point cap
    score = 0.0
    reasons = []
    
    # Genre matching
    if song['genre'].lower() == user_prefs.get('genre', '').lower():
        score += 3.0
        reasons.append(f"genre match (+3.0)")
    
    # Mood matching
    if song['mood'].lower() == user_prefs.get('mood', '').lower():
        score += 2.5
        reasons.append(f"mood match (+2.5)")
    
    # Energy similarity
    if 'energy' in user_prefs:
        energy_diff = abs(song['energy'] - user_prefs['energy'])
        energy_score = 2.0 * (1 - energy_diff)
        score += energy_score
        reasons.append(f"energy similarity (+{energy_score:.2f})")
    
    # Tempo similarity
    if 'tempo' in user_prefs:
        tempo_diff = abs(song['tempo_bpm'] - user_prefs['tempo'])
        tempo_score = 1.5 * (1 - tempo_diff / 120)
        score += tempo_score
        reasons.append(f"tempo similarity (+{tempo_score:.2f})")
    
    # Valence similarity
    if 'valence' in user_prefs:
        valence_diff = abs(song['valence'] - user_prefs['valence'])
        valence_score = 1.5 * (1 - valence_diff)
        score += valence_score
        reasons.append(f"valence similarity (+{valence_score:.2f})")
    
    # Danceability similarity
    if 'danceability' in user_prefs:
        dance_diff = abs(song['danceability'] - user_prefs['danceability'])
        dance_score = 1.0 * (1 - dance_diff)
        score += dance_score
        reasons.append(f"danceability similarity (+{dance_score:.2f})")
    
    # Artist similarity
    if 'favorite_artists' in user_prefs and song['artist'] in user_prefs['favorite_artists']:
        score += 0.5
        reasons.append("artist match (+0.5)")
    
    # Acousticness preference
    if 'likes_acoustic' in user_prefs:
        if user_prefs['likes_acoustic'] and song['acousticness'] > 0.5:
            score += 0.5
            reasons.append("acoustic preference match (+0.5)")
        elif not user_prefs['likes_acoustic'] and song['acousticness'] <= 0.5:
            score += 0.5
            reasons.append("non-acoustic preference match (+0.5)")
    
    # Apply 10.0 point cap
    if score > 10.0:
        score = 10.0
        reasons.append("score capped at 10.0")
    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Recommend top k songs based on user preferences using scoring algorithm."""
    
    # Uses score_song to evaluate all songs and returns top k recommendations.
    # Expected return format: (song_dict, score, explanation)
    # Score all songs using score_song function
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))
    
    # Sort songs by score in descending order using sorted()
    # sorted() returns a new list, leaving original data unchanged
    sorted_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)
    
    # Return top k recommendations
    return sorted_songs[:k]
