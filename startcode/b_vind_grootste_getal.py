# Maak een lijst met getallen.
# Schrijf een functie vind_grootste_getal die de grootste waarde uit een lijst teruggeeft.
# Gebruik een for-loop om de grootste waarde te vinden.

getallen = [1,5,2,8,9,6,3]

getallen.sort()
for i in getallen:
    print(i)

def Vind_grootste_getal():
    getal = getallen.pop()
    print(getal)

Vind_grootste_getal()