import random
def check_validity(input, valid_set):
    if input.lower() in valid_set:
        return True
    else:
        return False
def input_choice(valid_set):
    choice = input("Your choice: ")
    if check_validity(choice, valid_set):
        return choice.lower()
    else:
        print("Please choose a valid option")
        return input_choice(valid_set)

## plot 0 : Beginning
## plot 1 : Monument 1 Beginning
## plot 2 : Post T-Rex story
## plot 3 : Cave entry
    ## plot 3.1 : Cave left
        ## plot 3.11 : Cave ending
    ## plot 3.2 : Cave right
## plot 4 : End Cave with EGG
## plot 5 : End cave without EGG

## plot 100 : Death "Opponent was too strong"

class Player:
    def __init__(self,player_name):
        self.player_name=player_name

    def change_name(self,name):
        self.player_name=name

    def get_player_name(self):
        return self.player_name

hero=Player("placeholder")

def storyline(plot):
    global weapon
    class weapon:
        def __init__(self, weapon_name, min_damage, max_damage):
            self.weapon_name = weapon_name
            self.max_damage = max_damage
            self.min_damage = min_damage

    global beasts
    class beasts:
        def __init__(self, beast_name, beast_description,beast_min_attack, beast_max_attack):
            self.beast_name = beast_name
            self.beast_description = beast_description
            self.beast_min_attack = beast_min_attack
            self.beast_max_attack = beast_max_attack
    T_REX = beasts("T-REX" , "King of Tyrant Lizards" , 150 , 250)
    Beast_1 = beasts("Sabretooth" , "Mean Cat with banger fangs" , 20 , 30)
    Beast_2 = beasts("Black Bear" , "Black furry angry mama" , 30 , 40)
    Beast_3 = beasts("Rabid Dog" , "Cross eyed salivating satan spawn" , 5 , 10)

    Beast_grunts = [Beast_1 , Beast_2 , Beast_3]




    global fight
    def fight(monster):
        print("You encounter {}".format(monster.beast_name))
        print("{}".format(monster.beast_description))
        beast_attack = random.randint(monster.beast_min_attack, monster.beast_max_attack)
        user_attack = random.randint(current_weapon.min_damage , current_weapon.max_damage)
        print("{} attacks. Deals {} damage".format(monster.beast_name, beast_attack))

        print("You attack. Deal {} damage".format(user_attack))

        if beast_attack >= user_attack:
            return 100
        else:
            print("You have defeated the {}".format(monster.beast_name))
            if monster == T_REX:
                return 2
            elif monster == enemy1:
                return 3.11


    if plot == "map":
        print("Where do you wish to go")

    if plot == 0:
        print("Welcome to Altos. My name is Professor Shah")
        print("Here, humans and beasts live in harmony, however, recently some beasts are going rogue")
        print("Before we embark on your adventure, what shall i call you?")
        global name
        input_name = input("My name is ")
        hero.change_name(input_name[0].upper() + input_name[1:].lower())
        print("Ah, nice to meet you " + hero.get_player_name())
        print("I hope to see you at my office soon.")
        print("Hello " + hero.get_player_name() + ". Now that you've settled, its time for your adventure.")
        print("Here, i have the following weapons for you to choose from.")
        print("As you progress, you will find stronger weapons to fight stronger beasts.")
        print("Which of these do you want? Pick only one")
        print("Press 1 for the LARGE AXE")
        print("Press 2 for the 2 HANDED LONG SWORD")
        print("Press 3 for the DOUBLE MACE")

        A = input_choice(["1", "2", "3"])
        global current_weapon
        if A == "1":
            AXE = weapon("AXE", 30, 70)
            print("You have chosen: {}".format(AXE.weapon_name))
            current_weapon = AXE
        elif A == "2":
            SWORD = weapon("SWORD",50,90)
            print("You have chosen: {}".format(SWORD.weapon_name))
            current_weapon = SWORD
        elif A == "3":
            MACE = weapon("MACE",25,55)
            print("You have chosen: {}".format(MACE.weapon_name))
            current_weapon = MACE
        print("You have obtained the {}".format(current_weapon.weapon_name))
        print("Ah, so you have chosen the " + current_weapon.weapon_name + ". Fantastic choice. Now you may leave to save the world")
        print("Are you ready to start your adventure and go to your first destination?")
        print("Press 1 for yes")
        print("Press 2 for no")
        if input_choice(["1" , "2"]) == "1":
            return 1
        else:
            print("Whenever you are ready, press '1'")
            yes = input()
            return 1

    elif plot == 1:
        print("Alright, lets now go to Monument 1")
        print("You hear a loud roar. Best go check it out")
        print("You encounter a T-REX eating the flesh of a dead TRICERATOPS")
        print("The T-REX seems to be above your current skill rating. What do you wanna do?")
        print("Press 1 to fight")
        print("Press 2 to run away")
        if input_choice(["1", "2"]) == "1":
            return fight(T_REX)
        else:
            print("You run away from the beast")
            return 2

    elif plot == 2:
        print("You move on")
        print("You see a cave in front of you")
        print("Do you wish to enter the cave?")
        print("Press 1 for yes")
        print("Press 2 for no")
        if input_choice(["1", "2"]) == "1":
            return 3
        else:
            print("Whenever you are ready, press '1'")
            yes = input()
            return 3

    elif plot == 3:
        print("The cave is dark but there is a path illuminated by lit torches")
        print("You continue to walk forward")
        print("You see two new paths. One leading to the left and the other to the right")
        print("Which path do you wish to take? ")
        print("Press 1 to go left")
        print("Press 2 to go right")
        if input_choice(["1", "2"]) == "1":
            return 3.1
        else:
            return 3.2

    elif plot == 3.1:
        print("You go through the left path. You see something moving.")
        print("You keep moving forward.")
        enemy1 = random.choice(Beast_grunts)
        print("You are jumped by a {}".format(enemy1.beast_name))
        print("Do you wish to fight the beast?")
        print("Press 1 fight")
        print("Press 2 to run away")
        if input_choice(["1", "2"]) == "1":
            return fight(enemy1)
        else:
            print("You try to run past but the {} stops you".format(enemy1.beast_name))
            input()
            print("You have no choice but to fight")
            return fight(enemy1)

    elif plot == 3.11:
        print("You keep walking and reach the end of the cave")
        return 5

    elif plot == 3.2:
        print("You chose the right path and keep walking forward")
        print("You see a lever in the distance, illuminated by light coming from a hole in the ceiling")
        print("Do you want to pull the lever or keep walking?")
        print("Press 1 for yes")
        print("Press 2 for no")
        if input_choice(["1", "2"]) == "1":
            print("You hear the sound of a large wall moving somewhere in the distance. You keep walking forward")
            return 3.21
        else:
            print("You ignore the lever and keep walking forward")
            return 3.22

    elif plot == 3.22:
        print("You see two paths infront of you, but the one on the left seems to be closed")
        print("You go right")
        print("You keep walking forward and reach the end of the cave")
        return 5

    elif plot == 3.21:
        print("You see two paths infront of you. The one on the left seems to be the one you just opened")
        print("Which door do you wish to go through?")
        print("Press 1 for left path")
        print("Press 2 for right path")
        if input_choice(["1", "2"]) == "1":
            print("You see a nest with an egg in it")
            print("They look like T-Rex EGGS")
            print("What do you want to do?")
            print("Press 1 to take the EGG")
            print("Press 2 to ignore it and keep walking")
            if input_choice(["1", "2"]) == "1":
                print("You take the egg and keep in in your bag")

                print("You keep walking forward and reach the end of the cave")
                return 4
            else:
                print("You keep walking forward and reach the end of the cave")
                return 5
        else:
            print("You keep walking forward and reach the end of the cave")
            return 5
    elif plot == 5:
        print("You exit the cave to see a garden with a river flowing through the middle")
        print("The river is coming from a small waterfall")
        print("You can see bright colours behind the waterfall")
        print("You proceed to the WATERFALL to inspect what's behind it")
        print("It looks like you need to jump to cross. Looks like you got a 67% chance of making the jump")
        print("Do you want to jump or look for another way in?")
        print('Press 1 to jump')
        print("press 2 to look for an alternate route")
        if input_choice(["1", "2"]) == "1":
            jump_result = random.choice(["1", "2", "3" , "4" , "5"])
            if jump_result in ["1", "2", "3", "4", "5"]:
                return 5.1
            else:
                return 101
    elif plot == 5.1:
        print("You made the jump")
        print("You see a lab, almost completely destroyed. It looks like some sort of large beast came and attacked the lab")
        print("You decide to inspect the lab")
        print("You see a JOURNAL, a POD with wires inside, and a unlocked TRUNK")
        print("Press 1 to inspect the JOURNAL")
        print("Press 2 to inspect the POD")
        print("Press 3 to inspect the TRUNK")
        a =  input_choice(["1", "2" , "3"])
        if a == "1":
            print("Most of the pages are torn off. Looks like the beast wasn't alone.")
            print("Press 2 to inspect the POD")
            print("Press 3 to inspect the TRUNK")
            if input_choice(["2" , "3"]) == "2":
                print("It looks like someone was experimenting on some beast inside this pod")
                print("The beast was probably taken by the raiders")
                print("Press 3 to inspect the TRUNK")
                if input_choice(["3"]) =="3":
                    print("You find LARGE JACKHAMMER")
                    jackhammer = weapon("JACK HAMMER" , 50, 100)
                    print("Do you want to replace your weapon?")
                    print("{} attack stat: {}".format(current_weapon.weapon_name, (current_weapon.max_damage + current_weapon.min_damage)/2))
                    print("JACK HAMMER attack stat: {}".format((jackhammer.max_damage + jackhammer.min_damage)/2))
                    print("Press 1 to replace weapon")
                    print("Press 2 to keep weapon")
                    if input_choice(["1", "2"])== "1" :
                        current_weapon = jackhammer
                    else:
                        current_weapon = current_weapon
            else:
                print("You find LARGE JACKHAMMER")
                jackhammer = weapon("JACK HAMMER", 50, 100)
                print("Do you want to replace your weapon?")
                print("{} attack stat: {}".format(current_weapon.weapon_name, (current_weapon.max_damage + current_weapon.min_damage) / 2))
                print("JACK HAMMER attack stat: {}".format((jackhammer.max_damage + jackhammer.min_damage) / 2))
                print("Press 1 to replace weapon")
                print("Press 2 to keep weapon")
                if input_choice(["1", "2"]) == "1":
                    current_weapon = jackhammer
                else:
                    current_weapon = current_weapon
                print("Press 2 to inspect the POD")
                if input_choice(["2"]) == "2":
                    print("It looks like someone was experimenting on some beast inside this pod")
                    print("The beast was probably taken by the raiders")
            return 6

        elif a == "2":
            print("It looks like someone was experimenting on some beast inside this pod")
            print("The beast was probably taken by the raiders")
            print("Press 1 to inspect the JOURNAL")
            print("Press 3 to inspect the TRUNK")
            if input_choice(["1", "3"]) == "1":
                print("Most of the pages are torn off. Looks like the beast wasn't alone.")
                print("Press 3 to inspect the TRUNK")
                if input_choice(["3"]) == "3":
                    print("You find LARGE JACKHAMMER")
                    jackhammer = weapon("JACK HAMMER", 50, 100)
                    print("Do you want to replace your weapon?")
                    print("{} attack stat: {}".format(current_weapon.weapon_name, (current_weapon.max_damage + current_weapon.min_damage) / 2))
                    print("JACK HAMMER attack stat: {}".format((jackhammer.max_damage + jackhammer.min_damage) / 2))
                    print("Press 1 to replace weapon")
                    print("Press 2 to keep weapon")
                    if input_choice(["1", "2"]) == "1":
                        current_weapon = jackhammer
                    else:
                        current_weapon = current_weapon
            else:
                print("You find LARGE JACKHAMMER")
                jackhammer = weapon("JACK HAMMER", 50, 100)
                print("Do you want to replace your weapon?")
                print("{} attack stat: {}".format(current_weapon.weapon_name, (current_weapon.max_damage + current_weapon.min_damage) / 2))
                print("JACK HAMMER attack stat: {}".format((jackhammer.max_damage + jackhammer.min_damage) / 2))
                print("Press 1 to replace weapon")
                print("Press 2 to keep weapon")
                if input_choice(["1", "2"]) == "1":
                    current_weapon = jackhammer
                else:
                    current_weapon = current_weapon
                print("Press 1 to inspect the JOURNAL")
                if input_choice(["1"]) == "1":
                    print("Most of the pages are torn off. Looks like the beast wasn't alone.")
            return 6


        elif a == "3":
            print("You find LARGE JACKHAMMER")
            jackhammer = weapon("JACK HAMMER", 50, 100)
            print("Do you want to replace your weapon?")
            print("{} attack stat: {}".format(current_weapon.weapon_name, (current_weapon.max_damage + current_weapon.min_damage) / 2))
            print("JACK HAMMER attack stat: {}".format((jackhammer.max_damage + jackhammer.min_damage) / 2))
            print("Press 1 to replace weapon")
            print("Press 2 to keep weapon")
            if input_choice(["1", "2"]) == "1":
                current_weapon = jackhammer
            else:
                current_weapon = current_weapon
            print("Press 1 to inspect the JOURNAL")
            print("Press 2 to inspect the POD")
            if input_choice(["1", "2"]) == "1":
                print("Most of the pages are torn off. Looks like the beast wasn't alone.")
                print("Press 2 to inspect the POD")
                if input_choice(["2"]) == "2":
                    print("It looks like someone was experimenting on some beast inside this pod")
                    print("The beast was probably taken by the raiders")
            else:
                print("It looks like someone was experimenting on some beast inside this pod")
                print("The beast was probably taken by the raiders")
                print("Press 1 to inspect the JOURNAL")
                if input_choice(["1"]) == "1":
                    print("Most of the pages are torn off. Looks like the beast wasn't alone.")
            return 6
    elif plot == 6:
        print("You leave the waterfall")
    elif plot == 100:
        print("You draw your {} and engage in battle".format(current_weapon.weapon_name))
        input()
        print("Opponent was too strong and kills you")
        input()
        print("GAME OVER")
        print("TIP: Try not to engage with high level enemies until you become strong")
        print("Do you wish to play again?")
        print("Press 1 for yes")
        print("press 2 for no")
        if input_choice(["1" , "2"]) == "1":
            return 0
        else:
            return "end"
    elif plot == 101:
        print("You fell down and died")
        input()
        print("GAME OVER")





def main():
    ## test from which storyline to start from
    x = 0
    while True:
        ## checking plot
        print("plot: " + str(x))
        input()
        x = storyline(x)
        if x == "end":
            break




main()
