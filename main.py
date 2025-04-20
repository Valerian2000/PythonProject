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
    print(f"L'année {annee} est bissextile.")
else:
    print(f"L'année {annee} n'est pas bissextile.")
    
     
mois = input("Entrez un mois : ")
while not IsMonth(mois):
    print("Le mois doit être un nombre entier entre 1 et 12 ou le nom du mois.")
    mois = input("Entrez un mois : ")


    
print("Voulez vous calculer un salaire anuel ou mensuel ?")
choix = input("Entrez 'annuel' ou 'mensuel' : ").lower()
while not choix in ['annuel', 'mensuel']:
    print("Choix invalide. Veuillez entrer 'annuel' ou 'mensuel'.")
    choix = input("Entrez 'annuel' ou 'mensuel' : ").lower()


print("Le nombre de jours de présence doit être un nombre entier pouvant aller jusqu'à une trentaine de jours.")
presence = input("Entrez le nombre de jours de présence :")
while not IsPositiveInt(presence) or int(presence) > monthNomberOfDay[int(numberMonth(mois))]:
    if not IsPositiveInt(presence):
        print("Le nombre de jours de présence doit être un nombre entier positif.")
    elif int(presence) < 0:
        print("Le nombre de jours de présence ne peut pas être négatif.")
    elif int(presence) > monthNomberOfDay[int(numberMonth(mois))]:
        print(f"Le mois {yearsMonth[int(numberMonth(mois))]} n'a pas autant de jours.")
    presence = input("Entrez le nombre de jours de présence : ")


# Calcul du salaire brut de la taxe et du salaire net
salaire_brute = salaire_journalier * int(presence)
taxes = salaire_brute * total_taxes/100 
salaire_net = salaire_brute - taxes

# Affichage du salaire brut de la taxe et du salaire net
print(f"Le salaire brut est de {int(salaire_brute)} dollars({int(salaire_brute*taux_echange)} Fc) et les taxes s'elevent à {int(taxes)} dollars({int(taxes*taux_echange)} Fc).\n \
Le salaire mensuel net est de {int(salaire_net)} dollars. ce qui équivaut à {int(salaire_net* taux_echange)} franc congolais.") 
