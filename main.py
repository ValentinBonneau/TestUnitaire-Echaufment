import datetime

heure = datetime.datetime.now().hour

bonjour = ""
aurevoir = ""

if 5 <= heure < 18:
    bonjour = "Bonjour"
else:
    bonjour = "Bonsoir"

if 5 <= heure < 12:
    aurevoir = "Bonne fin de matinée"
elif 12 <= heure < 18:
    aurevoir = "Bonne fin d'après midi"
elif heure < 2 or 18 <= heure:
    aurevoir = "Bonne fin d'après midi"
else:
    aurevoir = "Bonne nuité les ptiots"

print(bonjour, "et bienvenue sur le programme d'échaufment de Valentin Bonneau")

test = True

while test:
    print('''Entrez quelque chose (":q!" pour quité (non je l'ai pas fait sur vim))''')
    chaine = input()
    inverse = "".join(reversed(chaine))
    if chaine == ":q!":
        test = False
    elif chaine == inverse:
        print("Bien dit !")
    else:
        print(inverse)


print(aurevoir)