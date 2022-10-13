import datetime

import locale
import ctypes


windll = ctypes.windll.kernel32
lang = locale.windows_locale[ windll.GetUserDefaultUILanguage() ]



print(lang);

heure = datetime.datetime.now().hour

bonjour = ""
aurevoir = ""

if lang == "fr_FR":
    if 5 <= heure < 18:
        bonjour = "Bonjour"
    else:
        bonjour = "Bonsoir"

    if 5 <= heure < 12:
        aurevoir = "Bonne fin de matinée"
    elif 12 <= heure < 18:
        aurevoir = "Bonne fin d'après midi"
    elif heure < 2 or 18 <= heure:
        aurevoir = "Bonne soirée"
    else:
        aurevoir = "Bonne nuité les ptiots"
else:
    if 5 <= heure < 18:
        bonjour = "Good Morning"
    else:
        bonjour = "Good Afternoon"

    if 5 <= heure < 12:
        aurevoir = "good late morning"
    elif 12 <= heure < 18:
        aurevoir = "good late Afternoon"
    elif heure < 2 or 18 <= heure:
        aurevoir = "good evening"
    else:
        aurevoir = "good night"

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