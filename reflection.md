# Music Recommender Reflection

## Profile Comparisons and Analysis

### High-Energy Pop vs Chill Lofi
The EDM profile consistently got perfect matches because pop is heavily represented in dataset. The lofi profile also performed well, showing that system works well when genres match. This demonstrates that users with clear genre preferences get strong recommendations regardless of energy level differences.

### Deep Intense Rock vs Conflicting Energy-Mood
The intense rock profile got perfect results. The conflicting profile struggled, recommending different songs instead. This reveals how the system prioritizes genre matches so strongly that it ignores mood conflicts, showing that genre preference outweighs mood compatibility in the scoring algorithm.

### Nonexistent Genre Impact
The classical user profile was most telling - zero genre matches forced the system to rely solely on mood and energy. This shows how users with niche genres get penalized. This demonstrates the dataset bias: 60% of songs are pop/rock variants, so classical users get second-best recommendations.

### Acoustic Preference Logic
The acoustic lover profile worked perfectly while the anti-acoustic user got good recommendations. Both got good recommendations, but the scoring correctly rewarded acoustic vs non-acoustic preferences. This shows the binary acoustic preference works as intended.

### Energy Scoring Behavior
The zero energy and max energy profiles revealed that the linear energy formula works but doesn't account for musical context. Users requesting "relaxed" music with 0.0 energy still got recommendations, but they were all high-energy songs that just happened to have lower energy scores. The system doesn't penalize logically impossible combinations, showing that the algorithm treats energy as a simple numerical difference rather than considering musical coherence.

## What This Means
The stress testing showed that the recommender is technically solid but has clear biases toward mainstream genres and doesn't handle conflicting preferences well. The scoring logic works as programmed, but the weights create predictable patterns that might not match how humans actually think about music recommendations.
