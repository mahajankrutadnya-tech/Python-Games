# #Rock Paper Scissor

import random
print("=== Rock Paper Scissor ===")
choices=["rock","paper","scissor"]

userchoice=input("Enter the rock,paper or scissor:")

computer=random.choice(choices)
print("computer :",computer)

if computer==userchoice:
    print("Result : Draw")
elif computer=="scissor" and userchoice=="rock":
    print("You win!!!")
elif computer=="rock" and userchoice=="paper":
    print("You win!!!")
elif computer=="paper" and userchoice=="scissor":
    print("You win!!!")
else:
    print("computer win!!! and You lose...")


#Guess the number

import random
target_no=random.randint(1,100)

while True:
    userNo=input("Enter a target no or Quit(Q)=")
    if(userNo=="Q"):
     break
    userNo=int(userNo)

    if userNo==target_no:
       print("Yes you guess successfully!!!")

    elif userNo>target_no:
       print("You guess too big...try again and guess another smaller number...")

    else:
       print("You guess too small...try again and guess another bigger number...")
    

print("----Game Over----")

