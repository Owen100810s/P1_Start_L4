# Schrijf een programma genaamd “Score bijhouden”.
# De gebruiker kan:
# - Scores toevoegen
# - De hoogste score bekijken
# - Het gemiddelde berekenen
# - Het programma beëindigen


score = []
counter = 0

while counter < 5:
    score_toevoegen = input("Voeg een score toe: ")
    if score_toevoegen == "Ik ben klaar":
        print("Oké! Hier is een lijst van de scores die je me gegeven hebt:")
        for i in score:
            print(i)
        counter = 8
    elif score_toevoegen:
        score.append(score_toevoegen)
    else:
        print("Error! Probeer opnieuw!")
        counter = 0
