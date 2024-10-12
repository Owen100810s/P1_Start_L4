# We gaan aan de gebruiker een aantal instructies vragen en op basis daarvan tekenen.
# - Maak eerst een lege lijst waar de stappen in zullen komen.
# - Maak een oneindige lus:
#     - Vraag een stap aan de gebruiker
#     - Als het gelijk is aan “stop”, breek uit de lus.
#     - Anders, voeg het toe aan de lijst met stappen.
# - Itereer over de stappenlijst om te tekenen.
import turtle

counter = 0
while counter < 5:
    instructie = input("welke stap moet ik zetten? ")

    if instructie == "boven":
        turtle.forward(100)
    elif instructie == "beneden":
        turtle.backward(100)
    elif instructie == "links":
        turtle.left(90)
        turtle.forward(100)
    elif instructie == "rechts":
        turtle.right(90)
        turtle.forward(100)
    elif instructie == "stop":
        counter = 8




turtle.done()




