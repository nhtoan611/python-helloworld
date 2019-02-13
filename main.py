import random
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

print("\n")
# create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restore HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restore party's HP/MP ", 9999)

grenade = Item("Grenade", "grenade", "Deal 500 damage", 500)

player_speels = [fire, thunder, blizzard, meteor, cura]
player_items = [{"item": potion, "quantity": 5},
                {"item": elixer, "quantity": 15},
                {"item": hielixer, "quantity": 15},
                {"item": grenade, "quantity": 25}]

#player = Person("Toan",460, 65, 60, 34, player_speels, player_items )
player1 = Person("Toan  ",460, 65, 60, 34, player_speels, player_items )
player2 = Person("Hoang ",300, 65, 90, 34, player_speels, player_items )
player3 = Person("Tho   ",900, 65, 30, 34, player_speels, player_items )
enemy = Person("Enemy", 2000, 65, 45, 25, [], [])

players = [player1, player2, player3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attack!!" + bcolors.ENDC)

while running: 
    print("======================")
    print("NAME                          HP                                   MP")
    for player in players:       
        player.get_stats()
    
    enemy.get_enemy_stats()

    for player in players: 
        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("\n - You attack for " + str(dmg) + " points of damage." )
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            cost = spell.cost

            current_mp = player.get_mp()

            if cost > current_mp:
                print(bcolors.FAIL + "\n Not enough MP \n" + bcolors.ENDC)
                continue
            
            player.reduce_mp(cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n - " + spell.name + " heals for "+ str(magic_dmg)+" HP."+bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n - " + spell.name + " deals " + str(magic_dmg) + " points of damage." + bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) -1
            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n"+"None left ..."+bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKBLUE + "\n - " + item.name + " heals for "+ str(item.prop)+" HP."+bcolors.ENDC)
            
            elif item.type == "elixer":
                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp 
                print(bcolors.OKBLUE + "\n - " + item.name + " fully restore HP/MP "+bcolors.ENDC)

            elif item.type == "grenade":
                enemy.take_damage(item.prop)
                print(bcolors.OKBLUE + "\n - " + item.name + " deals " + str(item.prop) + " points of damage." + bcolors.ENDC)

        enemy_choice = 1
        target = random.randrange(0,3)
        print(target)
        enemy_dmg = enemy.generate_damage()
        players[target].take_damage(enemy_dmg)
        print(" - Enemy attack "+players[target].name.strip()+" " + str(enemy_dmg) + " points of damage.")
        print(bcolors.FAIL+" - Enemy HP: "+str(enemy.hp)+bcolors.ENDC)

        if enemy.get_hp() == 0:
            print(bcolors.OKGREEN + bcolors.BOLD + "You win!" + bcolors.ENDC)
            running = False
        elif player.get_hp() == 0:
            print(bcolors.FAIL + "Game over!" + bcolors.ENDC)
            running = False