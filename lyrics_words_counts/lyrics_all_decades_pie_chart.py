import pandas as pd
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('fivethirtyeight')

decades = ["1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s"]
lyrics = " "
for decade in decades:
    file = pd.read_csv('{}_lyrics.csv'.format(decade),encoding ='latin1')
    lyric = file["Lyrics"]
    for i in lyric:
        lyrics += str(i)

all_words = lyrics.lower().split()
all_words_clean = []
for word in all_words:
    word = word.replace(",", "")
    word = word.replace("'", "")
    word = word.replace("(", "")
    word = word.replace(")", "")
    word = word.replace("'s", "")
    word = word.replace("'d", "")
    word = word.replace("'ll", "")
    word = word.replace("s'", "s")
    all_words_clean.append(word)


stop_words = set(stopwords.words('english'))
stop_words_add = ["like", "get", "im", "oh", "dont", "know", "yeah", "baby", "youre", "got",\
                  "cause", "one", "never", "want", "go", "cant", "come", "gonna", "na", "right",\
                  "make", "way", "feel", "ever", "let", "hey", "thats", "need", "ive", "wanna",\
                  "put", "aint", "ya", "could", "lets", "feeling", "still", "la", "see",\
                  "say", "back", "take", "look", "tell", "well", "getting", "things",\
                  "really", "think", "turn", "wont", "ooh", "keep", "long", "em", "shes", "said", "nananana",\
                  "much", "youll", "whoa", "hold", "uh-huh", "ah", "around", "theres", "da", "us",\
                  "every", "another", "give", "would", "always", "ba", "mmm...", "watch", "gotta", "dat",\
                  "dum", "doo", "bop", "boom", "dooby"]
stop_words |= set(stop_words_add)
clean_words = [w for w in all_words_clean if not w in stop_words]
freq_clean = nltk.FreqDist(clean_words)
top10_words = freq_clean.most_common(15)

df = pd.DataFrame(top10_words)
df.columns = ["word", "count"]
print(df.word)
plt.axis('equal')
df["count"].plot(kind='pie', autopct='%1.1f%%', fontsize = 18, labels=df['word'], title="Top 15 Words of Most Popular Songs' Lyrics from the 1950s to 2010s")
plt.show()
