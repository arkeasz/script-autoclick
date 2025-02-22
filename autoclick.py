from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.reactive import reactive
from pynput.keyboard import Listener, KeyCode
from click_mouse import ClickMouse
from textual.color import Color


class AutoClickApp(App):
    CSS = "Screen {align: center middle;}"
    status = reactive("[white]Autoclick: STOPPED[/white]")

    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.click_thread = ClickMouse(delay, button, self.update_status)
        self.listener = None

    def compose(self) -> ComposeResult:
        self.status_display = Static(self.status)
        instructions = Static("[cyan]Press [bold]R[/bold] to start/stop | Press [bold]X[/bold] to exit[/cyan]")
        yield self.status_display
        yield instructions


    def update_status(self, message):
        self.status = message
        if "RUNNING" in message:
            self.screen.styles.background = Color(78, 191, 96) 
        else:
            self.screen.styles.background = Color(191, 78, 96) 


    def on_mount(self) -> None:
        self.screen.styles.background = Color(191, 78, 96)
        self.screen.styles.border = ('heavy', 'white')
        self.click_thread.start()
        start_stop_key = KeyCode(char='r')
        exit_key = KeyCode(char='x')

        def on_press(key):
            if key == start_stop_key:
                if self.click_thread.running:
                    self.click_thread.stop_clicking()
                else:
                    self.click_thread.start_clicking()
            elif key == exit_key:
                self.exit()

        self.listener = Listener(on_press=on_press)
        self.listener.start()

    def on_unmount(self) -> None:
        if self.listener:
            self.listener.stop()
        self.click_thread.exit()
