# coding : utf-8

import random
import os
os.system("clear")

#Créer une classe player qui a comme attribut: self (nom du joueur), lastscore (Le score de la partie précédente), et bestscore (Le meilleur score), les valeurs du meilleur score et le score précédent sont initialisées d'un 0 en cas ou le joueur n'a jamais joué. 
class player:

	def __init__(self, name, lastscore = 0, bestscore = 0):
		self.name = name
		self.lastS = lastscore
		self.bestS = bestscore
#Méthode pour tester le score courant, si la valeur du meilleur score est plus petite que la valeur du score de la partie couranate, sa valeur sera écrasée.  

	def score(self, Score):
		self.dScore = Score
		if self.dScore > self.mScore:
			self.mScore = self.dScore


#Une fonction pour afficher l'état du jeu. 

def screen(namePlayer,listobj):
	os.system("clear")

	print("{}".format(namePlayer))
	i = 0
	while i < len(listobj):
		l = ["|	"] + ["*"]*listobj[i] + [" "]*(max(listobj) - listobj[i]) + ["	|"]
		_str = "".join(l)
		print("{} {} {}".format(i+1, _str, listobj[i]))
		i = i + 1
	print("introduiser le numéro du tas ainsi que le nombre de nombre de pierre sous cette forme: 1 - 4 càd premier tas - quatre pierre")


def dealingFunction():
#Tester si l’un des deux joueurs a déjà joué au jeu, l’ordinateur doit récupérer le score de la dernière partie jouée ainsi que le meilleur score obtenu par le joueur depuis un fichier de sauvegarde.

	P1 = input("nom du premier joueur :")
	P2 = input("nom du second joueur :")
	_list = [player(P1), player(P2)]
	file_save = open("save.txt")
	Lines = file_save.readlines()
	file_save.close()
	lines = [Lines[0].strip()]
	lines[0] = lines[0].split(" ")
	l = []
	for i in l:
	 	l.append(i[0].split("	"))
	for i in l:
	 	if (i[0] == P1) or (i[0] == P2):
	 		if i[0] == P1 :
	 			_list[0].lastS = i[1]
	 			_list[0].bestS = i[2]
	 		if i[0] == P2 :
	 			_list[1].lastS = i[1]
	 			_list[1].bestS = i[2]

#Tirer aléatoirement un chiffre entre 3 et 7 représentant le nombre de tas de pierres.
	rndm = random.randint(3,7)
	comteur = 0
	tas = []
	
	while i < rndm :
		tas.append(random.randint(5,23)) #il tire autant de chiffre entre 5 et 23 que de tas de pierres. Ces chiffres représentent le nombre de pierres par tas.
		comteur = comteur + 1
	nbr_tour = 0
#Le corps du jeu 

	p1win = False
	p2win = False
	while sum(tas) > 0 :
		nbr_tour += 1
		screen(P1, tas)
		res = input()
		res = res.split("-")
		res[0] = int(res[0])
		res[1] = int(res[1])
		tas[res[0] - 1] = tas[res[0] - 1] - res[1]
		if sum(tas) == 1:
			p1win = True
			break
		screen(P2, tas)
		res = input()
		res = res.split("-")
		res[0] = int(res[0])
		res[1] = int(res[1])
		tas[res[0] - 1] = tas[res[0] - 1] - res[1]
		if sum(tas) == 1:
			p2win = True
			break
	comteur = 1
	scorePartie = 0
	while comteur <= nbr_tour:
		points = points + comteur*(10)**comteur #Calcul du score pour le joueur gagnant. 
	#Actualiser les valeurs des attributs du score des joueurs dans le fichier save.txt. 
	if p1win: 
		_list[0].score(Score = points)
		for i in l:
	 		if i[0] == _list[0].name:
	 			i[1] = _list[0].lastS 
	 			i[2] = _list[0].bestS
	else:
		_list[1].score(Score = points)
		for i in l:
	 		if i[0] == _list[1].name:
	 			i[1] = _list[1].lastS 
	 			i[2] = _list[1].bestS
	file_save = open("save.txt", 'w')
	for i in l:
		file_save.write(" {}	{}	{}".format(i[0],i[1],i[2]))
	file_save.close(save.txt)

dealingFunction()
