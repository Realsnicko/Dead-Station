import random
import glib
def deathscreen(c):
        glib.slpr(f"You have fallen. Your community will go on. But you wont.")
        glib.slpr(f"You failed them. For the last time.")
        glib.slpr(f"Be better.", 0.1)

def event(s, dat):
    print(s)
    if dat["addicted"] is None:
        if glib.oit():
            dat["addicted"] = random.choice(["Meth", "Marijuana", "Cocaine"])
            glib.slpr(f"EVENT: {dat["name"]} has become addicted to {dat["addicted"]}")