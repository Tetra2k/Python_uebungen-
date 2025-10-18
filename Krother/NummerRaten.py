import random

zahl = random.randint(1, 100)

player = input("Gib eine Zahl zwischen 1 und 100 ein. Du hast 5 Versuche: ")
richtig = False
versuche = 4
while not richtig and versuche > 0:
        try: 
            player = int(input("Gib eine Zahl zwischen 1 und 100 ein. Du hast noch {} Versuche: ".format(versuche)))
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")
            continue

        if zahl < player:
            versuche -= 1
            print("Die Zahl ist zu groß")
        elif zahl > player:
            versuche -= 1
            print("Die Zahl ist zu klein")
        else:
         print("Herzlichen Glückwunsch! Du hast die Zahl erraten.")
         richtig = True

if not richtig:
    print(f"Leider keine Versuche mehr. Die richtige Zahl war {zahl}.")