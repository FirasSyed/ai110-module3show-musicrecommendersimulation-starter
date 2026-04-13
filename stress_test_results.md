# Music Recommender Stress Test Results

## Profile 1: High-Energy Pop
**User Profile:** pop / happy / Energy: 0.9

[SCREENSHOT SPACE - Take screenshot of results below]

```bash
cd src && python3 -c "
from recommender import load_songs, recommend_songs
songs = load_songs('../data/songs.csv')
user_prefs = {'genre': 'pop', 'mood': 'happy', 'energy': 0.9}
recommendations = recommend_songs(user_prefs, songs, k=5)

print('============================================================')
print('MUSIC RECOMMENDATIONS - High-Energy Pop')
print('============================================================')
print(f'User Profile: {user_prefs[\"genre\"]} / {user_prefs[\"mood\"]} / Energy: {user_prefs[\"energy\"]}')
print('============================================================')

for i, rec in enumerate(recommendations, 1):
    song, score, explanation = rec
    print(f'\n{i}. {song[\"title\"]} by {song[\"artist\"]}')
    print(f'   Genre: {song[\"genre\"]} | Mood: {song[\"mood\"]} | Energy: {song[\"energy\"]:.2f}')
    print(f'   Score: {score:.2f}/10.0')
    print(f'   Reasons: {explanation}')

print('\n============================================================')
"
```

---

## Profile 2: Chill Lofi
**User Profile:** lofi / chill / Energy: 0.3

[SCREENSHOT SPACE - Take screenshot of results below]

```bash
cd src && python3 -c "
from recommender import load_songs, recommend_songs
songs = load_songs('../data/songs.csv')
user_prefs = {'genre': 'lofi', 'mood': 'chill', 'energy': 0.3}
recommendations = recommend_songs(user_prefs, songs, k=5)

print('============================================================')
print('MUSIC RECOMMENDATIONS - Chill Lofi')
print('============================================================')
print(f'User Profile: {user_prefs[\"genre\"]} / {user_prefs[\"mood\"]} / Energy: {user_prefs[\"energy\"]}')
print('============================================================')

for i, rec in enumerate(recommendations, 1):
    song, score, explanation = rec
    print(f'\n{i}. {song[\"title\"]} by {song[\"artist\"]}')
    print(f'   Genre: {song[\"genre\"]} | Mood: {song[\"mood\"]} | Energy: {song[\"energy\"]:.2f}')
    print(f'   Score: {score:.2f}/10.0')
    print(f'   Reasons: {explanation}')

print('\n============================================================')
"
```

---

## Profile 3: Deep Intense Rock
**User Profile:** rock / intense / Energy: 0.95

[SCREENSHOT SPACE - Take screenshot of results below]

```bash
cd src && python3 -c "
from recommender import load_songs, recommend_songs
songs = load_songs('../data/songs.csv')
user_prefs = {'genre': 'rock', 'mood': 'intense', 'energy': 0.95}
recommendations = recommend_songs(user_prefs, songs, k=5)

print('============================================================')
print('MUSIC RECOMMENDATIONS - Deep Intense Rock')
print('============================================================')
print(f'User Profile: {user_prefs[\"genre\"]} / {user_prefs[\"mood\"]} / Energy: {user_prefs[\"energy\"]}')
print('============================================================')

for i, rec in enumerate(recommendations, 1):
    song, score, explanation = rec
    print(f'\n{i}. {song[\"title\"]} by {song[\"artist\"]}')
    print(f'   Genre: {song[\"genre\"]} | Mood: {song[\"mood\"]} | Energy: {song[\"energy\"]:.2f}')
    print(f'   Score: {score:.2f}/10.0')
    print(f'   Reasons: {explanation}')

print('\n============================================================')
"
```

---

## Profile 4: Conflicting Energy-Mood
**User Profile:** pop / sad / Energy: 0.9

[SCREENSHOT SPACE - Take screenshot of results below]

