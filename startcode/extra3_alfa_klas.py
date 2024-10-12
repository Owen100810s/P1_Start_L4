# Maak een programma dat:
# - De gebruiker één voor één een naam van een klasgenoot laat intypen. Het programma blijft vragen tot er eens een lege string wordt ingevuld.
# - Je gaat dan deze lijst met namen alfabetisch sorteren.
# - Deze gesorteerde namen ga je dan printen.

Namen = []
counter = 0

while counter < 5:
    Namen_input = input("Geef me de namen van je klasgenoten!(typ 'Ik ben klaar' als je klaar bent!) ")

    if Namen_input == "Ik ben klaar":
        print("Oké! Hier is de lijst van namen die je me gegeven hebt:")
        for i in Namen:
            print(i)
        counter = 8
    else:
        Namen.append(Namen_input)
