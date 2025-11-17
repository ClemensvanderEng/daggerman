import random

a = ["-","-","-"]
b = ["-","-","-"]
c = ["-","-","-"]

def showboard():
    print("  a b c")
    print("1", a[0], b[0], c[0])
    print("2", a[1], b[1], c[1])
    print("3", a[2], b[2], c[2])
    print()

def checkvertical(column):
    if column[0] == column[1] == column[2] == "x":
        return 2
    if column[0] == column[1] == column[2] == "o":
        return 3

def checkwin():
    #horizontal
    for i in range(3):
        if a[i] == b[i] == c[i] == "x":
            return 2
        if a[i] == b[i] == c[i] == "o":
            return 3
    #vertical
    for column in (a, b, c):
        result = checkvertical(column)
        if result:
            return result
    #diagonal
    if a[0] == b[1] == c[2] == "x":
        return 2
    if a[0] == b[1] == c[2] == "o":
        return 3
    if a[2] == b[1] == c[0] == "x":
        return 2  
    if a[2] == b[1] == c[0] == "o":
        return 3
    return 0

win = 0
empty = 9
while win == 0:
    done = 0
    showboard()
    while done == 0:
        print("Name a colunm.")
        column = input()
        print("Name a row.")
        try:
            row = int(input()) - 1   # van "1..3" naar index 0..2
        except ValueError:
            print("Enter a number from 1 to 3.")
            continue
        if column == "a":
            if a[row] != "x" or "o":
                a[row] = "x"
                done = 1
        elif column == "b":
            if b[row] != "x" or "o":
                b[row] = "x"
                done = 1
        elif column == "c":
            if c[row] != "x" or "o":
                c[row] = "x"
                done = 1
        elif column == "no":
            done = 1
        if done == 0:
            print ("Error, try again.")
    win = checkwin()
    if win != 0:
        continue
    empty -= 1
    if empty == 0: 
        win = 1
        win = checkwin()
        continue
    empties = []
    for i in range(3):
        if a[i] == "-":
            empties.append(("a", i))
        if b[i] == "-":
            empties.append(("b", i))
        if c[i] == "-":
            empties.append(("c", i))
    if empties:
        col, i = random.choice(empties)
        if col == "a":
            a[i] = "o"
        elif col == "b":
            b[i] = "o"
        else:
            c[i] = "o"
        empty -= 1
    win = checkwin()
    if empty == 0: 
        win == 1
        win = checkwin()

showboard()

if win == 1:
    print ("It is a draw.")
elif win == 2:
    print ("You win.")
else:
    print ("You lose.")


    

        

    
