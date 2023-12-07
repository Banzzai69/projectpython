import os

# #lecture du fichier FIFA-2022.txt

def load_data(FileName):
  with open(FileName, "r") as load:
     print(load.read())

#Enleve l'entete 
     
  with open("FIFA_World_Cup/FIFA-2022.txt") as noheader:
      lines = noheader.readlines()[1:]
      
  for lignes in lines:
      lignes = lignes.strip()
      print(lignes)
         
import pandas as datas

datas = [
"1,Argentina,7,6,0,1,15,8,7,18",
"2,France,7,5,0,2,16,8,8,15",
"3,Croatia,7,4,2,1,8,7,1,14",
"4,Morocco,7,4,1,2,6,5,1,13",
"5,England,5,3,1,1,13,4,9,10",
"6,Netherlands,5,3,1,1,10,4,6,10",
"7,Portugal,5,3,0,2,12,6,6,9",
"8,Brazil,5,3,0,2,8,3,5,9",
"9,Japan,4,2,0,2,5,4,1,6",
"10,Senegal,4,2,0,2,5,7,-2,6",
"11,Australia,4,2,0,2,4,6,-2,6",
"12,Switzerland,4,2,0,2,5,9,-4,6",
"13,USA,4,1,2,1,3,4,-1,5",
"14,Spain,4,1,1,2,9,3,6,4",
"15,Poland,4,1,1,2,3,5,-2,4",
"16,South Korea,4,1,1,2,5,8,-3,4",
"17,Germany,3,1,1,1,6,5,1,4",
"18,Ecuador,3,1,1,1,4,3,1,4",
"19,Cameroon,3,1,1,1,4,4,0,4",
"20,Uruguay,3,1,1,1,2,2,0,4",
"21,Tunisia,3,1,1,1,1,1,0,4",
"22,Mexico,3,1,1,1,2,3,-1,4",
"23,Belgium,3,1,1,1,1,2,-1,4",
"24,Ghana,3,1,0,2,5,7,-2,3",
"25,Saudi Arabia,3,1,0,2,3,5,-2,3",
"26,Iran,3,1,0,2,4,7,-3,3",
"27,Costa Rica,3,1,0,2,3,11,-8,3",
"28,Denmark,3,0,1,2,1,3,-2,1",
"29,Serbia,3,0,1,2,5,8,-3,1",
"30,Wales,3,0,1,2,1,6,-5,1",
"31,Canada,3,0,0,3,2,7,-5,0",
"32,Qatar,3,0,0,3,1,7,-6,0",
]

nom_pays = []

for ligne in datas:
    colonnes = ligne.split(',')
    nom_pays.append(colonnes[1])


#Afficher les noms des equipes en 3 lettres

nom_equipe_triee= sorted(nom_pays)
for nom in nom_pays:
    trois_premieres_lettres = nom[:3]
    print (trois_premieres_lettres)

#Enregistrer fichiers avec modifications
filename = "FIFA_World_Cup/FIFA-2022_Trie.txt"

with open(filename, mode='w') as file:
    for equipe in nom_pays:
        file.write(equipe + '\n')

print(f"Données triées enregistrées avec succès dans {filename}")
#melanger les données
import random

nouveau_classement = datas[:]

random.shuffle(nouveau_classement)
print('\n'.join(nouveau_classement))

chemin = "new_class.txt"
with open(chemin, mode = "w") as mon_fichier:
  mon_fichier.write("new_class"+'\n')
  mon_fichier.writelines(repr(nouveau_classement))

#Nombre de points pour chaque equipe

nombre_point = {}

for ligne in datas:
    colonnes = ligne.split(',')
    nom_pays = colonnes[1]
    victoires = int(colonnes[3])
    match_nuls = int(colonnes[4])

    points = 3 * victoires + 1 * match_nuls
    nombre_point[nom_pays] = points

for nom_pays, points in nombre_point.items():
    
    print(f"{nom_pays}: {points} point(s)")
 
#Calculer la difference de but
nombre_buts = {}

for ligne in datas:
    colonnes = ligne.split(',')
    nom_pays = colonnes[1]
    goals_for = int(colonnes[7])
    goals_against = int(colonnes[8])

    buts = goals_for - goals_against
    nombre_buts[nom_pays] = buts 

