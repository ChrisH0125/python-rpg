import random


health = 100
attack = 1
enemy1hp = 10
enemy2hp = 20
randomAtk = random.randint(5,30)
superBlock = 30
sword = 10
dagger = 5
greatsword = 15
block = 10
print("Hello! Welcome to my first python project, it's basically a little RPG game where you have 2 enemies to defeat and a powerup after defeating each one!, have fun!!!\n")

name = input("So, let's get started! What is your name?: ")
weapon_Prompt = int(input(("Welcome," + name + "!\n What do you want your weapon to be? \n\t1) Dagger \n\t2) Sword \n\t3) Greatsword\n")))

if weapon_Prompt == 1:
    print("Your first choice is a dagger! It has 5 attack damage and your first enemy has 10 health!\n")
    attack_Prompt = int(input("Which attack do you want to use? \n\t1) Attack \n\t Block"))
    if(attack_Prompt == 1):
        enemy1hp -= dagger
        while enemy1hp != 0:
            health -= 20
            try_Again1 = int(input("You didn't kill him my brotha, now your health is 80, would you wanna attack again? \n\t1) Yes \n\t2) No"))
            if try_Again1 == 1:
                enemy1hp -=dagger
            else:
                print("You suck")

        
