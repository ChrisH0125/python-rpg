import random


health = 100
attack = 1
enemy1hp = 10
enemy2hp = 20
enemy3hp = 50
enemy4hp = 70
enemy5hp = 100
randomAtk = random.randInt(5,30)
superBlock = 30
heal = health+=20
sword = 10
dagger = 5
greatsword = 15
block = 10
print("Hello! Welcome to my first python project, it's basically a little RPG game where you have 3 enemies to defeat and a powerup after defeating each one!, have fun!!!\n")

name = input("So, let's get started! What is your name?: ")
weapon_Prompt = int(input(("Welcome," + name + "!\n What do you want your weapon to be? \n\t1) Dagger \n\t2) Sword \n\t3) Greatsword\n")))

if weapon_Prompt == 1:
    print("Your first choice is a dagger! It has 5 attack damage and your first enemy has 10 health!\n")
    attack_Prompt = int(input("Which attack do you want to use? \n\t1) Attack \n\t Block"))
    if(attack_Prompt == 1):
        enemy1hp -= dagger
        if(enemy1hp == 0):
            power_Up1 = int(input("You have slain the first boss! What would you like to be your powerup? \n\t1) Random Attack Damage \n\t Super Block for 1 Turn \n\t Heal for 20 health\n"))
        
