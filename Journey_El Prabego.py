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


## for the time being jump is 100% guaranteed

## plot 6 : Leave waterfall with EGG
## plot 7 : Leave waterfall without EGG
## plot 8 : Post T-Rex 2 encounter (common with / without egg)
## plot 8.1 : Monster Hunter Arena
## plot 9 : Last Puzzle

## plot 100 : Death "Opponent was too strong"

def storyline(plot):
    global weapon

    class weapon:
        def __init__(self, weapon_name, min_damage, max_damage):
            self.weapon_name = weapon_name
            self.max_damage = max_damage
            self.min_damage = min_damage

    global beasts

    class beasts:
        def __init__(self, beast_name, beast_description, beast_min_attack, beast_max_attack):
            self.beast_name = beast_name
            self.beast_description = beast_description
            self.beast_min_attack = beast_min_attack
            self.beast_max_attack = beast_max_attack

    T_REX = beasts("T-REX", "King of Tyrant Lizards", 150, 250)
    T_REX2 = beasts("T-REX", "King of Tyrant Lizards", 150, 250)
    Beast_1 = beasts("Monica", "If stares could kill, you'd already be dead", 20, 30)
    Beast_2 = beasts("Ameya", "Has definitely bitched about the horrible balancing on this game", 30, 40)
    Beast_3 = beasts("Vignesh", "Channelled all his stamina into his vocal chords", 5, 10)

    Beast_grunts = [Beast_1, Beast_2, Beast_3]
    ArenaFoe1 = beasts("P.S Anil Kumar", "Don't let his sweet demeanor trick you", 50, 150)
    ArenaFoe2 = beasts("Sambudha Mishra", "The sexy meteorologist", 50, 150)
    ArenaFoe3 = beasts("Vidhi Sinha", "Probably louder than a T-REX", 50, 150)

    global fight

    def fight(monster):
        print("You encounter {}".format(monster.beast_name))
        input()
        print("{}".format(monster.beast_description))
        input()
        beast_attack = random.randint(monster.beast_min_attack, monster.beast_max_attack)
        user_attack = random.randint(current_weapon.min_damage, current_weapon.max_damage)
        print("{} attacks. Deals {} damage".format(monster.beast_name, beast_attack))
        input()

        print("You attack. Deal {} damage".format(user_attack))
        input()

        if beast_attack >= user_attack:
            Foes = [ArenaFoe1, ArenaFoe2, ArenaFoe3]
            if monster in Foes:
                print("You have been defeated")
                input()
                print("Better luck next time")
                return 8.2
            else:
                print()
                return 100
        else:
            print("You have defeated {}".format(monster.beast_name))
            input()
            Foes = [ArenaFoe1, ArenaFoe2, ArenaFoe3]
            if monster == T_REX:
                return 2
            elif monster in Foes:
                print("Good job")
                return 8.2
            elif monster == enemy1:
                return 3.11

    if plot == 0:
        print("Welcome to Pravega. My name is Publicity Co-ordinator R.Shah")
        input()
        print("Here, humans and monsters live in harmony, however, recently some monsters have been going rogue")
        input()
        print("Before we embark on your adventure, what shall i call you?")
        global name
        input_name = input("My name is ")
        name = input_name[0].upper() + input_name[1:].lower()
        print("Ah, nice to meet you " + name)
        input()
        print("I hope to see you at my office soon.")
        input()
        print("Hello " + name + ". Now that you've settled, its time for your adventure.")
        input()
        print("Here, i have the following weapons for you to choose from.")
        input()
        print("As you progress, you will find stronger weapons to fight stronger beasts.")
        input()
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
            SWORD = weapon("SWORD", 50, 90)
            print("You have chosen: {}".format(SWORD.weapon_name))
            current_weapon = SWORD
        elif A == "3":
            MACE = weapon("MACE", 25, 55)
            print("You have chosen: {}".format(MACE.weapon_name))
            current_weapon = MACE
        print("You have obtained the {}".format(current_weapon.weapon_name))
        print("Ah, so you have chosen the " + current_weapon.weapon_name + ". Fantastic choice. Now you may leave to save the world")
        input()
        print("Are you ready to start your adventure and go to your first destination?")
        print("Press 1 for yes")
        print("Press 2 for no")
        if input_choice(["1", "2"]) == "1":
            return 1
        else:
            print("Whenever you are ready, press '1'")
            yes = input()
            return 1

    elif plot == 1:
        print("Alright, lets now go to Main Building")
        input()
        print("You hear a loud roar. Best go check it out")
        input()
        print("You encounter an AIRBUS 747 eating the flesh of a dead Sponsorship Co-ordinator")
        input()
        print("The AIRBUS 747 seems to be above your current skill rating. What do you wanna do?")
        print("Press 1 to fight")
        print("Press 2 to run away")
        if input_choice(["1", "2"]) == "1":
            return fight(T_REX)
        else:
            print("You run away from the monster")
            return 2

    elif plot == 2:
        print("You move on")
        input()
        print("You see a cave in front of you")
        input()
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
        input()
        print("You continue to walk forward")
        input()
        print("You see two new paths. One leading to the left and the other to the right")
        input()
        print("Which path do you wish to take? ")
        print("Press 1 to go left")
        print("Press 2 to go right")
        if input_choice(["1", "2"]) == "1":
            return 3.1
        else:
            return 3.2

    elif plot == 3.1:
        global enemy1
        print("You go through the left path. You see something moving.")
        input()
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
        input()
        print("You see a lever in the distance, illuminated by light coming from a hole in the ceiling")
        input()
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
        input()
        print("You go right")
        input()
        print("You keep walking forward and reach the end of the cave")
        return 5

    elif plot == 3.21:
        print("You see two paths infront of you. The one on the left seems to be the one you just opened")
        input()
        print("Which door do you wish to go through?")
        print("Press 1 for left path")
        print("Press 2 for right path")
        if input_choice(["1", "2"]) == "1":
            print("You see a nest with something in it")
            input()
            print("They look like AIRBUS STANDEES")
            input()
            print("What do you want to do?")
            print("Press 1 to take the STANDEES")
            print("Press 2 to ignore it and keep walking")
            if input_choice(["1", "2"]) == "1":
                print("You take the STANDEES and keep in in your bag")

                print("You keep walking forward and reach the end of the cave")
                return 4
            else:
                print("You keep walking forward and reach the end of the cave")
                return 5
        else:
            print("You keep walking forward and reach the end of the cave")
            return 5
    elif plot == 4:
        print("You exit the cave to see a garden with a river flowing through the middle")
        input()
        print("The river is coming from a small waterfall")
        input()
        print("You can see bright colours behind the waterfall")
        input()
        print("You proceed to the WATERFALL to inspect what's behind it")
        input()
        print("It looks like you need to jump to cross. Looks like you got a 67% chance of making the jump")
        input()
        print("Do you want to jump or look for another way in?")
        print('Press 1 to jump')
        print("press 2 to look for an alternate route")
        if input_choice(["1", "2"]) == "1":
            jump_result = random.uniform(0, 1)
            if jump_result <= 0.67:
                return 4.1
            else:
                return 101
        else:
            print("You look for another way in but you could not find any.")
            input()
            print("Do you want to jump?")
            print("Press 1 to jump")
            if input_choice(["1"]) == "1":
                jump_result = random.uniform(0, 1)
                if jump_result <= 1:
                    return 4.1
                else:
                    return 101
    elif plot == 4.1:
        print("You made the jump")
        input()
        print("You see a lab, almost completely destroyed. It looks like some sort of large beast came and attacked the lab")
        input()
        print("You decide to inspect the lab")
        input()
        print("You see a JOURNAL, a POD with wires inside, and a unlocked TRUNK")
        print("Press 1 to inspect the JOURNAL")
        print("Press 2 to inspect the POD")
        print("Press 3 to inspect the TRUNK")
        a = input_choice(["1", "2", "3"])
        if a == "1":
            print("Most of the pages are torn off. There is just one line visible. Looks like some ancient godly text")
            print("i bethought yest'rday wast yest'rday because the present day is tom'rrow")
            print("Press 2 to inspect the POD")
            print("Press 3 to inspect the TRUNK")
            if input_choice(["2", "3"]) == "2":
                print("It looks like someone was experimenting on some beast inside this pod")
                print("The beast was probably taken by the raiders")
                print("Press 3 to inspect the TRUNK")
                if input_choice(["3"]) == "3":
                    print("You find LARGE JACKHAMMER")
                    jackhammer = weapon("JACK HAMMER", 50, 100)
                    print("Do you want to replace your weapon?")
                    print("{} attack stat: {}".format(current_weapon.weapon_name,
                                                      (current_weapon.max_damage + current_weapon.min_damage) / 2))
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
                print("{} attack stat: {}".format(current_weapon.weapon_name,
                                                  (current_weapon.max_damage + current_weapon.min_damage) / 2))
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
            input()
            print("The beast was probably taken by the raiders")
            input()
            print("Press 1 to inspect the JOURNAL")
            print("Press 3 to inspect the TRUNK")
            if input_choice(["1", "3"]) == "1":
                print("Most of the pages are torn off. There is just one line visible. Looks like some ancient godly text")
                print("i bethought yest'rday wast yest'rday because the present day is tom'rrow")
                print("Press 3 to inspect the TRUNK")
                if input_choice(["3"]) == "3":
                    print("You find LARGE JACKHAMMER")
                    jackhammer = weapon("JACK HAMMER", 50, 100)
                    print("Do you want to replace your weapon?")
                    print("{} attack stat: {}".format(current_weapon.weapon_name,
                                                      (current_weapon.max_damage + current_weapon.min_damage) / 2))
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
                print("{} attack stat: {}".format(current_weapon.weapon_name,
                                                  (current_weapon.max_damage + current_weapon.min_damage) / 2))
                print("JACK HAMMER attack stat: {}".format((jackhammer.max_damage + jackhammer.min_damage) / 2))
                print("Press 1 to replace weapon")
                print("Press 2 to keep weapon")
                if input_choice(["1", "2"]) == "1":
                    current_weapon = jackhammer
                else:
                    current_weapon = current_weapon
                print("Press 1 to inspect the JOURNAL")
                if input_choice(["1"]) == "1":
                    print("Most of the pages are torn off. There is just one line visible. Looks like some ancient godly text")
                    print("i bethought yest'rday wast yest'rday because the present day is tom'rrow")
            return 6


        elif a == "3":
            print("You find LARGE JACKHAMMER")
            jackhammer = weapon("JACK HAMMER", 50, 100)
            print("Do you want to replace your weapon?")
            print("{} attack stat: {}".format(current_weapon.weapon_name,
                                              (current_weapon.max_damage + current_weapon.min_damage) / 2))
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
                print("Most of the pages are torn off. There is just one line visible. Looks like some ancient godly text")
                print("i bethought yest'rday wast yest'rday because the present day is tom'rrow")
                print("Press 2 to inspect the POD")
                if input_choice(["2"]) == "2":
                    print("It looks like someone was experimenting on some beast inside this pod")
                    print("The beast was probably taken by the raiders")
            else:
                print("It looks like someone was experimenting on some beast inside this pod")
                input()
                print("The beast was probably taken by the raiders")
                input()
                print("Press 1 to inspect the JOURNAL")
                if input_choice(["1"]) == "1":
                    print(
                        "Most of the pages are torn off. There is just one line visible. Looks like some ancient godly text")
                    print("i bethought yest'rday wast yest'rday because the present day is tom'rrow")
            return 6
    elif plot == 5:
        print("You exit the cave to see a garden with a river flowing through the middle")
        input()
        print("The river is coming from a small waterfall")
        input()
        print("You can see bright colours behind the waterfall")
        input()
        print("You proceed to the WATERFALL to inspect what's behind it")
        input()
        print("It looks like you need to jump to cross. Looks like you got a 67% chance of making the jump")
        print("Do you want to jump or look for another way in?")
        print('Press 1 to jump')
        print("press 2 to look for an alternate route")
        if input_choice(["1", "2"]) == "1":
            jump_result = random.uniform(0, 1)
            if jump_result <= 0.67:
                return 5.1
            else:
                return 101
        else:
            print("You look for another way in but you could not find any.")
            input()
            print("Do you want to jump?")
            print("Press 1 to jump")
            if input_choice(["1"]) == "1":
                jump_result = random.uniform(0, 1)
                if jump_result <= 1:
                    return 5.1
                else:

                    return 101
    elif plot == 5.1:
        print("You made the jump")
        input()
        print("You see a lab, almost completely destroyed. It looks like some sort of large beast came and attacked the lab")
        input()
        print("You decide to inspect the lab")
        input()
        print("You see a JOURNAL, a POD with wires inside, and a unlocked TRUNK")
        print("Press 1 to inspect the JOURNAL")
        print("Press 2 to inspect the POD")
        print("Press 3 to inspect the TRUNK")
        a = input_choice(["1", "2", "3"])
        if a == "1":
            print("Most of the pages are torn off. There is just one line visible. Looks like some ancient godly text")
            print("i bethought yest'rday wast yest'rday because the present day is tom'rrow")
            input()
            print("Press 2 to inspect the POD")
            print("Press 3 to inspect the TRUNK")
            if input_choice(["2", "3"]) == "2":
                print("It looks like someone was experimenting on some beast inside this pod")
                input()
                print("The beast was probably taken by the raiders")
                print("Press 3 to inspect the TRUNK")
                if input_choice(["3"]) == "3":
                    print("You find LARGE JACKHAMMER")
                    jackhammer = weapon("JACK HAMMER", 50, 100)
                    print("Do you want to replace your weapon?")
                    print("{} attack stat: {}".format(current_weapon.weapon_name,
                                                      (current_weapon.max_damage + current_weapon.min_damage) / 2))
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
                print("{} attack stat: {}".format(current_weapon.weapon_name,
                                                  (current_weapon.max_damage + current_weapon.min_damage) / 2))
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
                    input()
                    print("The beast was probably taken by the raiders")
            return 7

        elif a == "2":
            print("It looks like someone was experimenting on some beast inside this pod")
            input()
            print("The beast was probably taken by the raiders")
            input()
            print("Press 1 to inspect the JOURNAL")
            print("Press 3 to inspect the TRUNK")
            if input_choice(["1", "3"]) == "1":
                print(
                    "Most of the pages are torn off. There is just one line visible. Looks like some ancient godly text")
                print("i bethought yest'rday wast yest'rday because the present day is tom'rrow")
                print("Press 3 to inspect the TRUNK")
                if input_choice(["3"]) == "3":
                    print("You find LARGE JACKHAMMER")
                    jackhammer = weapon("JACK HAMMER", 50, 100)
                    print("Do you want to replace your weapon?")
                    print("{} attack stat: {}".format(current_weapon.weapon_name,
                                                      (current_weapon.max_damage + current_weapon.min_damage) / 2))
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
                print("{} attack stat: {}".format(current_weapon.weapon_name,
                                                  (current_weapon.max_damage + current_weapon.min_damage) / 2))
                print("JACK HAMMER attack stat: {}".format((jackhammer.max_damage + jackhammer.min_damage) / 2))
                print("Press 1 to replace weapon")
                print("Press 2 to keep weapon")
                if input_choice(["1", "2"]) == "1":
                    current_weapon = jackhammer
                else:
                    current_weapon = current_weapon
                print("Press 1 to inspect the JOURNAL")
                if input_choice(["1"]) == "1":
                    print(
                        "Most of the pages are torn off. There is just one line visible. Looks like some ancient godly text")
                    print("i bethought yest'rday wast yest'rday because the present day is tom'rrow")
            return 7


        elif a == "3":
            print("You find LARGE JACKHAMMER")
            jackhammer = weapon("JACK HAMMER", 50, 100)
            print("Do you want to replace your weapon?")
            print("{} attack stat: {}".format(current_weapon.weapon_name,
                                              (current_weapon.max_damage + current_weapon.min_damage) / 2))
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
                print(
                    "Most of the pages are torn off. There is just one line visible. Looks like some ancient godly text")
                print("i bethought yest'rday wast yest'rday because the present day is tom'rrow")
                input()
                print("Press 2 to inspect the POD")
                if input_choice(["2"]) == "2":
                    print("It looks like someone was experimenting on some beast inside this pod")
                    input()
                    print("The beast was probably taken by the raiders")
            else:
                print("It looks like someone was experimenting on some beast inside this pod")
                input()
                print("The beast was probably taken by the raiders")
                print("Press 1 to inspect the JOURNAL")
                if input_choice(["1"]) == "1":
                    print(
                        "Most of the pages are torn off. There is just one line visible. Looks like some ancient godly text")
                    print("i bethought yest'rday wast yest'rday because the present day is tom'rrow")
            return 7
    elif plot == 6:
        print("You leave the waterfall")
        input()
        print("You feel something wobbling in your bag")
        input()
        print("The AIRBUS STANDEE is almost about to hatch into an A-320")
        input()
        print("You keep walking")
        input()
        print("You see a Savannah. Many Pravega Co-ordinators are running around trying to get an HDMI to VGA converter")
        input()
        print("You see a couple of them shouting at their volunteers")
        input()
        print("Suddenly you hear a loud roar. Sounds like the AIRBUS 747")
        input()
        print("You see it run towards you at full speed")
        input()
        print("What do you wanna do?")
        print("Press 1 to fight")
        print("Press 2 to run away")
        print("Press 3 to give her the STANDEE")
        choice = input_choice(["1", "2", "3"])
        if choice == "1":
            return fight(T_REX2)
        elif choice == "2":
            print("You hide in the bushes")
            input()
            print("The AIRBUS 747 runs away")
            return 8
        elif choice == "3":
            print("You take out the STANDEE from your bag")
            input()
            print("The AIRBUS 747 comes to a halt")
            input()
            print("You slowly lay down the STANDEE infront of the mama")
            input()
            print('The STANDEE wobbles again and cracks')
            input()
            print("The baby A-320 comes out of the EGG as it hatches")
            input()
            print("The mama seems to be grateful")
            input()
            print("The mama walks away with her offspring")
            input()
            print("You obtained AIRBUS SPONSORSHIP")
            input()
            print("Do you want to infuse AIRBUS SPONSORSHIP with your weapon?")
            print("Press 1 for yes")
            print("Press 2 for no")
            if input_choice(["1", "2"]) == "1":
                current_weapon.max_damage = current_weapon.max_damage + 150
                current_weapon.min_damage = current_weapon.min_damage + 150
                print("{} damage has increased immensely".format(current_weapon.weapon_name))
                return 8
            else:
                return 8



    elif plot == 7:
        print("You leave the waterfall")
        input()
        print("You keep walking")
        input()
        print("You see a Savannah. Many Pravega Co-ordinators are running around trying to get an HDMI to VGA converter")
        input()
        print("You see a couple of them shouting at their volunteers")
        input()
        print("Suddenly you hear a loud roar. Sounds like the AIRBUS 747")
        input()
        print("You see it run towards you at full speed")
        input()
        print("What do you wanna do?")
        print("Press 1 to fight")
        print("Press 2 to run away")
        if input_choice(["1", "2"]) == "1":
            return fight(T_REX2)
        else:
            print("You hide in the bushes")
            input()
            print("The AIRBUS 747 runs away")
            return 8
    elif plot == 8:
        print("You cross the Savannah")
        input()
        print("You reach a Monster Hunter Convention")
        input()
        print("You see many other monster hunters there, just like yourself")
        input()
        print("There seems to be a MONSTER HUNTER ARENA where you can spar with fellow monster hunters")
        input()
        print("Do you wish to spar with them?")
        print("Press 1 for yes")
        print("Press 2 to continue on your journey")
        if input_choice(["1", "2"]) == "1":
            return 8.1
        else:
            return 9
    elif plot == 8.1:
        print("You enter the MONSTER HUNTER ARENA")
        input()
        print("You go up to the registration office and see Aswhath there")
        input()
        print("What do you want to be called?")
        input()
        arena_name = input("Enter fighter name here: ")
        print("Welcome {}. Let us proceed to your first match".format(arena_name))
        opponent_select = random.uniform(0, 1)
        if 0 <= opponent_select <= 0.33:
            opponent = ArenaFoe1
        elif 0.34 <= opponent_select <= 0.67:
            opponent = ArenaFoe2
        elif 0.68 <= opponent_select <= 1:
            opponent = ArenaFoe3
        print("Your opponent is {}".format(opponent.beast_name))
        input()
        print("Are you ready?")
        print("Press 1 to fight whenever you are ready")
        if input_choice(["1"]) == "1":
            return fight(opponent)
    elif plot == 8.2:
        print("Do you wish to fight again?")
        print("Press 1 to fight again")
        print("Press 2 to continue journey")
        if input_choice(["1", "2"]) == "1":
            return 8.1
        else:
            return 9

    elif plot == 9:
        print("You keep walking")
        input()
        print("You see a gate")
        input()
        print("You see a massive board infront of the gate")
        input()
        print("It looks like a puzzle")
        input()
        print("Under it, there is a note that says: ")
        input()
        print("On decoding this puzzle, this gate will open")
        input()
        print("And then, you can continue your adventure")
        print("The puzzle reads")
        input()
        print("ENVIAR MIJ ELFU MOJA EN GooPAY")
        input()
        print("Your next adventure awaits")
        return "end"

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
        if input_choice(["1", "2"]) == "1":
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

        x = storyline(x)
        if x == "end":
            break


main()
