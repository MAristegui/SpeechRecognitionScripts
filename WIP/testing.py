import csv
from googletrans import Translator
import sys

print("\014")
translator = Translator()
language_dictionary = {
					'Español':'es',
					'Frances':'fr',
					'Aleman':'de',
					'Italiano':'it',
					'Portugués':'pt',
					'Turco':'tr'}

def getTranslations(word):
    words = []
    for language in language_dictionary.values():
        translate_word = translator.translate(word,dest=language)
        words.append(translate_word.text.lower())
    return words
header = ['English','Spanish','French','German','Italian','Portuguese','Turkish','Positive', 'Negative', 'Anger', 'Anticipation', 'Disgust', 'Fear', 'Joy', 'Sadness', 'Surprise', 'Trust']

with open('nrc_emotion_lexicon.csv' , 'r') as csvfile:
    with open('Lexicon.csv','a',encoding="UTF-32",newline='') as f:
        csv_file_reader = csv.reader(csvfile,delimiter=',')
        #next(csv_file_reader,None)
        writer = csv.writer(f)
        #writer.writerow(header)
        word = ''
        for row in csv_file_reader:
            row = row[0].split(';')
            if '1' in row:
                word = getTranslations(row[0])
                to_write =[row[0]] + word + row[1::]         
                writer.writerow(to_write)
                print(row[0])
            
