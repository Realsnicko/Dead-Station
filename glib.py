text_speed = 0.1
import os
import time
import random
def cl():
    try:
        os.system('cls')
    except:
        os.system('clear')
def slpr(text, delay=None):
    global text_speed
    if delay is None:
        delay = 0.03
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    time.sleep(1)

def dialogue(prompt, text=False, *options):
    print(f"{prompt}\n\n\n\n")

    if text:
        return input("> ").strip()

    if not options:
        return input("> ").strip()

    for i, option in enumerate(options, start=1):
        print(f"[{i}] {option}")

    while True:
        choice = input("> ").strip()

        if not choice.isdigit():
            print("Invalid input. Enter an option number.")
            continue

        choice = int(choice)

        if not 1 <= choice <= len(options):
            print(f"Choose a number between 1 and {len(options)}.")
            continue

        return str(choice)

def cf():
    x = random.randint(1,2)
    if x == 1: return True
    if x == 2: return False
    else: print("wtf cf returned smth that isnt 1 or 2 how did that happen")

def oit():
    x = random.randint(1,3)
    if x == 1: return True
    else: return False