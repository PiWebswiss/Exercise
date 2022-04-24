# 04. Exercise: Write the code!
import random
secret_number = random.randint(1, 100) # Should I write this two line in my function ?
print(secret_number) # for testing

attempts = []  # Creating an array.

def game():
    try:
        user = int(input("Please enter a number: "))
        # Storing the user input in the array.
        attempts.append(user)
        # Calculating the number of value in the array.
        attempts_number = len(attempts)
        if secret_number > user:
            print("The number is bigger!")
            return game() # It’s correct to return the function game()?
        elif secret_number < user:
            print("The number is smaller!")
            return game()
        elif secret_number == user and attempts_number == 1:
            print("You won the game in " + str(attempts_number) + " attempt")
            quit() 
        elif secret_number == user:
            print("You won the game in " + str(attempts_number) + " attempts")
            quit()
    except:
        print("You didn't enter a number.")
        quit()
    # New problem the except run (x time) the number of attempts !
        

game()



    

