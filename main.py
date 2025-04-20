from varTools import yearsMonth
from varTools import monthNomberOfDay 
from varTools import total_taxes
from varTools import taux_echange
from varTools import  salaire_journalier

from fonctionTools import IsPositiveInt
from fonctionTools import IsBissextile 
from fonctionTools import IsMonth
from fonctionTools import numberMonth





# Nous demandons à l'utilisateur d'entrer une année
# et nous vérifions si c'est un entier positif
# Si ca ne l'est pas le programme redemande une année correcte
annee = input("Entrez une année : ")
while not IsPositiveInt(annee):
    print("L'année doit être un nombre entier positif.")
    annee = input("Entrez une année : ")

if IsBissextile(annee):
    monthNomberOfDay[2]=29
    
     
mois = input("Entrez un mois : ")
while not IsMonth(mois):
    print("Le mois doit être un nombre entier entre 1 et 12 ou le nom du mois.")
    mois = input("Entrez un mois : ")


    
print("Voulez vous calculer un salaire anuel ou mensuel ?")
choix = input("Entrez 'annuel' ou 'mensuel' : ").lower()
while not choix in ['annuel', 'mensuel']:
    print("Choix invalide. Veuillez entrer 'annuel' ou 'mensuel'.")
    choix = input("Entrez 'annuel' ou 'mensuel' : ").lower()



presence = input("Entrez le nombre de jours de présence :")
while not IsPositiveInt(presence) or int(presence) > monthNomberOfDay[int(numberMonth(mois))]:
    if not IsPositiveInt(presence):
        print("Le nombre de jours de présence doit être un nombre entier positif.")
    elif int(presence) < 0:
        print("Le nombre de jours de présence ne peut pas être négatif.")
    elif int(presence) > monthNomberOfDay[numberMonth(mois)]:
        print(f"Le mois {yearsMonth[numberMonth(mois)]} n'a pas autant de jours.")

    print("Le nombre de jours de présence doit être un nombre entier positif.")
    presence = input("Entrez le nombre de jours de présence : ")



salaire_mensuel_brute = salaire_journalier * int(presence)
salaire_mensuel_net = salaire_mensuel_brute*(1 - total_taxes/100) 

print(f"Le salaire mensuel net est de {salaire_mensuel_net} dollars. ce qui équivaut à{salaire_mensuel_net* taux_echange}  ")
