import battlelib
import glib
from pathlib import Path
import dslib
import time
import json
import datetime
scriptdir = Path(__file__).resolve().parent
csave_file = scriptdir / "saves" / "comsave.json"
psave_file = scriptdir / "saves" / "psave.json"
#region definingHelperVars
n = False
f = False
y = True
t = True
#endregion
# class char:
#     def __init__(self,name,health=100,morale=100, survivor=True):
#         self.name = name
#         self.hp = health
#         self.morale = morale
#         self.damage = 15.5
#         if survivor:
#             self.addicted = None
#             self.sick = False

#     def kill(self):
#         self.health = 0

def gsur(name,hp=100,morale=100,survivor=True):
    default = {
        "name": name,
        "hp": hp,
        "morale": morale,
        "damage": 15.5
    }
    if survivor:
        default["addicted"] = None
        default["sick"] = None
    return default
version = "internalV0.0"
gamename = "Dead Station"
glib.cl()
print(f"Welcome to {gamename} {version}\nLead your people well, for they shall treat you as you lead them.\n\n\n\n\n")
print("1) Start Game\n2) Settings\n3) Saves\n4) Release Notes\n\n")
action = input("> ")
if action == "1":
    if not psave_file.is_file() or not csave_file.is_file():
        p = gsur(None)
        community = {
            "name": None,
            "members": {},
            "averagemorale": None,
            "food": None,
            "meds": None,
            "ammo": None,
            "mats": None,
            "alive": True,
            "day": 0,
            "survivorcount": 1
        }
        pickingcomname = True
        while pickingcomname:
            glib.cl()
            cname = glib.dialogue("Name your community.", True)
            glib.cl()
            x = glib.dialogue(f"So, your community shall be called '{cname}'?", False, "Yes", "No")
            if x == "2":
                continue
            if x == "1":
                pickingcomname = False
        del pickingcomname
        print(f"{cname}... a wonderful name. Lead your people well, for they shall treat you as you lead them.")
    else:
        with open(psave_file,"r",encoding="utf-8") as f:
            p = json.load(f)
        with open(csave_file,"r",encoding="utf-8") as f:
            community =json.load(f)
    time.sleep(3)
    glib.cl()
    glib.slpr(f"08:00 - 10/29/17 (MMDDYY).")
    glib.slpr(f"The bombs have fallen.")
    glib.slpr(f"The apocalypse has begun.")
    time.sleep(3)
    glib.cl()
    choosingitems = True
    count = 0
    chosenitems = []
    items = ["Baseball Bat", "Medicine", "Ammunition", "Materials", "Gas Mask", "Firearm"]
    while choosingitems and count < 3:
        choice = glib.dialogue("Several items lie before you. Which do you choose?",n,*items)
        if not choice.isdigit():
            continue
        choice = int(choice)
        chosen = items.pop(choice - 1)
        chosenitems.append(chosen)
        count += 1
        pci = "\n".join(chosenitems)
        if count == 3:
            glib.cl()
            print("You have chosen the following:\n", pci)
            x = glib.dialogue("Do you accept these choices?",n,"1) Yes","2) No")
            if x == 1:
                choosingitems = False
            if x == 2:
                continue
        glib.cl()
    del choosingitems, count, items
    glib.slpr("You retreat to the bunker with the items you have chosen.")
    glib.slpr("The doors slam shut behind you. A pressure wave chases you down the stairs. You nearly lose your footing.")
    time.sleep(2)
    glib.cl()
    #time.sleep(2)
    if "Baseball Bat" in chosenitems:
        p["damage"] += 7
while community["alive"] == True and community["survivorcount"] > 0:
    glib.cl()
    glib.slpr(f"DAY {community["day"]}", 0.2)
    print(f"Community morale: {community["averagemorale"]}")
    action = glib.dialogue("You're sitting in your bunker. What will you do?",n,"Explore\nEnter the city in hopes of finding loot, combat, or other survivors.","Signal to other survivors\nSignals to anyone who may be listening where you are. Not all who pick up this signal are friendly.","Skip\nSkip this turn. This can be benifical if you have abilities to benefit from this.\n","Save Game\nSave your current progress.")
    if action == "1":
        glib.cl()
        p = battlelib.entercity(p)
        if p.hp == 0:
            community["alive"] = False
            glib.cl()
            dslib.deathscreen()
    if action == "2":
        glib.cl()
        if not glib.oit() and not glib.oit():
            survivor = gsur("Bob")
            trash = community["survivorcount"] + 1
            community["survivorcount"] += 1
            trash2 = f"Survivor{trash}"
            del trash
            community["members"][trash2] = survivor
            print(community)
            glib.slpr("A new survivor has joined your community!")
        else:
            glib.slpr("Uh oh... a raider operation has begun on the border of your territory.")
    if action == "3":
        glib.slpr("You skip the day...")
        glib.cl()
    if action == "4":
        with open(csave_file, "w", encoding="utf-8") as f:
            json.dump(community, f)
        with open(psave_file, "w", encoding="utf-8") as f:
            json.dump(p, f)
    community["day"] += 1
    for s, dat in community["members"].items():
        glib.oit()
        if not glib.oit():
            pass
        else:
            dslib.event(s, dat)