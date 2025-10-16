ttt = [['7', '8', '9'],
       ['4', '5', '6'],
       ['1', '2', '3']]

player1 = 'X'
player2 = 'O'
current_player = player1

def setze_feld(ttt, feld, symbol):
    for i, row in enumerate(ttt):
        for j, value in enumerate(row):
            if value == feld:
                ttt[i][j] = symbol
                return True
    return False

def spielfeld_voll(ttt):
    return all(feld in ['X', 'O'] for row in ttt for feld in row)

def gewonnen(ttt, symbol):
    # Zeilen
    for row in ttt:
        if all(feld == symbol for feld in row):
            return True
    # Spalten
    for col in range(3):
        if all(ttt[row][col] == symbol for row in range(3)):
            return True
    # Diagonalen
    if all(ttt[i][i] == symbol for i in range(3)):
        return True
    if all(ttt[i][2-i] == symbol for i in range(3)):
        return True
    return False

while True:
    for row in ttt:
        print(" | ".join(row))
    feld = input(f"Spieler {current_player}, wähle ein Feld (1-9): ")
    if setze_feld(ttt, feld, current_player):
        if gewonnen(ttt, current_player):
            for row in ttt:
                print(" | ".join(row))
            print(f"Spieler {current_player} hat gewonnen!")
            break
        if spielfeld_voll(ttt):
            for row in ttt:
                print(" | ".join(row))
            print("Unentschieden!")
            break
        current_player = player2 if current_player == player1 else player1
    else:

        print("Ungültige Eingabe. Bitte versuche es erneut.") 

