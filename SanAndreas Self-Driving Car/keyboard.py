from pynput.keyboard import Key, Listener


key_presses = []
def on_press(key):
    if key not in key_presses:
        key_presses.append(key)

def on_release(key):
    if key in key_presses:
        key_presses.remove(key)
    if key == Key.esc:
        # Stop listener
        return False

from threading import Thread
def start_thread():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

t1 = Thread(target=start_thread)
t1.start()
while True:
    print(key_presses)