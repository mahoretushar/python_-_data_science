import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Typing Test!\n")
    stdscr.addstr("Press any key to begin.")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}\n")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1) if char == correct_char else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)


def load_text():
    with open("lines.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()  # value of time.time() = seconds since epoch 1970-01-01 00:00:00 UTC
    stdscr.nodelay(True)

    while True:
        elapsed_time = max(time.time() - start_time, 1)
        wpm = round(len(current_text) / (elapsed_time / 60) / 5)

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        # 30 characters per 15s = 120
        # 15 / 60 = 0.25
        # 30 characters / 0.25 = 120
        # 120 / 5 = 24 words per minute

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)

        stdscr.refresh()

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # Escape key ASCII code
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "Thank you for using Typing Test! Press any key to continue.")
        key = stdscr.getkey()
        if ord(key) == 27:  # Escape key ASCII code
            break


wrapper(main)
