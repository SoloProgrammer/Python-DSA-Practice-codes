import random

no_of_guess = 1
no_to_guess = random.randint(1,30)
print(no_to_guess)

no_of_try = 0

def win():
    print("\nYoohoo! You have Correct guess .... \n")
    print(f"you Guess the no in {no_of_try} Tries \n")

while no_of_guess <= 9:
    if no_of_try == 0:
        n = int(input("Enter a number between 1 - 30 but you have only 9 Tries:"))
    else:
        n = int(input("Guess again: "))
    no_of_try += 1
    if no_of_guess == 9:
        if n == no_to_guess:
            win()
            break
        else:
            print("\nsoooory you have excced your tries!!!!!   Game Over ")
            print(f"The num to guess is {no_to_guess} \n")
            break 
    else:
        if n == no_to_guess:
            win()
            break
        elif n == no_to_guess - 2 or n == no_to_guess - 1 or n == no_to_guess + 2 or n == no_to_guess + 1 :
            print("You are Close ,keep Trying!!")
            print(f"you have only {9 - no_of_try} Tries remain!!")

        elif n < no_to_guess:
            print("You Guess to small")
            print(f"you have only {9 - no_of_try} Tries remain!!")
        elif n > no_to_guess:
            print("You Guess to Big")
            print(f"you have only {9 - no_of_try} Tries remain!!")



    no_of_guess += 1