from pynput import keyboard
from pynput.keyboard import Key, Listener, Controller

keyboard = Controller()

def move_right():
    print("Pressing D")
    keyboard.press('d')
    keyboard.release('d')

def move_left():
    print("Pressing A")
    keyboard.press('a')
    keyboard.release('a')

def move_up():
    print("Pressing W")
    keyboard.press('w')
    keyboard.release('w')

def move_down():
    print("Pressing S")
    keyboard.press('s')
    keyboard.release('s')