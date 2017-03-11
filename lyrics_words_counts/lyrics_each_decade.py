import pandas as pd
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

decades = ["1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s"]
for decade in decades:
    file = pd.read_csv('{}_lyrics.csv'.format(decade),encoding ='latin1')
    lyric = file["Lyrics"]
    lyrics = " "
    for i in lyric:
        lyrics += str(i)

    all_words = lyrics.lower().split()
    #all_words.replace("'","")
    all_words_clean = []
    for word in all_words:
        word = word.replace(",","")
        word = word.replace("'", "")
        word = word.replace("(", "")
        word = word.replace(")", "")
        word = word.replace("'s", "")
        word = word.replace("'d", "")
        word = word.replace("'ll", "")
        word = word.replace("s'", "s")
        all_words_clean.append(word)

    print("{}: ".format(decade), len(all_words_clean))
    #freq = nltk.FreqDist(all_words_clean)
    #print(freq.most_common(30))

    stop_words = set(stopwords.words('english'))
    stop_words_add = ["like", "get", "im", "oh", "dont", "know", "yeah", "baby", "youre", "got",\
                      "cause", "one", "never", "want", "go", "cant", "come", "gonna", "na", "right",\
                      "make", "way", "feel", "ever", "let", "hey", "thats", "need", "ive", "wanna",\
                      "put", "aint", "ya", "could", "lets", "feeling", "still", "la", "see",\
                      "say", "back", "take", "look", "tell", "well", "getting", "things",\
                      "really", "think", "turn", "wont", "ooh", "keep", "long", "em", "shes", "said", "nananana",\
                      "much", "youll", "whoa", "hold", "uh-huh", "ah", "around", "theres", "da", "us",\
                      "every", "another", "give", "would", "always", "ba", "mmm...", "watch", "gotta", "dat",\
                      "dum", "doo", "bop", "boom", "bum", "dooby"]
    stop_words |= set(stop_words_add)
    clean_words = [w for w in all_words_clean if not w in stop_words]
    freq_clean = nltk.FreqDist(clean_words)
    top15_words = freq_clean.most_common(15)
    #print(top15_words)

    df = pd.DataFrame(top15_words)
    df.columns = ["word", "count"]
    #print(df)
    colors = []
    top15_all = ["love", "ill", "girl", "time", "night", "heart", "good", "life", "day", "little",\
                 "dance", "tonight", "away", "stop", "world"]

    for word in df["word"]:
        if word in top15_all:
            colors.append("#00BEC5")
        else:
            colors.append("#FA8072")

    ax = df.plot(x="word", y="count", color=colors, width=0.8, kind="bar", legend=False, fontsize=25, rot=360)
    ax.set_xlabel("")
    plt.title("Top 15 Words of Most Popular Songs' Lyrics in the {} ".format(decade), fontsize=30)
    plt.show()

