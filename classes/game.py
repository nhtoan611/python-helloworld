from __future__ import division
import random
from .magic import Spell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df 
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <0:
            self.hp = 0
        return self.hp
    
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        #print("\n"+bcolors.BOLD + self.name + bcolors.ENDC)
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + self.name.strip() +"'s turn" + bcolors.ENDC)
        for item in self.actions:
            print("    "+str(i) + ": " + item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n"+bcolors.OKBLUE + bcolors.BOLD + "Magic" + bcolors.ENDC) 
        for spell in self.magic:
            print("    "+str(i) + ": " + spell.name + " -- Cost: " +str(spell.cost))
            i += 1

    def choose_item(self):
        i = 1
        print("\n"+bcolors.OKBLUE + bcolors.BOLD + "Items"+bcolors.ENDC)
        for item in self.items:
            print("    "+str(i) + ": " + item["item"].name + " --- " + item["item"].description + " (x"+ str(item["quantity"])+")")
            i += 1

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 /4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 10

        while bar_ticks >0 :
            hp_bar += "/"
            bar_ticks -= 1
        
        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "/"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        lenhp = 4 - len(str(self.hp))
        lenhpadd = ""
        while lenhp > 0:
            lenhpadd += " "
            lenhp -= 1

        lenmp = 4 - len(str(self.mp))
        lenmpadd = ""
        while lenmp > 0:
            lenmpadd += " "
            lenmp -= 1

        print("                               _________________________              __________")
        print(bcolors.BOLD+self.name+"               "
        +str(self.hp)+"/"+str(self.maxhp)+lenhpadd+" |" +bcolors.FAIL+ hp_bar+bcolors.ENDC + "|"+bcolors.BOLD+"     "
        +str(self.mp)+"/"+str(self.maxmp)+lenmpadd +"|"+bcolors.OKBLUE+mp_bar+bcolors.ENDC+"|")

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 50

        while bar_ticks >0 :
            hp_bar += "/"
            bar_ticks -= 1
        
        while len(hp_bar) < 50:
            hp_bar += " "

        lenhp = 4 - len(str(self.hp))
        lenhpadd = ""
        while lenhp > 0:
            lenhpadd += " "
            lenhp -= 1

        print("                               __________________________________________________")
        print(bcolors.BOLD+self.name+"               "
        +str(self.hp)+"/"+str(self.maxhp)+lenhpadd+" |" +bcolors.FAIL+ hp_bar+bcolors.ENDC + "|")