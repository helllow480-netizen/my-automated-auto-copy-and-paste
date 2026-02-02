import pyperclip
import time
from pynput import mouse, keyboard

# Initialize controller to simulate key presses
kbd = keyboard.Controller()

def on_click(x, y, button, pressed):
    # We trigger when the right mouse button is RELEASED
    if button == mouse.Button.right and not pressed:
        # Give the OS a tiny moment to ensure text is highlighted
        time.sleep(0.1)
        
        # Simulate Ctrl+C (or Cmd+C on Mac)
        with kbd.pressed(keyboard.Key.ctrl):
            kbd.press('c')
            kbd.release('c')
        
        print("Text attempted to copy to clipboard!")

# Start listening to mouse events
with mouse.Listener(on_click=on_click) as listener:
    print("Python Auto-Copy is running... (Press Ctrl+C in this terminal to stop)")
    listener.join()