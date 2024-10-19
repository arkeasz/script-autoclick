# !/usr/bin/python
from click_mouse import *
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Button, Controller
from rich.console import Console
from rich.style import Style
import argparse
import os

console = Console()

parser = argparse.ArgumentParser(description="Autoclicker")
parser.add_argument("--left", action="store_true", help="Use left mouse button")
parser.add_argument("--right", action="store_true", help="Use right mouse button")
args = parser.parse_args()

delay: float = 0.1
button = Button.left

if args.left:
    button = Button.left
    delay: float = 0.05
elif args.right:
    button = Button.right
    delay: float = 0.5


os.system('cls' if os.name == 'nt' else 'clear')
console.print("PRESS 'r'", style="#aaaaaa", justify="center", )
start_stop_key = KeyCode(char='r')
exit_key = KeyCode(char='x')


click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            console.print("stop autoclick", style="#ffffff")
        else:
            style = Style(bgcolor="#eeeeee", color="#3322dd")
            click_thread.start_clicking()
            console.print("start autoclick", style=style)
    elif key == exit_key:
        console.print("exit autoclick", style="#aaaaaa")
        click_thread.exit()
        listener.stop()



with Listener(on_press=on_press) as listener:
    listener.join()
