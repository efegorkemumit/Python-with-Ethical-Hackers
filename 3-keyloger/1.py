import pynput.keyboard

def process_key_press(key):
    print(key)

keyword_listener = pynput.keyboard.Listener(on_press = process_key_press)
with keyword_listener:
    keyword_listener.join()