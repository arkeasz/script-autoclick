from pynput.mouse import Button
import argparse
import os
from autoclick import AutoClickApp

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Autoclicker with Textual")
    parser.add_argument("--left", action="store_true", help="Use left mouse button")
    parser.add_argument("--right", action="store_true", help="Use right mouse button")
    args = parser.parse_args()

    delay = 0.1
    button = Button.left

    if args.left:
        button = Button.left
        delay = 0.05
    elif args.right:
        button = Button.right
        delay = 0.5

    os.system('cls' if os.name == 'nt' else 'clear')
    app = AutoClickApp(delay, button)
    app.run()
