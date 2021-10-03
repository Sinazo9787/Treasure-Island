print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice=input("You are walking and come to a crossroads.Choose 'left'or 'right'.\n")
if choice =='left' :
  print("You were taken to the base of the mountain, near the treasure.")
  choice2=input("As you are hiking up the mountain,you see a clue but it is across the river.Are you waiting for a boat or swimming across.Type 'wait'or 'swim'.\n")
  if choice2 == 'wait':
    print("While you were waiting you were bitten by a Banana Spider and died.Game over")
  elif choice2 == 'swim':
    print("You arrived safely to the otherside and the clue took you to a cave.")
    choice3=input("You have reached the cave but there are 2 doors.Which door are you picking.Type '1' or '2'.\n")
    if choice3 == '1':
      print("You have found the treasure.You win.")
    elif choice3 == '2':
      print("You met a Neandethal and you were beaten to death.Game over")
elif choice == 'right':
  print("You drank from a saltwater source and died of dehydration.Game over.")
