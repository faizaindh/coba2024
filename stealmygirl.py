import sys
from time import sleep

def print_lyrics():
    lines = [
        ("She's been my queen", 0.05),
        ("since we were sixteen", 0.05),
        ("We want the same things", 0.05),
        ("we dream the same dreams", 0.05),
        ("Alright", 0.05),
        ("Alright", 0.05),
    ]
    
    delays = [0.3, 0.3, 0.3,0.4, 2.7, 2.7] 
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print("")

print_lyrics()
