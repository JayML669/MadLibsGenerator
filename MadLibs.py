import csv
import json
import random
import re

with open('myMad.json', encoding = 'utf-8') as file:
    templates = json.load(file)

with open('simplemaps-worldcities-basic.csv', encoding = 'utf-8') as file:
    reader = csv.reader(file)
    cities = [row[1] for row in reader]

with open('music.csv') as file:
    reader = csv.reader(file)
    songTitles = [row[21] for row in reader]

with open('CSV_Database_of_First_Names.csv') as file:
    reader = csv.reader(file)

    namesHeader = next(reader)

    names = [row[0] for row in reader]

with open('dictionary.csv')  as file:
    reader = csv.reader(file)

    header = next(reader)

    data = [row for row in reader]

vi = [row[0] for row in data if row[1] == 'v. i.']
vt =[row[0] for row in data if row[1] == 'v. t.']
noun = [row[0] for row in data if row[1] == 'n.']
adj = [row[0] for row in data if row[1] == 'a.']



class MadLib:
    '''A MadLib Object With Nouns Verbs And Adjs and Names'''
    def __init__(self, vi, vt, noun, adj, names, places, songs):
        self.verbs = vi
        self.verbs.append(vt)
        self.nouns = noun
        self.adjs = adj
        self.names = names
        self.cities = places
        self.songs = songs

    def constructMadLib(self):
        '''Create The MadLib'''

        usableTemplate = templates[random.choice(list(templates.keys()))]['Copy']
        empties = re.findall(r'\[.+?\]', usableTemplate)
        print(empties)

        tempEmpties = empties

        same = (False, None)

        for i in range(len(empties)):
            for j in range(i):
                if empties[i] == tempEmpties[j]:
                    same = (True, j)
                else:
                    same = (False, None)
            if same[0] == True:
                empties[i] = tempEmpties[same[1]]
            else:
                if 'Name' in empties[i] and 'Place' not in empties[i] and 'Song' not in empties[i]:
                    empties[i] = random.choice(self.names)

                elif 'Place' in empties[i]:
                    empties[i] = random.choice(self.cities)

                elif 'Song' in empties[i]:
                    empties[i] = random.choice(self.songs)

                elif 'Noun' in empties[i] or 'Clothing' in empties[i]:
                    if 'Plural' in empties[i]:
                        empties[i] = random.choice(self.nouns) + 's'
                    else:
                        empties[i] = random.choice(self.nouns)

                elif ('Action' or 'Verb') in empties[i]:
                    if '-ing' in empties[i]:
                        empties[i] = random.choice(self.verbs) + 'ing'
                    else:
                        empties[i] = random.choice(self.verbs)

                elif 'Describing' in empties[i]:
                    empties[i] = random.choice(self.adjs)

                elif 'Number' in empties[i]:
                    empties[i] = str(random.randint(0, 1000))

        print(empties)


testMadLib = MadLib(vi, vt, noun, adj, names, cities, songTitles)

testMadLib.constructMadLib()
