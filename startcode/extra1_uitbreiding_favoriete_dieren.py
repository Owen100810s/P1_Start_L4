# Maak een uitbreiding op de oefening favoriete dieren (a).
# - Na het printen van de lijst vraag je welk dier uit de lijst moet.
# - Nadien toon je de lijst opnieuw maar deze keer zonder het gekozen dier.


dier_1 = input("Wat is je favoriete dier? ")
dier_2 = input("Wat is je tweede favoriete dier? ")
dier_3 = input("Wat is je derde favoriete dier? ")

dieren = [dier_1, dier_2, dier_3]
for i in dieren:
    print(i)

verwijderen = input("Vind je dat er een dier uit de lijst moet? Zo ja, welk dier? ")

if verwijderen == dier_1:
    dieren.remove(dier_1)
elif verwijderen == dier_2:
    dieren.remove(dier_2)
elif verwijderen == dier_3:
    dieren.remove(dier_3)
elif verwijderen == "Nee":
    print("Oke!")
else:
    print("Error! Probeer opnieuw!")

for i in dieren:
    print(i)