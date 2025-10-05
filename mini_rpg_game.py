import random

player = 100
enemy = 100

while player > 0 and enemy > 0:
    move = input("(a = Attack, h = Heal): ")

    if move == "a":
        enemy -= random.randint(10, 30)
    elif move == "h":
        player = min(100, player + random.randint(10, 25)) 

    if enemy <= 0:
        print("You win!") 
        break

    player -= random.randint(10, 35)

    if player <= 0:
        print("You lose!")
        break

    print(f"Your HP: {player}, Enemy HP: {enemy}")     