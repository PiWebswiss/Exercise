# 04. Exercise: Write the code!

import random
secret_number = random.randint(1, 5)


def game():
    user = input("Please enter a number: ")
    guess = int(user)
    # creating an array
    attempts = []
    # storing the user input in the array
    attempts.append(user)
    print(attempts)
    # calculating the number of value in the array
    attempts_number = len(attempts)
    print(attempts_number)

    if guess != secret_number:
        # I don't know how to store multiple value in the array?
        return game()


game()

""" if secret_number > guess:
    print("The number is bigger")
elif secret_number < guess:
    print("The number is smaller ")
elif secret_number == guess:
    print(i)
    quit() """



    

