from varTools import yearsMonth
from varTools import monthNomberOfDay 

# Nous testons si une valeur est un entier positif
def IsPositiveInt(value):
    return value.isdigit() and int(value) > 0


# Nous testons si l'argument est un mois
def IsMonth(mois):
    return (IsPositiveInt(mois) and 1 <= int(mois) <= 12) or (mois.lower() in yearsMonth.values())


# Nous testons si l'année est bissextile
def IsBissextile(annee):
    annee = int(annee)
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)


def numberMonth(mois):
    if IsPositiveInt(mois):
        return mois
    elif mois.lower() in yearsMonth.values():
        return yearsMonth.get(mois.lower())