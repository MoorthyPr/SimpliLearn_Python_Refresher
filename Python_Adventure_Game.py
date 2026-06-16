

def start_game():

    print("\nChoose your path:")
    print("1. 🌲 The Dark Forest")
    print("2. 🪨 The Hidden Cave")

    player_answer = input("Enter your choice (1 or 2): ")

    if player_answer == "1":
        print(f"You have chosen the Dark Forest!")
        print("The dark mystery awaits you... Don't wake the sleeping beasts!")
        forest_adventure()
    elif player_answer == "2":
        print(f"Your have chosen the Hidden Cave!")
        print("The ancient secrets await you... Be cautious of the hidden dangers!")
        cave_adventure()
    else:
        print(f"{player_answer}, player decided to take rest")
        return


def cave_adventure():
    print("="*50)
    print("Your journey into the Hidden Cave begins... Make wise choices!")
    print("="*50)
    print("\nWhat will you do next?")
    print("1. Move forward")
    print("2. Light a torch")
    print("3. Turn back")

    cave_answer1 = input("Enter your choice (1, 2, or 3): ")

    if cave_answer1 == "1":
        print("You fell into a pit and got injured! Now you must find a way out.")
        print("\nWhat will you do next?")
        print("1. Climb out using the rope")
        print("2. Dig a tunnel")
        cave_answer2 = input("Enter your choice (1 or 2): ")

        if cave_answer2 == "1":
            print("You successfully climb out of the pit!")
            print("\nYou see 3 doors in front of you. Choose wisely!")
            print("1. Open the first door")
            print("2. Open the second door")
            print("3. Open the third door")
            cave_answer3 = input("Enter your choice (1, 2, or 3): ")
            if cave_answer3 == "1":
                print("You open the first door and find a treasure! You win!")
                return
            elif cave_answer3 == "2":
                print("You open the second door and find a trap! Game over!")
                return
            elif cave_answer3 == "3":
                print("You open the third door and find a monster! Game over!")
                return
            else:
                print(f"You made a wrong choice, Game over!")
                return
        elif cave_answer2 == "2":
            print("You dig a tunnel and encountered a snake! Game over!")
            return
        else:
            print(f"You made a wrong choice, Game over!")
            return

    elif cave_answer1 == "2":
        print("You light a torch and see the cave more clearly , there is pit in front of you and a button on the wall.")
        print("\nWhat will you do next?")
        print("1. Use the rope to cross the pit")
        print("2. press the button")
        cave_answer4 = input("Enter your choice (1 or 2): ")

        if cave_answer4 == "1":
            print("You crossed the pit!")
            print("\nYou see 3 doors in front of you. Choose wisely!")
            print("1. Open the first door")
            print("2. Open the second door")
            print("3. Open the third door")
            cave_answer5 = input("Enter your choice (1, 2, or 3): ")
            if cave_answer5 == "1":
                print("You open the first door and find a treasure! You win!")
                return
            elif cave_answer5 == "2":
                print("You open the second door and find a trap! Game over!")
                return
            elif cave_answer5 == "3":
                print("You open the third door and find a monster! Game over!")
                return
            else:
                print(f"You made a wrong choice, Game over!")
                return
        elif cave_answer4 == "2":
            print("You pressed the button and the floor collapsed! Game over!")
            return
        else:
            print(f"You made a wrong choice, Game over!")
            return
    elif cave_answer1 == "3":
        print("\nYou decide to turn back and leave the cave.")
        return
    else:
        print(f"PLayer decided to take rest")
        return
    
def forest_adventure():
    print("="*50)
    print("Your journey into the Dark Forest begins... Make wise choices!")
    print("="*50)
    print("\nWhat will you do next?")
    print("1. Take a boat and cross the river")
    print("2. Climb the tree")
    print("3. Turn back")

    forest_answer1 = input("Enter your choice (1, 2, or 3): ")

    if forest_answer1 == "1":
        print("You hit a rock and boat is sinking.")
        print("\nWhat will you do next?")
        print("1. Row fast and try to reach the shore")
        print("2. Jump into the water and swim to the shore")
        forest_answer2 = input("Enter your choice (1 or 2): ")

        if forest_answer2 == "1":
            print("You successfully reached the shore!")
            print("\nYou see 3 paths in front of you. Choose wisely!")
            print("1. Choose the left side path")
            print("2. Choose the middle path")
            print("3. Choose the right side path")
            forest_answer3 = input("Enter your choice (1, 2, or 3): ")
            if forest_answer3 == "1":
                print("You choose the left side path and find a lion! Game over!")
                return
            elif forest_answer3 == "2":
                print("You choose the middle path and find a tiger! Game over!")
                return
            elif forest_answer3 == "3":
                print("You choose the right side path and find a treasure! You win!")
                return
            else:
                print(f"You made a wrong choice, Game over!")
                return
        elif forest_answer2 == "2":
            print("You jumped into the water and encountered a crocodile! Game over!")
            return
        else:
            print(f"You made a wrong choice, Game over!")
            return

    elif forest_answer1 == "2":
        print("You Climb the tree, there is a rope to cross the river and a treasure box on top of the tree.")
        print("\nWhat will you do next?")
        print("1. Use the rope to cross the river")
        print("2. Touch the treasure box")
        forest_answer4 = input("Enter your choice (1 or 2): ")

        if forest_answer4 == "1":
            print("\nYou see 3 paths in front of you. Choose wisely!")
            print("1. Choose the left side path")
            print("2. Choose the middle path")
            print("3. Choose the right side path")
            forest_answer5 = input("Enter your choice (1, 2, or 3): ")
            if forest_answer5 == "1":
                print("You choose the left side path and find a lion! Game over!")
                return
            elif forest_answer5 == "2":
                print("You choose the middle path and find a tiger! Game over!")
                return
            elif forest_answer5 == "3":
                print("You choose the right side path and find a treasure! You win!")
                return
            else:
                print(f"You made a wrong choice, Game over!")
                return
        elif forest_answer4 == "2":
            print("You touched the treasue box and lightning struck! Game over!")
            return
        else:
            print(f"You made a wrong choice, Game over!")
            return
    elif forest_answer1 == "3":
        print("\nYou decide to turn back and leave the forest.")
        return
    else:
        print(f"PLayer decided to take rest")
        return



start_your_game = True

while start_your_game:
    print("="*50)
    print("\nAre you ready for the adventure?")
    print("="*50)

    player_answer = input("Enter your name to begin the journey: ")


    print(f"\nWelcome, {player_answer}, to the Land of Mysteries!")
    print("="*50)

    start_game()
    print("\nThanks for playing!")
    print("="*50)
    print("\nDo you want to play again?")
    play_again = input("Enter 'yes' to play again or 'no' to quit: ")
    if play_again.lower() != "yes":
        start_your_game = False