for nom_pays, buts in nombre_buts.items():
    print(f"{nom_pays}: {buts} but(s)")

#supprimer une colonne

import pandas as deleted_column

df = deleted_column.DataFrame(datas)
df.drop(df.iloc[:, 1:3], inplace=True, axis=1)

#  Trie les equipes par nom

filename="FIFA_World_Cup/FIFA-2022_abregee_Trie.txt"

filename="equipes_triees.txt"
for ligne in datas:
    colonnes = ligne.split(',')
    nom_equipe_triee.append(colonnes[1])

for nom in nom_equipe_triee:
    trois_premieres_lettress = nom[:3]
    print (trois_premieres_lettress)
   
#trie les equipes avec leur classement

import pandas as pd

data = [
    [1, 'Argentina', 7, 6, 0, 1, 15, 8, 7, 18],
    [2, 'France', 7, 5, 0, 2, 16, 8, 8, 15],
    [3, 'Croatia', 7, 4, 2, 1, 8, 7, 1, 14],
    [4, 'Morocco', 7, 4, 1, 2, 6, 5, 1, 13],
    [5, 'England', 5, 3, 1, 1, 13, 4, 9, 10],
    [6, 'Netherlands', 5, 3, 1, 1, 10, 4, 6, 10],
    [7, 'Portugal', 5, 3, 0, 2, 12, 6, 6, 9],
    [8, 'Brazil', 5, 3, 0, 2, 8, 3, 5, 9],
    [9, 'Japan', 4, 2, 0, 2, 5, 4, 1, 6],
    [10, 'Senegal', 4, 2, 0, 2, 5, 7, -2, 6],
    [11, 'Australia', 4, 2, 0, 2, 4, 6, -2, 6],
    [12, 'Switzerland', 4, 2, 0, 2, 5, 9, -4, 6],
    [13, 'USA', 4, 1, 2, 1, 3, 4, -1, 5],
    [14, 'Spain', 4, 1, 1, 2, 9, 3, 6, 4],
    [15, 'Poland', 4, 1, 1, 2, 3, 5, -2, 4],
    [16, 'South_Korea', 4, 1, 1, 2, 5, 8, -3, 4],
    [17, 'Germany', 3, 1, 1, 1, 6, 5, 1, 4],
    [18, 'Ecuador', 3, 1, 1, 1, 4, 3, 1, 4],
    [19, 'Cameroon', 3, 1, 1, 1, 4, 4, 0, 4],
    [20, 'Uruguay', 3, 1, 1, 1, 2, 2, 0, 4],
    [21, 'Tunisia', 3, 1, 1, 1, 1, 1, 0, 4],
    [22, 'Mexico', 3, 1, 1, 1, 2, 3, -1, 4],
    [23, 'Belgium', 3, 1, 1, 1, 1, 2, -1, 4],
    [24, 'Ghana', 3, 1, 0, 2, 5, 7, -2, 3],
    [25, 'Saudi_Arabia', 3, 1, 0, 2, 3, 5, -2, 3],
    [26, 'Iran', 3, 1, 0, 2, 4, 7, -3, 3],
    [27, 'Costa_Rica', 3, 1, 0, 2, 3, 11, -8, 3],
    [28, 'Denmark', 3, 0, 1, 2, 1, 3, -2, 1],
    [29, 'Serbia', 3, 0, 1, 2, 5, 8, -3, 1],
    [30, 'Wales', 3, 0, 1, 2, 1, 6, -5, 1],
    [31, 'Canada', 3, 0, 0, 3, 2, 7, -5, 0],
    [32, 'Qatar', 3, 0, 0, 3, 1, 7, -6, 0],
]

df = pd.DataFrame(data, columns=['Position', 'Team', 'Games Played', 'Win', 'Draw', 'Loss', 'Goals For', 'Goals Against', 'Goal Difference', 'Points'])

colonnes_enlevees = df.drop(['Win', 'Loss'], axis=1)

print(colonnes_enlevees)

chemin = "FIFA_World_Cup/Classement_sans_deux_colonnes.txt"
with open(chemin, mode = "w") as mon_fichier:
  mon_fichier.write("Classement_sans_deux_colonnes\n")
  mon_fichier.writelines(repr(colonnes_enlevees))

