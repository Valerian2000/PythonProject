from tools import yearsMonth
from tools import monthNomberOfDay 

# Nous testons si une valeur est un entier positif
def Is_PositiveInt(value):
    return value.isdigit() and int(value) > 0


# Nous testons si l'argument est un mois
def Is_Month(mois):
    return (Is_PositiveInt(mois) and 1 <= mois <= 12) or (mois.lower() in yearsMonth.values())


# Nous testons si l'année est bissextile
def Is_bissextile(annee):
    annee = int(annee)
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)


def numberMonth(mois):
    if Is_PositiveInt(mois):
        return mois
    elif mois.lower() in yearsMonth.values():
        return yearsMonth.get(mois.lower())