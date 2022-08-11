import random
#enconter setup
class encounter():
    def __init__(self):
        print("You are in a forest walking along a path\n", "You hear rustling in the bushes\n")
    def chance(self):
        while True:
            roll = random.randint(0,1)
            clear = 0
            if roll == 0:
                print("A goblin jumps out of the bushes and attacks!\n")
                Battle().outcome()
                break
            else:
                print("nothing happens\n")
                clear += 1
                action = input("do you want to continue? y/n\n")
            if clear == 1:
                print("You made it out of the forest!\n", "The end!")
                break
    def action(self):
        action = input("Do you continue walking? y/n\n")
        while action != {"y""n"}:
            if action =="y":
                self.chance()
                break
            else:
                print("You just stand there doing nothing")
                action = input("do you want to continue? y/n\n")
#Player Stats
class Player():
    def __init__(stats, pHP = 5):
        stats.pHP = pHP
        super().__init__()
#Goblin Stats
class Goblin():
    def __init__(stats):
        stats.gHP = random.randint(3,5)
#Battle encounter
class Battle(Player,Goblin):
    def __init__(stats):
        super().__init__()
    def action(stats):
        #Player and Goblin attack damage and hit chance rolled from here
        stats.roll = random.randint(0,1)
        stats.attk = random.randint(1,4)
    def outcome(stats):
        while True:
            print("The Goblin has",stats.gHP,"Health\n")
            choice = input("Would you like to Attack the goblin?\n")
            if choice == "y":
                print("You swing at the goblin")
                stats.action()
                if stats.roll == 0:
                    print("Hit! The Goblin takes",stats.attk,"damage\n")
                    stats.gHP -= stats.attk
                else:
                    print("you missed!")
            if stats.gHP <= 0:
                print("The Goblin has been defeated!\n")
                break

mock = encounter()
mock.action()
input('Press ENTER to exit')


