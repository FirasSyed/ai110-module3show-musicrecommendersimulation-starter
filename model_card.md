# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**  

---

## 2. Intended Use  

The system suggests songs based on user preferences for genre, mood, and energy level. It assumes users know what genres and moods they like. This is designed for classroom learning about recommendation algorithms, not for real music streaming services.  

---

## 3. How the Model Works  

The system looks at song features like genre, mood, energy, tempo, and acousticness. Users specify their preferred genre, mood, and energy level. The algorithm gives points for matching preferences: 3 points for genre match, 2.5 points for mood match, and up to 2 points for energy similarity. It also considers tempo, valence, danceability, and whether the user likes acoustic music. The total score is capped at 10 points.

---

## 4. Data  

The catalog contains 20 songs with features like genre, mood, energy, tempo, valence, danceability, and acousticness. Genres include pop, rock, lofi, jazz, electronic, and others. The dataset is small and limited - it only has 1-2 songs per genre and misses many popular genres like hip-hop, country, and classical.  

---

## 5. Strengths  

The system works well for users with clear genre preferences like pop, rock, or lofi. It correctly identifies when songs match multiple preferences (genre + mood + energy). The acoustic preference feature works as expected, rewarding users who like acoustic or non-acoustic music.  

---

## 6. Limitations and Bias 

Where does system struggle or behave unfairly. 

The system over-prioritizes genre matches because 60% of the dataset contains pop/rock variants, creating filter bubbles for users with niche preferences like classical or blues.  

---

## 7. Evaluation  

I tested 10 different user profiles including normal preferences and edge cases. I looked at whether the system gave reasonable recommendations and tested conflicting preferences like high energy with sad mood. The biggest surprise was how genre matches dominated all other factors, creating bias toward mainstream genres.

---

## 8. Future Work  

I would add related genre matching (classical users get jazz recommendations), reduce genre weight from 3 to 2.5 points, and add more diverse songs to the dataset. I also want to improve the energy scoring to handle impossible combinations better.  

---

## 9. Personal Reflection  

My biggest learning moment was realizing how simple scoring can create filter bubbles. AI tools helped me write code quickly but I had to double-check the scoring logic manually. It surprised me that even basic algorithms can "feel" like real recommendations when they match genre and energy well. If I extended this project, I would add collaborative filtering and more diverse music genres.  
