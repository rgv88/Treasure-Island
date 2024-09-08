choice1 = input('Welcome to Treasure Island.\n Your mission is to find the treasure.\n You\'re on a cross road. Where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake.'
                    'There is an island in the middle of the lake.'
                    'Type "wait" to wait for the boat.'
                    'Type "swim" to swim accross.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed.\n There is a house with 3 doors. One yellow, one red and one blue.\n Which colour do you choose?\n".lower())
        if choice3 == "yellow":
            print("You found the treasure. You win.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif choice3 == "red":
            print("Burned by fire. Game Over.")
        else:
            print("You chose a door that does not exist. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
        
else:
    print("Fall into a hole. Game Over.")
