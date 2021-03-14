#### IMPORT ####

import json

from corpus_tfidf import tf_idf_compute

from title_detection import identify_title, read_result

#### CODE ####

filmAsked = input('Rentrez le film désiré ci-après : ')

filmTitles, filmIndexes = identify_title(filmAsked)

print ('-------------------------')
print('Le film choisi est-il l\'un des trois ci-dessous ?')
print(filmTitles)
inList = input('Si oui, indiquez son numéro dans la liste, si non écrivez "ERREUR" : ')

numFilm = filmIndexes[int(inList) - 1]

''''''

with open("corpus_questions2.json", "r", encoding="utf-8") as file:
    json_file = json.loads(file.read())
    
content = json_file['intents']

corpus_temp = []
corpus = []
for i in range(len(content)):
    corpus_temp.append(content[i]['examples'])
    for j in range(len(corpus_temp[i])):
        corpus.append(corpus_temp[i][j])

questionAsked = input('quelle est votre question ? :')
corpus.append(questionAsked)

''''''

index, cos_similarity = tf_idf_compute(corpus)

''''''

intent = -1
count = 0

while (count < index):
    intent += 1
    count += len(content[intent]['examples'])
    
nameClass = content[intent]['intent']

''''''

result = read_result(numFilm, nameClass)

print(result)