```bash
cd src && python3 -c "
from recommender import load_songs, recommend_songs
songs = load_songs('../data/songs.csv')
user_prefs = {'genre': 'pop', 'mood': 'sad', 'energy': 0.9}
recommendations = recommend_songs(user_prefs, songs, k=5)

print('============================================================')
print('MUSIC RECOMMENDATIONS - Conflicting Energy-Mood')
print('============================================================')
print(f'User Profile: {user_prefs[\"genre\"]} / {user_prefs[\"mood\"]} / Energy: {user_prefs[\"energy\"]}')
print('============================================================')

for i, rec in enumerate(recommendations, 1):
    song, score, explanation = rec
    print(f'\n{i}. {song[\"title\"]} by {song[\"artist\"]}')
    print(f'   Genre: {song[\"genre\"]} | Mood: {song[\"mood\"]} | Energy: {song[\"energy\"]:.2f}')
    print(f'   Score: {score:.2f}/10.0')
    print(f'   Reasons: {explanation}')

print('\n============================================================')
"
```

---

## Profile 5: Nonexistent Genre
**User Profile:** classical / happy / Energy: 0.7

[SCREENSHOT SPACE - Take screenshot of results below]

```bash
cd src && python3 -c "
from recommender import load_songs, recommend_songs
songs = load_songs('../data/songs.csv')
user_prefs = {'genre': 'classical', 'mood': 'happy', 'energy': 0.7}
recommendations = recommend_songs(user_prefs, songs, k=5)

print('============================================================')
print('MUSIC RECOMMENDATIONS - Nonexistent Genre')
print('============================================================')
print(f'User Profile: {user_prefs[\"genre\"]} / {user_prefs[\"mood\"]} / Energy: {user_prefs[\"energy\"]}')
print('============================================================')

for i, rec in enumerate(recommendations, 1):
    song, score, explanation = rec
    print(f'\n{i}. {song[\"title\"]} by {song[\"artist\"]}')
    print(f'   Genre: {song[\"genre\"]} | Mood: {song[\"mood\"]} | Energy: {song[\"energy\"]:.2f}')
    print(f'   Score: {score:.2f}/10.0')
    print(f'   Reasons: {explanation}')

print('\n============================================================')
"
```

---

## Profile 6: Extreme Acoustic Lover
**User Profile:** folk / peaceful / Energy: 0.2 / Acoustic: True

[SCREENSHOT SPACE - Take screenshot of results below]

```bash
cd src && python3 -c "
from recommender import load_songs, recommend_songs
songs = load_songs('../data/songs.csv')
user_prefs = {'genre': 'folk', 'mood': 'peaceful', 'energy': 0.2, 'likes_acoustic': True}
recommendations = recommend_songs(user_prefs, songs, k=5)

print('============================================================')
print('MUSIC RECOMMENDATIONS - Extreme Acoustic Lover')
print('============================================================')
profile_desc = f'{user_prefs[\"genre\"]} / {user_prefs[\"mood\"]} / Energy: {user_prefs[\"energy\"]} / Acoustic: {user_prefs[\"likes_acoustic\"]}'
print(f'User Profile: {profile_desc}')
print('============================================================')

for i, rec in enumerate(recommendations, 1):
    song, score, explanation = rec
    print(f'\n{i}. {song[\"title\"]} by {song[\"artist\"]}')
    print(f'   Genre: {song[\"genre\"]} | Mood: {song[\"mood\"]} | Energy: {song[\"energy\"]:.2f}')
    print(f'   Score: {score:.2f}/10.0')
    print(f'   Reasons: {explanation}')

print('\n============================================================')
"
```

---

## Profile 7: Anti-Acoustic
**User Profile:** electronic / euphoric / Energy: 0.8 / Acoustic: False

[SCREENSHOT SPACE - Take screenshot of results below]

```bash
cd src && python3 -c "
from recommender import load_songs, recommend_songs
songs = load_songs('../data/songs.csv')
user_prefs = {'genre': 'electronic', 'mood': 'euphoric', 'energy': 0.8, 'likes_acoustic': False}
recommendations = recommend_songs(user_prefs, songs, k=5)

print('============================================================')
print('MUSIC RECOMMENDATIONS - Anti-Acoustic')
print('============================================================')
profile_desc = f'{user_prefs[\"genre\"]} / {user_prefs[\"mood\"]} / Energy: {user_prefs[\"energy\"]} / Acoustic: {user_prefs[\"likes_acoustic\"]}'
print(f'User Profile: {profile_desc}')
print('============================================================')

for i, rec in enumerate(recommendations, 1):
    song, score, explanation = rec
    print(f'\n{i}. {song[\"title\"]} by {song[\"artist\"]}')
    print(f'   Genre: {song[\"genre\"]} | Mood: {song[\"mood\"]} | Energy: {song[\"energy\"]:.2f}')
    print(f'   Score: {score:.2f}/10.0')
    print(f'   Reasons: {explanation}')

print('\n============================================================')
"
```

