import sys
from time import sleep
import time


def print_lyrics():
    lines = [
        ("bring the boom", 0.058),
        ("bring the boom", 0.058),
        ("listen to the sound", 0.05),
        ("oh what fun it is to bring", 0.058),
        ("the boomest holiday", 0.058)
    ]

    delays = [0.1, 0.1, 0.1, 0.1, 0.1]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')


print_lyrics()
