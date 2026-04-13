"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("../data/songs.csv") 

    # Define distinct user preference dictionaries for stress testing
    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.3},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
        
        # Adversarial/Edge Case Profiles
        "Conflicting Energy-Mood": {"genre": "pop", "mood": "sad", "energy": 0.9},  # High energy but sad mood
        "Nonexistent Genre": {"genre": "classical", "mood": "happy", "energy": 0.7},  # Genre not in dataset
        "Extreme Acoustic Lover": {"genre": "folk", "mood": "peaceful", "energy": 0.2, "likes_acoustic": True},
        "Anti-Acoustic": {"genre": "electronic", "mood": "euphoric", "energy": 0.8, "likes_acoustic": False},
        "Zero Energy": {"genre": "ambient", "mood": "relaxed", "energy": 0.0},  # Edge case: minimum energy
        "Max Energy": {"genre": "metal", "mood": "angry", "energy": 1.0},  # Edge case: maximum energy
        "Genre Mood Mismatch": {"genre": "metal", "mood": "peaceful", "energy": 0.5}  # Unlikely combination
    }

    # Test each profile
    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=3)
        
        print("\n" + "="*60)
        print(f"MUSIC RECOMMENDATIONS - {profile_name}")
        print("="*60)
        # Build profile description dynamically
        profile_desc = f"{user_prefs['genre']} / {user_prefs['mood']} / Energy: {user_prefs['energy']}"
        if 'likes_acoustic' in user_prefs:
            profile_desc += f" / Acoustic: {user_prefs['likes_acoustic']}"
        print(f"User Profile: {profile_desc}")
        print("="*60)
        
        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"\n{i}. {song['title']} by {song['artist']}")
            print(f"   Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']:.2f}")
            print(f"   Score: {score:.2f}/10.0")
            print(f"   Reasons: {explanation}")
        
        print("\n" + "="*60)

    

if __name__ == "__main__":
    main()
