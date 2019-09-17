def direction(letter):
    if letter == "n" or letter == "N":
        return k + 1
    elif letter == "s" or letter == "S":
        return k - 1
    elif letter == "e" or letter == "E":
        return k + 3
    elif letter == "w" or letter == "W":
        return k - 3 
        
k = 0
i = ""
while k != 6:
    if k == 0:
        print("You can travel: (N)orth")
        i = input("Direction: ")
        if i == "n" or i == "N":
            k = direction(i)
        else:
            print("Not a valid direction!")
    elif k == 1:
        print("You can travel: (N)orth or (East) or (S)outh")
        i = input("Direction: ")
        if i == "n" or i == "N" or i == "s" or i == "S"  or i == "e" or i == "E":
            k = direction(i)
        else:
            print("Not a valid direction!")
    elif k == 2:
        print("You can travel: (E)ast or (S)outh")
        i = input("Direction: ")
        if i == "e" or i == "E" or i == "s" or i == "S":
            k = direction(i)
        else:
            print("Not a valid direction!")
    elif k == 3:
        print("You can travel: (N)orth")
        i = input("Direction: ")
        if i == "n" or i == "N":
            k = direction(i)
        else:
            print("Not a valid direction!")
    elif k == 4:
        print("You can travel: (S)outh or (W)est")
        i = input("Direction: ")
        if i == "w" or i == "W"  or i == "s" or i == "S":
            k = direction(i)
        else:
            print("Not a valid direction!")
    elif k == 5:
        print("You can travel: (E)ast or (W)est")
        i = input("Direction: ")
        if i == "w" or i == "W" or i == "e" or i == "E":
            k = direction(i)
        else:
            print("Not a valid direction!")
    elif k == 7:
        print("You can travel: (N)orth or (S)outh")
        i = input("Direction: ")
        if i == "n" or i == "N" or i == "s" or i == "S":
            k = direction(i)
        else:
            print("Not a valid direction!")
    elif k == 8:
        print("You can travel: (S)outh or (W)est")
        i = input("Direction: ")
        if i == "w" or i == "w" or i == "s" or i == "S":
            k = direction(i)
        else:
            print("Not a valid direction!")
print("Victory")





