import random

grid = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]


def drawGrid():
    print(grid[0] + "|" + grid[1] + "|" + grid[2])
    print(grid[3] + "|" + grid[4] + "|" + grid[5])
    print(grid[6] + "|" + grid[7] + "|" + grid[8])
    print("--------------------------------------")


def userMove():
    while True:
        x = input("Pick an index:")
        try:
            x = int(x) - 1
        except:
            print("!!! Invalid index !!!")
            continue
        if x > 8 or x < 0:
            print("!!! Invalid index !!!")
        elif not grid[x].isdigit():
            print("!!! Invalid index !!!")
        else:
            break

    grid[x] = "X"


def computerMove():
    global continueGame
    vacantIndexes = []

    for i in grid:
        if i.isdigit():
            vacantIndexes.append(int(i) - 1)
    if vacantIndexes:
        index = random.choice(vacantIndexes)
        grid[index] = "O"
    else:
        drawGrid()
        print("The grid is full")
        continueGame = False


def checkWin():
    global continueGame

    win = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]

    userSquares = []
    computerSquares = []

    for i in range(9):
        if grid[i] == "X":
            userSquares.append(i)
        elif grid[i] == "O":
            computerSquares.append(i)

    for j in win:
        if set(j).issubset(set(userSquares)):
            print("""
 /$$   /$$                                     /$$      /$$ /$$                           /$$ /$$ /$$
| $$  | $$                                    | $$  /$ | $$|__/                          | $$| $$| $$
| $$  | $$  /$$$$$$$  /$$$$$$   /$$$$$$       | $$ /$$$| $$ /$$ /$$$$$$$   /$$$$$$$      | $$| $$| $$
| $$  | $$ /$$_____/ /$$__  $$ /$$__  $$      | $$/$$ $$ $$| $$| $$__  $$ /$$_____/      | $$| $$| $$
| $$  | $$|  $$$$$$ | $$$$$$$$| $$  \__/      | $$$$_  $$$$| $$| $$  \ $$|  $$$$$$       |__/|__/|__/
| $$  | $$ \____  $$| $$_____/| $$            | $$$/ \  $$$| $$| $$  | $$ \____  $$                  
|  $$$$$$/ /$$$$$$$/|  $$$$$$$| $$            | $$/   \  $$| $$| $$  | $$ /$$$$$$$/       /$$ /$$ /$$
 \______/ |_______/  \_______/|__/            |__/     \__/|__/|__/  |__/|_______/       |__/|__/|__/
                 """)
            drawGrid()
            continueGame = False
        if set(j).issubset(set(computerSquares)):
            print("""
  /$$$$$$                                                /$$                               /$$      /$$ /$$                           /$$ /$$ /$$
 /$$__  $$                                              | $$                              | $$  /$ | $$|__/                          | $$| $$| $$
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$ /$$$| $$ /$$ /$$$$$$$   /$$$$$$$      | $$| $$| $$
| $$       /$$__  $$| $$_  $$_  $$ /$$__  $$| $$  | $$|_  $$_/   /$$__  $$ /$$__  $$      | $$/$$ $$ $$| $$| $$__  $$ /$$_____/      | $$| $$| $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$  \ $$| $$  | $$  | $$    | $$$$$$$$| $$  \__/      | $$$$_  $$$$| $$| $$  \ $$|  $$$$$$       |__/|__/|__/
| $$    $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$  | $$  | $$ /$$| $$_____/| $$            | $$$/ \  $$$| $$| $$  | $$ \____  $$                  
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$/  |  $$$$/|  $$$$$$$| $$            | $$/   \  $$| $$| $$  | $$ /$$$$$$$/       /$$ /$$ /$$
 \______/  \______/ |__/ |__/ |__/| $$____/  \______/    \___/   \_______/|__/            |__/     \__/|__/|__/  |__/|_______/       |__/|__/|__/
                                  | $$                                                                                                           
                                  | $$                                                                                                           
                                  |__/                                                                                                           
                """)
            drawGrid()
            continueGame = False


# ========= Main =========

print("""
Welcome to
  _______ _____ _____   _______       _____   _______ ____  ______ 
 |__   __|_   _/ ____| |__   __|/\   / ____| |__   __/ __ \|  ____|
    | |    | || |         | |  /  \ | |         | | | |  | | |__   
    | |    | || |         | | / /\ \| |         | | | |  | |  __|  
    | |   _| || |____     | |/ ____ \ |____     | | | |__| | |____ 
    |_|  |_____\_____|    |_/_/    \_\_____|    |_|  \____/|______|

Created by: MrLDGCA
""")


continueGame = True

while continueGame:
    drawGrid()
    userMove()
    checkWin()
    if not continueGame:
        break
    computerMove()
    checkWin()

print("Hope you enjoyed")
