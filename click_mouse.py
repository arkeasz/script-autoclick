import threading
import time
from pynput.mouse import Controller, Button


class ClickMouse(threading.Thread):
    def __init__(self, delay, button, update_status_callback):
        super().__init__()
        self.delay = delay
        self.button = Button.left if button == 'left' else Button.right
        self.update_status_callback = update_status_callback
        self.running = False
        self.program_running = True
        self.mouse = Controller()
        self.daemon = True 

    def start_clicking(self):
        self.running = True
        self.update_status_callback("[green]Autoclick: RUNNING[/green]")

    def stop_clicking(self):
        self.running = False
        self.update_status_callback("[yellow]Autoclick: STOPPED[/yellow]")

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            if self.running:
                self.mouse.click(self.button)
                time.sleep(self.delay)
            else:
                time.sleep(0.1)
