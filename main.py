import random

items = [1, 2, 3]

print("Hello. Welcome to the Rock, paper, scissors game!")
user = int(input("If you are brave enough and want to play with me, please choose between: paper-1, scissors-2, stone-3. "))
computer = random.choice(items)


while True:
    if user == computer:
        print("We're are both winners.")
        print("You have chosen " + str(user) + " and I have chosen " + str(computer))

    elif user == 1 and computer == 3 or user == 2 and computer == 1 or user == 3 and computer == 2:
        print("You have chosen " + str(user) + " and I have chosen " + str(computer))
        print("You're the winner. Hats off to you!")

    elif user == 1 and computer == 1 or user == 2 and computer ==2 or user ==3 and computer == 3:
        print("You have chosen " + str(user) + " and I have chosen " + str(computer))
        print("I have won this time. Sorry, human.")

    else:
        print("User put " + str(user) + " and computer put " + str(computer))
        print("You loose, because you chose wrong command!")

    answer = input("Tell me if you want to continue: yes or no?")
    if answer == "yes":
        user = int(input("Choose paper-1, scissors-2, stone-3"))
    else:
        print("Sorry to see you go...")
        break
