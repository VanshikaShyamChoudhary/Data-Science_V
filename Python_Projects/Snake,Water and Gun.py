# The Basic Rules
# Snake vs. Water: Snake wins because it drinks the water.
# Water vs. Gun: Water wins because the gun is submerged in it.
# Gun vs. Snake: Gun wins because it defeats the snake.
# Tie: If both players pick the same item, the round is a draw.

import random

choose=["Snake","Water", "Gun"]
opponent = random.choice(choose)


print("\nSNAKE, WATER AND GUN GAMEEEEEEE!!!!!!!!")
print("Let's Play\n")

print("You have 3 choices : ")
print("Snake\n"
      "Water\n"
      "Gun\n")

print("Now Choose : ")

user_1=input()
print(user_1)
print("\nThe choice of opponent is : ",opponent)


if user_1== "Snake"  and  opponent=="Snake":
    print("It's a tie 🤪\n Try nexxt timeeeeee🤗")
elif  user_1=="Snake" and opponent=="Water": 
    print("YOU WIN 🥳\n Cz snake will dive in water💧")  
elif  user_1=="Snake" and opponent=="Gun": 
    print("YOU Lost 😔 \n Cz snake  would be shot by the Gun 💥\n Try nexxt timeeeeee🤗") 




elif user_1== "Gun"  and  opponent=="Gun":
    print("It's a tie 🤪\n Try nexxt timeeeeee🤗")
elif user_1== "Gun"  and  opponent=="Water":
    print("You loose 🫢 \nCz gun will drowned the water \n Try nexxt timeeeeee🤗")
elif user_1== "Gun"  and  opponent=="Snake":
    print("You win 🥳")




elif user_1== "Water"  and  opponent=="Water":
    print("It's a tie 🤪\n Try nexxt timeeeeee🤗")
elif user_1== "Water"  and  opponent=="Snake":
    print("You loose 🫢\n Cz Snake will Swwwwiiiimmmmmmmmmm in waterrrr \n Try nexxt timeeeeee🤗")
elif user_1== "Water"  and  opponent=="Gun":
    print("You Win 🤩")



    

