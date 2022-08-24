import os
import random
import time
import sys
from colorama import Fore

CURSOR_UP_ONE = '\x1b[1A' # move cursor
ERASE_LINE = '\x1b[2K' # erase line

def delete_last_lines(n=1):
    # Deletes n printed lines in console
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def quick_print(names_list):
    # Quickly prints and deletes lines in console
    i = 0
    colours = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE] # print colours
    while i < 200:
        for name in names_list:
            i += 1
            print(random.choice(colours) + name) # pick random colour and print name
            time.sleep(0.01)
            delete_last_lines(n=1)
            
            
names = [ # list of names
    "Billy",
    "Amanda",
    "Joe",
    "Brittany",
    "Owen",
    "James",
    "Sarah",
    "Fred",
    "Timmy",
    "Beth",
]
names2 = names
random.shuffle(names) # shuffle names

for name in names:
    quick_print(names2)
    print(name)
    input("Hit Enter to Pick Next Name \n")
    delete_last_lines(n=3)
