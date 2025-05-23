import random

health = 100
attack = 1
enemy1hp = 10
enemy2hp = 20
randomAtk = random.randint(5, 30)
superBlock = 30
sword = 10
dagger = 5
greatsword = 15
block = 10

print("Hello! Welcome to my first python project, it's basically a little RPG game where you have 2 enemies to defeat and a powerup after defeating each one!, have fun!!!\n")

name = input("So, let's get started! What is your name?: ")
weapon_Prompt = int(input(("Welcome, " + name + "!\nWhat do you want your weapon to be? \n\t1) Dagger \n\t2) Sword \n\t3) Greatsword\n")))

if weapon_Prompt == 1:
    print("Your first choice is a dagger! It has 5 attack damage and your first enemy has 10 health!\n")
    attack_Prompt = int(input("Which attack do you want to use? \n\t1) Attack \n\t2) Block\n"))
    
    if attack_Prompt == 1:
        enemy1hp -= dagger
        if enemy1hp <= 0:
            print("You have slain the first boss!")
        else:
            health -= 20
            print("You didn't kill him! Your health is now", health)
            while enemy1hp > 0:
                try_Again1 = int(input("Would you like to attack again? \n\t1) Yes \n\t2) No\n"))
                if try_Again1 == 1:
                    enemy1hp -= dagger
                    if enemy1hp <= 0:
                        print("You have slain the first boss!")
                        break
                    health -= 20
                    print("Still alive! Your health is now", health)
                    if health <= 0:
                        print("Wow you really lost -_-")
                        exit()
                else:
                    print("You suck")
                    exit()
    else:
        print("Don't block again")
        exit()

    # POWER-UP SECTION (AFTER FIRST BOSS)
    power_Up1 = int(input("Choose your powerup: \n\t1) Random Attack Damage \n\t2) Super Block for 1 Turn \n\t3) Heal for 20 health\n"))

    if power_Up1 == 3:
        health += 20
        print("You healed! Health is now", health)

    print("Your new enemy appears!")

    while enemy2hp > 0:
        power_Input = int(input("What do you want to do? \n\t1) Use Random Attack \n\t2) Attack \n\t3) Block\n"))
        if power_Input == 1:
            enemy2hp -= randomAtk
            print(f"You did {randomAtk} damage!")
        elif power_Input == 2:
            enemy2hp -= dagger
            print("You did 5 damage.")
        else:
            print("Don't block buddy")
            exit()

        if enemy2hp <= 0:
            print("You have beaten the final boss!")
            break
        else:
            health -= 40
            print(f"Enemy attacks! Your health is now {health}")
            if health <= 0:
                print("You lost -_-")
                exit()
