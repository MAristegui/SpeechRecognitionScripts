import re
import sqlite3
import numpy as np

# Cleaning spyder console 
print("\014")

maxCharacters = 3
maxDecimals = 2

def cleanString(text):
    text = re.sub(pattern='[^a-z\s]',repl=' ',string=text).split(' ')
    text = [x for x in text if len(x)>maxCharacters]
    return text

def wordsLearning():
    # Pending
     return 0
    

def emotionPercentages(emotions):
    
    total = sum(emotions)
    toret = [0,0,0,0,0,0,0,0,0,0]
    
    if (total != 0):
        for x in range(len(emotions)):
            toret[x] = (emotions[x]*100)/total
    toret = np.round(toret,2)
    
    return toret
    
def getEmotions(cursor, comment):
    
    words = cleanString(comment.lower())
    
    emotions = [0,0,0,0,0,0,0,0,0,0]
    newWords = []
    
    for word in words:
        res = cursor.execute("SELECT * FROM EmotionLexicon WHERE WORD=?", (word,))
        rows = res.fetchall()
        print(rows)
        
        if (len(rows) == 0):
            newWords.append(word)
        else:
            for row in rows:
                emotions = np.add(emotions,row[1::])

    print(emotions)              
    return emotions
    
