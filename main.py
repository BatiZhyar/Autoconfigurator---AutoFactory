import os

def configuratie_aanmaken():
    prijs = 0
    print("\n===== CONFIGURATIE AANMAKEN =====")
    print("\nEr zijn verschillende automodellen om te kiezen.")
    print("1. SUV, 2. Sedan, 3. Hatchback, 4. Coupé")

    while True:
        automodel = input("Welk automodel kies je? ")
        if automodel == "1":
            auto = "SUV"
            prijs += 10000
            break
        elif automodel == "2":
            auto = "Sedan"
            prijs += 15000
            break
        elif automodel == "3":
            auto = "Hatchback"
            prijs += 12000
            break
        elif automodel == "4":
            auto = "Coupé"
            prijs += 20000
            break
        else:
            print("Ongeldige invoer! Kies een getal van 1 t/m 4.")

    print("\nEr zijn verschillende motortypes om te kiezen.")
    print("1. Benzinemotor, 2. Dieselmotor, 3. Elektrische motor, 4. Hybride motor")
    
    while True:
        motortype = input("Welk motortype kies je? ")
        if motortype == "1":
            motor = "Benzinemotor"
            prijs += 5000
            break
        elif motortype == "2":
            motor = "Dieselmotor"
            prijs += 7000
            break
        elif motortype == "3":
            motor = "Elektrische motor"
            prijs += 10000
            break
        elif motortype == "4":
            motor = "Hybride motor"
            prijs += 15000
            break
        else:
            print("Ongeldige invoer! Kies een getal van 1 t/m 4.")

    print("\nEr zijn verschillende kleuren om te kiezen.")
    print("1. Wit, 2. Zwart, 3. Roze, 4. Blauw")

    while True:
        kleur = input("Welke kleur kies je? ")
        if kleur == "1":
            color = "Wit"
            prijs += 1000
            break
        elif kleur == "2":
            color = "Zwart"
            prijs += 1000
            break
        elif kleur == "3":
            color = "Roze"
            prijs += 1000
            break
        elif kleur == "4":
            color = "Blauw"
            prijs += 1000
            break
        else:
            print("Ongeldige invoer! Kies een getal van 1 t/m 4.")

    print("\nEr zijn verschillende uitvoeringen om te kiezen.")
    print("1. Basisuitvoering, 2. Comfort, 3. Sport, 4. Luxury")

    while True:
        uitvoering = input("Welke uitvoering kies je? ")
        if uitvoering == "1":
            uitvoer = "Basisuitvoering"
            prijs += 5000
            break
        elif uitvoering == "2":
            uitvoer = "Comfort"
            prijs += 7500
            break
        elif uitvoering == "3":
            uitvoer = "Sport"
            prijs += 10000
            break
        elif uitvoering == "4":
            uitvoer = "Luxury"
            prijs += 15000
            break
        else:
            print("Ongeldige invoer! Kies een getal van 1 t/m 4.")

    print("\nEr zijn verschillende extra opties om te kiezen.")
    print("1. Panoramadak, 2. Lederen bekleding, 3. Verwarmde stoelen, 4. Parkeersensoren")
    
    while True:
        Extra = input("Welke extra optie kies je? ")
        if Extra == "1":
            optie = "Panoramadak"
            prijs += 2000
            break
        elif Extra == "2":
            optie = "Lederen bekleding"
            prijs += 3000
            break
        elif Extra == "3":
            optie = "Verwarmde stoelen"
            prijs += 1500
            break
        elif Extra == "4":
            optie = "Parkeersensoren"
            prijs += 2000
            break
        else:
            print("Ongeldige invoer! Kies een getal van 1 t/m 4.")

    configuratie = (
        f"Automodel: {auto}\n"
        f"Motortype: {motor}\n"
        f"Kleur: {color}\n"
        f"Uitvoering: {uitvoer}\n"
        f"Extra optie: {optie}\n"
        f"Totale prijs: €{prijs}\n"
    )
    print("\n===== JOUW CONFIGURATIE =====")
    print(configuratie)
    return configuratie

def configuratie_opslaan(configuratie):
    if configuratie == "":
        print("Maak eerst een configuratie aan.")
    else:
        with open("configuraties.txt", "w") as bestand:
            bestand.write(configuratie)
        print("Configuratie succesvol opgeslagen!")

def configuratie_inlezen():
    if os.path.exists("configuraties.txt"):
        with open("configuraties.txt", "r") as bestand:
            configuratie = bestand.read()

        print("\n===== OPGESLAGEN CONFIGURATIE =====")
        print(configuratie)
    else:
        print("Er is nog geen opgeslagen configuratie gevonden.")

def hoofdmenu():
    configuratie = ""
    while True:
        print("\n========== HOOFDMENU ==========")
        print("1. Configuratie aanmaken")
        print("2. Configuratie opslaan")
        print("3. Configuratie inlezen")
        print("4. Programma Afsluiten")
        keuze = input("\nMaak een keuze (1-4): ")
        if keuze == "1":
            configuratie = configuratie_aanmaken()
        elif keuze == "2":
            configuratie_opslaan(configuratie)
        elif keuze == "3":
            configuratie_inlezen()
        elif keuze == "4":
            print("Programma wordt afgesloten. Tot ziens!")
            break
        else:
            print("Ongeldige keuze! Kies een getal van 1 t/m 4.")
hoofdmenu()
