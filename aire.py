def calculer():
	longueurDuRayon = input("donner longueur du rayon \n")
	longueurDuRayon = float(longueurDuRayon)
	perimetre = 2*3.14*longueurDuRayon
	print(perimetre,"m")
	aire = 3.14*longueurDuRayon*longueurDuRayon
	print (aire,"m2")

calculer()
import os
os.system('pause')