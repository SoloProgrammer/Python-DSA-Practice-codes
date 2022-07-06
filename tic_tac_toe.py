from operator import le


def showboard(xval,oval):
    # print(xval)

    # print(oval)
  
    one = 'X' if xval[0] else ('o' if oval[0] else 1 )
    two = 'X' if xval[1] else ('o' if oval[1] else 2 )
    three = 'X' if xval[2] else ('o' if oval[2] else  3)
    four = 'X' if xval[3] else ('o' if oval[3] else 4 )
    five = 'X' if xval[4] else ('o' if oval[4] else 5 )
    six = 'X' if xval[5] else ('o' if oval[5] else 6 )
    seven = 'X' if xval[6] else ('o' if oval[6] else 7 )
    eight = 'X' if xval[7] else ('o' if oval[7] else 8 )
    nine = 'X' if xval[8] else ('o' if oval[8] else 9 )
    print(f"| {one} | {two} | {three} |")
    print(f"|---|---|---|")
    print(f"| {four} | {five} | {six} |")
    print(f"|---|---|---|")
    print(f"| {seven} | {eight} | {nine} |")

def sum(a,b,c):
    return a + b + c

def checkwin(xvalues,ovalues):
    wins = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    for win in wins:        
        if(sum(xvalues[win[0] -1], xvalues[win[1] -1], xvalues[win[2] -1]) == 3):

            # print(xvalues[win[0] -1], xvalues[win[1] -1], xvalues[win[2] -1])

            print("\nplayer 1 wins !...............Congragulations\n")

            showboard(xvalues,ovalues)

            return 1

        if(sum(ovalues[win[0] -1], ovalues[win[1] -1], ovalues[win[2] -1]) == 3):

            # print(ovalues[win[0] -1], ovalues[win[1] -1], ovalues[win[2] -1])

            print("\nplayer 2 wins !...............Congragulations\n")

            showboard(xvalues,ovalues)

            return 1
 
    return -1


def main_code(chance,xvalues,ovalues):
    showboard(xvalues,ovalues)
            
    print("\n")

    if(chance == 1):
        print("Its 'player1's-(X) Turn \n")
    
        val = int(input("Enter value of position you want to place 'X' - "))

        if(val <= 9 and val > 0):
                if(ovalues[val - 1] == 0):
                    xvalues[val - 1] = 1
                else:
                    print("\n")
                    print("Plz choose the position where o is not placed ! choose again")
                    return "x-again"

                # xvalues[val - 1] = 1
                # print(xvalues)
        else:
            print("plz enter a value that given in gameboard \n")
    else:
        print("Its 'player2's-(o) Turn")
        val = int(input("Enter value of position you want to place 'o' - "))
        if(val <= 9 and val > 0):
            if(xvalues[val -1] == 0):
                ovalues[val - 1] = 1
            
            # ovalues[val - 1] = 1

        else:
            print("plz enter a value that given in board \n")
            

def play():
    xvalues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ovalues = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    chance = 1
    print("\n!...................................Welcome to Tic_Tac_Toe ...................................!\n")

    while(True):
        if(xvalues.count(0) > 4 and ovalues.count(0) > 4):
                val = main_code(chance,xvalues,ovalues)      ## Calling function
                cwin = checkwin(xvalues,ovalues)            ## Calling function
                # print(xvalues,ovalues)      
                if(cwin != -1):
                    print("\n........\n")

                    print("1. Exit \n")
                    print("2. Play again \n")
                    user_choice = int(input("Enter your choice : "))

                    if(user_choice == 1):
                        print("\nThanx for playing !................................... :) \n")
                        break

                    else:
                        play()
                        break
                if val == "x-again":
                    chance = 0

                chance = 1 - chance
            
        else:
            showboard(xvalues,ovalues)

            print("\nIts tie\n")

            print("1. Exit \n")
            print("2. Play again \n")
            user_choice = int(input("Enter your choice : "))

            if(user_choice == 1):
                print("\nThanx for playing !................................... :) \n")
                break

            else:
               play()
               break
   

if __name__  ==  "__main__":

    play()
    

            

        



