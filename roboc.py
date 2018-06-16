# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avecPython pour lance le jeu.

"""

import os

from carte import Carte
from fonctions import *

# Les commandes a utiliser
commandes = ["Q", "N", "E", "S", "O"]

# Pour permettre à l'utilisateur de recommencer après avoir gagné
recommencer = True
gagne = False

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
	if nom_fichier.endswith(".txt"):
		chemin = os.path.join("cartes", nom_fichier)
		nom_carte = nom_fichier[:-3].lower()
		
		with open(chemin, "r") as fichier:
			contenu = fichier.read()
			# Création d'une carte	
			carte = Carte(nom_carte, contenu)
			cartes.append(carte)
			
reprendre, labyrinthe = reprendre_partie()
opt = ' '
if reprendre:
	while opt.lower() != 'o' and opt.lower() != 'n':
		opt = input("Voules-vouz reprendre la partie en cours? (o/n)")
	if opt == 'n':
		reprendre = False

# On affiche les cartes existantes
while recommencer:
	gagne = False
	if not reprendre:
		print("\nLabyrinthes existants :")
		for i, carte in enumerate(cartes):
			print(" {} - {}".format(i + 1, carte.nom))
			
		# Si il y a une partie sauvegardée, on l'affiche, à compléter

		# On demande à l'utilisateur de saisir une option
		choix = input("\nEntrez un número de labyrinthe pour commencer à jouer : ")
		while not choix.isnumeric() or len(choix) != 1:
			print("Vous n'avez pas choisie une option valide")
			choix = input("\nEntrez un número de labyrinthe pour commencer à jouer : ")

		# L'option choisie est un nombre mais n'est pas dans les options
		while int(choix) > len(cartes) or int(choix) < 1:
			print("Vous devez choisir une des options presentées")
			choix = input("\nEntrez un número de labyrinthe pour commencer à jouer : ")

		choix = int(choix)
		# On affiche le labyrinthe
		print("\n")
		for i, carte in enumerate(cartes):
			if i+1 == choix:
				labyrinthe = carte.labyrinthe
				afficher_labyrinthe(labyrinthe)
	else:
		print("Bienvenu(e) à nouveau! On reprend la partie où vous aviez resté\n")
		afficher_labyrinthe(labyrinthe)

	chaine = input("> ")
	commande = chaine[0]
	while not commande.isalpha():
		print("La commande n'est pas valide\n")
		chaine = input("> ")
		commande = chaine[0]
	commande = chaine[0].upper()

	while commande not in commandes:
		print("La commande choisie n'est pas valide")
		chaine = input("> ")
		commande = chaine[0].upper()
		nb_pos = verifier_longueur(chaine)

	while len(chaine) < 1 or len(chaine) > 2:
		print("Vous devez choisir la commande tout seule ou suvie d'un nombre inferieur à 9")
		chaine = input("> ")
		commande = chaine[0].upper()
		nb_pos = verifier_longueur(chaine)

	if len(chaine) == 2:
		while not chaine[1].isnumeric():
			print("Le caractère qui suit la commande n'est pas un numéro")
			chaine = input("> ")
	
	commande = chaine[0].upper()
	nb_pos = verifier_longueur(chaine)
	
	while commande != "Q":
		i = 0
		while i < nb_pos:
			pos_avant = labyrinthe.robot
			labyrinthe = verifier_pos(labyrinthe, commande)
			afficher_labyrinthe(labyrinthe)
			if pos_avant == labyrinthe.robot:
				break
			i += 1
			if labyrinthe.robot == labyrinthe.sortie:
				print("Félicitations ! Vous avez gagné !")
				commande = "Q"
				gagne = True
				break
		if commande != "Q":
			chaine = input("> ")
			commande = chaine[0].upper()
			nb_pos = verifier_longueur(chaine)
		
		while commande not in commandes:
			print("La commande choisie n'est pas valide")
			chaine = input("> ")
			commande = chaine[0].upper()
			nb_pos = verifier_longueur(chaine)

	if gagne is True:
		opt = input("Voulez-vous jouer à nouveau? (o/n)")
		if opt.lower() == "o":
			recommencer = True
			print("\n")
		else:
			recommencer = False
	else:
		recommencer = False
		sauvegarder = input("Voulez-vous sauvegarder la partie en cours? (o/n)")
		if sauvegarder.lower() == "o":
			sauvegarder_partie(labyrinthe)