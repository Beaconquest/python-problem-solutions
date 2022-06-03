# python execrises from www.practicepython.org

# Execrise 9

import random

guess_number = random.randint(1, 9)
count = 0

while True:
    
    try:
        user = input("Please guess a number between 1 and 9: ")

        if user == "exit":
            if count == 0:
                break
            else:
                break
    
        user = int(user)

        count += 1
        
        if user == guess_number:
            print("Exactly right!")
            break
        elif user > guess_number:
            print("Too high!")
        else:
            print("Too low!")

    except ValueError:
        print('oh something went wrong! Try again!')
    except KeyboardInterrupt:
        print("No need to be end so rough!")
        break

if  count == 0:
    print("You quit before the game begun.")
elif count == 1:
    print(f"Wow, it only took you {count}")
else:
    print(f"The game lasted {count} rounds!")
