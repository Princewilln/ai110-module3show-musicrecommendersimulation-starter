# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One weakness I noticed is that the recommender can become too focused on a single signal when the scoring weights are changed. In my experiment, making energy matter more caused songs that were close to the target energy to rise quickly even when they did not match the user’s genre or mood as well. That means the system can accidentally create a filter bubble by favoring a narrow type of song and making the recommendations feel less diverse. It also does not capture deeper musical taste, such as artist identity, lyrics, or personal history, so it may miss what a real listener would actually enjoy.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested several very different user profiles to see whether the recommender would respond in a way that made sense. The first profile was a high-energy pop listener, and the top results were songs that matched both the preferred genre and mood. That felt reasonable, although I was a little surprised that Gym Hero kept appearing in some of the results for people who were not explicitly looking for intense pop. It made me realize the system is still picking up energy strongly, even when the user description is more about mood than force.

The chill lo-fi profile produced a very different set of recommendations. Songs with lower energy and more acoustic qualities rose to the top, which made sense because that profile was asking for a calmer, quieter mood. The deep intense rock profile also behaved in a clear way: it preferred songs with high energy and a more forceful tone, so the recommendations shifted toward songs that felt more aggressive and dramatic.

The adversarial profile was the most interesting one. I gave the system a user who wanted rock but also had a sad mood, which is a confusing combination in real life. The results still picked songs that matched the rock genre and energy, but the mood mismatch did not stop them from ranking highly. That told me the system is more comfortable following the visible features in the data than it is handling contradictory tastes.

I also ran a small experiment by changing the weights so energy mattered more and genre mattered less. That changed the rankings noticeably, and it helped me see that the system is quite sensitive to its scoring rules. In plain terms, it is not just saying “this person likes pop” or “this person likes rock”; it is also strongly reacting to how close a song is to the target energy level.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
