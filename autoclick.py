# !/usr/bin/python
from typing import List
from click_mouse import *
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Button, Controller
from rich.console import Console
from rich.style import Style
import sys
import os

console = Console()

def len(list: List) -> int:
    count = 0

    for el in list:
        count += 1
    
    return count

delay_left: float = 0.1


if len(sys.argv) > 1:
    if sys.argv[1] == "--left":
        button = Button.left
        delay_left: float = 0.0005
    elif sys.argv[1] == "--right":
        button = Button.right
        delay_left: float = 0.005
else:
    button = Button.left
    delay_left: float = 0.0005

os.system('cls' if os.name == 'nt' else 'clear')
console.print("PRESS 'r'", style="#aaaaaa", justify="center", )
start_stop_key = KeyCode(char='r')
exit_key = KeyCode(char='x')


click_thread = ClickMouse(delay_left, button)
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
