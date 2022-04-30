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


first_step = input("which wy would you like to ? Left or Right")
first_step_low = first_step.lower()
if (first_step_low == "left"):
  print("You made it safely and now there is lake in front of you")
  second_step = input("Now do you want to swim or wait ?")
  second_step_low = second_step.lower()
  if(second_step_low == "wait"):
    print("a random door appears in front of you")
    third_try = input("which door do you want to open? RED OR BLUE OR YELLOW")
    third_try_low = third_try.lower()
    if(third_try_low == "blue" ):
        print("You were Eaten by beasts! GAME OVER")
    elif(third_try_low == "red"):
        print("You were burned by fire! GAME OVER")
    elif(third_try_low == "yellow"):
        print("YAY you found the treasure!! YOU WIN")  
    else:
        print("wrong choice! GAME OVER")       


  else:
    print("You got attacked by a trout! GAME OVER")
      
else:
  print("You fell into a hole, GAME OVER")