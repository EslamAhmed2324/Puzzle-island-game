print("""welcome to my island
there are three doors in front of you
a red door and green door and blue door
you have to choose one""")

door_choice = input("which door do you want to open \n").lower()
if door_choice == "green":
    print("you choosed the wrong door, you lose")
elif door_choice == "blue":
    print("you lose")
elif door_choice == "red":
    print("you win the first round, now choose one of the boxex red , green , blue")
    
    box = input("choose one box \n").lower()
    if box == "red":
        print("congrats! you win the game and got 20k coins")
    elif box == "green":
        print("you found a box filled of snicks, lose")
    elif box == "blue":
        print("oops! you choosed the wrong box, lose")
    else:
        print("invalid choice")
        
else: 
  print("invalid choice")