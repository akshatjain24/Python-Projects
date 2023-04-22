l1 = [1,2,3,4,5,6,7,8,9]

def print_map():
    print(" "+str(l1[0])+" | "+str(l1[1])+" | "+str(l1[2])+" ")
    print("-"*3 + "|" + "-"*3 + "|" + "-"*3)
    print(" "+str(l1[3])+" | "+str(l1[4])+" | "+str(l1[5])+" ")
    print("-"*3 + "|" + "-"*3 + "|" + "-"*3)
    print(" "+str(l1[6])+" | "+str(l1[7])+" | "+str(l1[8])+" ")

i = 0

while (i<9):

    print_map()

    if i%2 == 0:
        print(" ")
        print("Player 1's Move")
        x = int(input("Enter the Position for X : "))
        if x <10 and x > 0:
            l1[x-1] = "X"
        else:
            print("Wrong Input !")
            i-=1

    else:
        print(" ")
        print("Player 2's Move")
        x = int(input("Enter the Position for O :" ))
        if x <10 and x > 0:
            l1[x-1] = "O"
        else:
            print("Wrong Input !")
            i-=1

    if l1[0] == l1[1] and l1[1] == l1[2]:
        if l1[1] == "X":
            print("*"*10 + " Player 1 Wins !!! " + "*"*10)
        else:
            print("*"*10 + " Player 2 Wins !!! " + "*"*10)
        break

    elif l1[3] == l1[4] and l1[4] == l1[5]:
        if l1[4] == "X":
            print("*"*10 + " Player 1 Wins !!! " + "*"*10)
        else:
            print("*"*10 + " Player 2 Wins !!! " + "*"*10)
        break

    elif l1[6] == l1[7] and l1[7] == l1[8]:
        if l1[7] == "X":
            print("*"*10 + " Player 1 Wins !!! " + "*"*10)
        else:
            print("*"*10 + " Player 2 Wins !!! " + "*"*10)
        break

    elif l1[0] == l1[3] and l1[3] == l1[6]:
        if l1[3] == "X":
            print("*"*10 + " Player 1 Wins !!! " + "*"*10)
        else:
            print("*"*10 + " Player 2 Wins !!! " + "*"*10)
        break

    elif l1[1] == l1[4] and l1[4] == l1[7]:
        if l1[4] == "X":
            print("*"*10 + " Player 1 Wins !!! " + "*"*10)
        else:
            print("*"*10 + " Player 2 Wins !!! " + "*"*10)
        break

    elif l1[2] == l1[5] and l1[5] == l1[8]:
        if l1[5] == "X":
            print("*"*10 + " Player 1 Wins !!! " + "*"*10)
        else:
            print("*"*10 + " Player 2 Wins !!! " + "*"*10)
        break

    elif l1[0] == l1[4] and l1[4] == l1[8]:
        if l1[4] == "X":
            print("*"*10 + " Player 1 Wins !!! " + "*"*10)
        else:
            print("*"*10 + " Player 2 Wins !!! " + "*"*10)
        break

    elif l1[2] == l1[4] and l1[4] == l1[6]:
        if l1[2] == "X":
            print("*"*10 + " Player 1 Wins !!! " + "*"*10)
        else:
            print("*"*10 + " Player 2 Wins !!! " + "*"*10)
        break

    i+=1