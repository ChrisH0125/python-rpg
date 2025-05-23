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
weapon_Prompt = int(input(("Welcome, " + name + "!\n What do you want your weapon to be? \n\t1) Dagger \n\t2) Sword \n\t3) Greatsword\n")))

if weapon_Prompt == 1:
    print("Your first choice is a dagger! It has 5 attack damage and your first enemy has 10 health!\n")
    attack_Prompt = int(input("Which attack do you want to use? \n\t1) Attack \n\t2) Block\n"))
    if(attack_Prompt == 1):
        enemy1hp -= dagger
        while enemy1hp != 0:
            health -= 20
            try_Again1 = int(input("You didn't kill him my brotha, now your health is 80, would you wanna attack again? \n\t1) Yes \n\t2) No\n"))
            if try_Again1 == 1:
                enemy1hp -=dagger
            else:
                print("You suck")
                exit()
    else:
        print("Why are you blocking loser")
        exit()
        power_Up1 = int(input("You have slain the first boss! What would you like to be your powerup? \n\t1) Random Attack Damage \n\t2) Super Block for 1 Turn \n\t3) Heal for 20 health\n"))
        if power_Up1 == 1:
            power_Input = int(input("You have chosen random attack damage! Your new enemy appears before you, what do you want to do? \n\t1) Use Random Attack \n\t2) Attack \n\t3) Block"))
            while enemy2hp !=0:
                if power_Input == 1:
                    enemy2hp -= randomAtk
                    health -=40
                elif power_Input == 2:
                    enemy2hp -= dagger
                    health -=40
                else:
                    print("Don't block buddy")
                    exit()
            print("You have beaten the boss!")


if health == 0:
    print("Wow you really lost -_-")
    exit()

        
