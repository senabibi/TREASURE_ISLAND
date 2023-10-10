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
first_choice=input("You have come to the bend, which way do you want to proceed? Right or left?").lower()

if first_choice=="left":
  second_choice=input("The bridge has collapsed, but you feel that you are short of treasure. Will you wait or will you swim across?").lower()
  if second_choice=="wait":
    third_choice=input("It's almost time! There are three doors and a dark road in front of you. One of them is blue, one is red, one is green. Will you choose one of the doors, or will you take a risk and choose the road?").lower()
    if third_choice=="red":
      print("It's a room full of fire.\nGame Over.🔥")
    elif third_choice=="yellow":
      print("You found the treasure!✨\nYou Win!💎")
    elif third_choice=="blue":
      print("You enter a room of beasts.\n Game Over.⚰️👻")
    else:
      print("You've attacked by an angry bird.\nGame Over.💀👾")
  

  
  