---

## Profile 8: Zero Energy
**User Profile:** ambient / relaxed / Energy: 0.0

[SCREENSHOT SPACE - Take screenshot of results below]

```bash
cd src && python3 -c "
from recommender import load_songs, recommend_songs
songs = load_songs('../data/songs.csv')
user_prefs = {'genre': 'ambient', 'mood': 'relaxed', 'energy': 0.0}
recommendations = recommend_songs(user_prefs, songs, k=5)

print('============================================================')
print('MUSIC RECOMMENDATIONS - Zero Energy')
print('============================================================')
print(f'User Profile: {user_prefs[\"genre\"]} / {user_prefs[\"mood\"]} / Energy: {user_prefs[\"energy\"]}')
print('============================================================')

for i, rec in enumerate(recommendations, 1):
    song, score, explanation = rec
    print(f'\n{i}. {song[\"title\"]} by {song[\"artist\"]}')
    print(f'   Genre: {song[\"genre\"]} | Mood: {song[\"mood\"]} | Energy: {song[\"energy\"]:.2f}')
    print(f'   Score: {score:.2f}/10.0')
    print(f'   Reasons: {explanation}')

print('\n============================================================')
"
```

---

## Profile 9: Max Energy
**User Profile:** metal / angry / Energy: 1.0

[SCREENSHOT SPACE - Take screenshot of results below]

```bash
cd src && python3 -c "
from recommender import load_songs, recommend_songs
songs = load_songs('../data/songs.csv')
user_prefs = {'genre': 'metal', 'mood': 'angry', 'energy': 1.0}
recommendations = recommend_songs(user_prefs, songs, k=5)

print('============================================================')
print('MUSIC RECOMMENDATIONS - Max Energy')
print('============================================================')
print(f'User Profile: {user_prefs[\"genre\"]} / {user_prefs[\"mood\"]} / Energy: {user_prefs[\"energy\"]}')
print('============================================================')

for i, rec in enumerate(recommendations, 1):
    song, score, explanation = rec
    print(f'\n{i}. {song[\"title\"]} by {song[\"artist\"]}')
    print(f'   Genre: {song[\"genre\"]} | Mood: {song[\"mood\"]} | Energy: {song[\"energy\"]:.2f}')
    print(f'   Score: {score:.2f}/10.0')
    print(f'   Reasons: {explanation}')

print('\n============================================================')
"
```

---

## Profile 10: Genre Mood Mismatch
**User Profile:** metal / peaceful / Energy: 0.5

[SCREENSHOT SPACE - Take screenshot of results below]

```bash
cd src && python3 -c "
from recommender import load_songs, recommend_songs
songs = load_songs('../data/songs.csv')
user_prefs = {'genre': 'metal', 'mood': 'peaceful', 'energy': 0.5}
recommendations = recommend_songs(user_prefs, songs, k=5)

print('============================================================')
print('MUSIC RECOMMENDATIONS - Genre Mood Mismatch')
print('============================================================')
print(f'User Profile: {user_prefs[\"genre\"]} / {user_prefs[\"mood\"]} / Energy: {user_prefs[\"energy\"]}')
print('============================================================')

for i, rec in enumerate(recommendations, 1):
    song, score, explanation = rec
    print(f'\n{i}. {song[\"title\"]} by {song[\"artist\"]}')
    print(f'   Genre: {song[\"genre\"]} | Mood: {song[\"mood\"]} | Energy: {song[\"energy\"]:.2f}')
    print(f'   Score: {score:.2f}/10.0')
    print(f'   Reasons: {explanation}')

print('\n============================================================')
"
```
