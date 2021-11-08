from pynput import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as kcon

mouse = Controller()
keyboard = kcon()

class Input():
    def focus_game(self):
        mouse.position = (100, 100)
        mouse.click(Button.left, 1)

    def move_dir(self, dir):
        if dir == [0, 1]:
            self.move_right()
        if dir == [0, -1]:
            self.move_left()
        if dir == [-1, 0]:
            self.move_up()
        if dir == [1, 0]:
            self.move_down()

    def move_right(self):
        print("Pressing D")
        keyboard.press('d')
        keyboard.release('d')

    def move_left(self):
        print("Pressing A")
        keyboard.press('a')
        keyboard.release('a')

    def move_up(self):
        print("Pressing W")
        keyboard.press('w')
        keyboard.release('w')

    def move_down(self):
        print("Pressing S")
        keyboard.press('s')
        keyboard.release('s')