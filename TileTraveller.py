#There are nine tiles so we need nine values for our tiles. Adding 1 every time we go up,
#subtracting when we go down and adding 3(since 2 was not sufficient for different numbers),
#and we employ six functions for the six option of movement we have.
def n():
    i = input("Direction: ")
    if i == "n" or i == "N":
        return k + 1
    else:
        print("Not a valid direction!")
        return n()
   

def nes():
    i = input("Direction: ")
    if i == "n" or i == "N":
        return k + 1
    elif i == "s" or i == "S":
        return k - 1
    elif i == "e" or i == "E":
        return k + 3
    else:
        print("Not a valid direction!")
        return nes()
   
           
def sw():
    i = input("Direction: ")
    if i == "s" or i == "S":
        return k - 1
    elif i == "w" or i == "W":
        return k - 3 
    else:
        print("Not a valid direction!")
        return sw()

def ns():
    i = input("Direction: ")
    if i == "n" or i == "N":
        return k + 1
    elif i == "s" or i == "S":
        return k - 1
    else:
        print("Not a valid direction!")
        return ns()

def ew():
    i = input("Direction: ")
    if i == "e" or i == "E":
        return k + 3
    elif i == "w" or i == "W":
        return k - 3 
    else:
        print("Not a valid direction!")
        return ew()
def es():
    i = input("Direction: ")
    if i == "s" or i == "S":
        return k - 1
    elif i == "e" or i == "E":
        return k + 3
    else:
        print("Not a valid direction!")
        return es()

        
        
k = 0
i = ""

        
while k != 6:
    if k == 0:
        print("You can travel: (N)orth.")
        k = n()
    elif k == 1:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        k = nes()
    elif k == 2:
        print("You can travel: (E)ast or (S)outh.")
        k = es()
    elif k == 3:
        print("You can travel: (N)orth.")
        k = n()
    elif k == 4:
        print("You can travel: (S)outh or (W)est.")
        k = sw()
 
    elif k == 5:
        print("You can travel: (E)ast or (W)est.")
        k = ew()
      
    elif k == 7:
        print("You can travel: (N)orth or (S)outh.")
        k = ns()
 
    elif k == 8:
        print("You can travel: (S)outh or (W)est.")
        k = sw()

print("Victory!")





