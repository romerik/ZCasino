#coding:utf-8
from random import randrange
from math import ceil
def jeu(numero_mise=50):
	continuer_partie=1
	while continuer_partie==1:
		somme=0
		nombre_aleatoire=0
		numero_mise=50
		while numero_mise<0 or numero_mise>49:
			try:
				numero_mise=input("Entrez un numéro compris entre 0 et 49 pour miser dessus(les bornes 0 et 49 étant inclus): ")
				numero_mise=int(numero_mise)
			except:
				print("Valeur mal renseignée: ")
				numero_mise=-1
				continue
		while somme<=0:
			try:
				somme=input("Combien voulez vous misez comme somme: ")
				somme=int(somme)
			except:
				print("Mauvaise valeur entrée: ")
				somme=-1
				continue
		nombre_aleatoire=randrange(50)
		print("Le nombre aléatoirement généré par la machine est: {}".format(nombre_aleatoire))
		if nombre_aleatoire==numero_mise:
			print("Bravo vous êtes un(e) génie. Vous venez de triplez votre mise et maintenant vous gagnez: {}".format(3*somme))
		elif nombre_aleatoire%2==numero_mise%2:
			print("Bien bravo à toi.Ton numéro n'est pas celui trouvé lors du jeu mais au moins de la même couleur.Tu remporte donc la moitié de ta somme à l'arrondi supérieur c'est-à dire: {}".format(ceil(somme/2)))
		else:
			print("Tu as perdu!!")
		continuer_partie=0
		print("Veux tu refaire une nouvelle partie ? :")
		print("1-Taper 1 pour refaire une nouvelle partie:")
		print("2-Taper 2 pour sortir du jeu:")
		while continuer_partie!=1 and continuer_partie!=2:
			try:
				continuer_partie=input("Quel est ton choix: ")
				continuer_partie=int(continuer_partie)
			except:
				print("Choix mal renseigné:")
		if continuer_partie==2:
                        break
def aide():
	print("AIDE")
	print("Ce jeu comme son nom l'indique est un jeu de CASINO.En effet, vous avez le droit de faire une mise d'une somme donnée puis de parier sur l'apparition d'un numéro donné; les numéros étants de 0 à 49. Les numéros pairs sont de couleur rouges et les impairs de couleur noir. Si votre nombre est celui qu'on trouve après qu'on lance le jeu vous gagner 3 fois votre mise, sinon si votre numéro est de même couleur que celui généré par la machine vous avez 50 pour cent de votre mise et dans tous les autres cas vous perdez.")
	print("----------------------------------------------------------------------------------------------")
	menu()
def menu(choix=0):
	print("MENU")
	print("1-Taper 1 pour voir l'aide afin de comprendre le but du jeu:")
	print("2-Taper 2 pour passer au jeu propement dit et jouer: ")
	while choix!=1 and choix!=2:
		try:
			choix=input("Quel est votre choix: ")
			choix=int(choix)
		except:
			print("Choix mal renseignée: ")
	if choix==1:
		aide();
	elif choix==2:
		jeu()
print("BIENVENUE A VOUS DANS LE JEU CASINO")
choix=0
numero_mise=50
argent_mise=0
menu()
