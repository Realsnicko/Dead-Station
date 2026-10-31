n = False
f = False
y = True
t = True

class Feral:
    def __init__(self):
        self.hp = 115
        self.damage = 12

import random
import glib
def entercity(p):
    glib.slpr("You enter the city.")
    while True:
        action = glib.dialogue("What will you do?",n,"Loot Building","Engage Feral","Flee the city")
        if action == "1":
            glib.slpr("You enter the building...")
            glib.cl()
        if action == "2":
            glib.slpr("You engage the Feral.")
            e = Feral()
            battle(p,e)
            glib.cl()
        if action == "3":
            glib.slpr("You flee the city, returning home to your bunker.")
def battle(p,e):
    while p.hp > 0 and e.hp > 0:
        glib.cl()
        glib.slpr(f"The Feral slashes wildly at you, dealing {e.damage} damage!")
        p.hp -= e.damage
        action = glib.dialogue("What will you do?",n,"Attack", "Flee")
        if action == "1":
            glib.slpr(f"You slash the Feral, dealing {p.damage} damage!")
            e.hp -= p.damage
        if action == "2":
            if not glib.oit():
                glib.slpr(f"You failed to get away!")
            else:
                glib.slpr(f"You successfully fled from the Feral.")
                break
    if e.hp <= 0:
        glib.slpr(f"You won. You have {p.hp} Health left.")
    else:
        return(p)