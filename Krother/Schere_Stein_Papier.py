import random

spieler = input("Wähle Schere(SH), Stein(ST), Papier(P): ").strip().upper()
computer = random.choice(["SH", "ST", "P"])

# Zustandsvariable: Standard-Ausgabe ist "Computer gewinnt!"
result = "Computer gewinnt!"


if spieler == computer:
    result = "Unentschieden!"


if (spieler == "SH" and computer == "P") or \
   (spieler == "ST" and computer == "SH") or \
   (spieler == "P"  and computer == "ST"):
    result = "Du gewinnst!"

print(result)