# Python Keylogger

This project is a simple keylogger implemented in Python. It captures user keystrokes and stores them in an encrypted log file. The logging process can be terminated by pressing the `Esc` key. Additionally, a decryption function is included to view the logged keystrokes securely.

## Key Logger Flow

![image](https://github.com/user-attachments/assets/91078e4e-413a-4933-8e3c-2297f43fee92)


## Features

- **Keystroke Logging:** Records all keystrokes made by the user.
- **Encryption:** Utilizes the `cryptography` library to encrypt logged keystrokes, ensuring data security.
- **Decryption Functionality:** Includes a function to decrypt the log file and display the original keystrokes securely.
- **Termination with Esc Key:** Pressing the `Esc` key stops the keylogger gracefully.
- **Persistent Encryption Key:** The encryption key is saved in a file (`encryption_key.key`) to ensure data can be decrypted across sessions.

## Prerequisites

Ensure you have the following installed:

- **Python 3.x**
- **pynput library**: For capturing keyboard input.
- **cryptography library**: For encrypting and decrypting the logged keystrokes.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Abdulbasit110/Key-logger.git
   cd Key-logger
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install pynput cryptography
   ```

## Usage

1. **Run the Keylogger:**

   ```bash
   python main.py
   ```

2. **Terminate Logging:**

   - Press the `Esc` key to stop the keylogger gracefully.

3. **Access the Log File:**

   - The encrypted log file (`keys.txt`) will be in the same directory.

4. **Decrypt the Log File:**

   - After the keylogger stops, you will be prompted to decrypt the log file.
   - Select "yes" to decrypt and view the original keystrokes.
   - The encryption key saved in `encryption_key.key` ensures decryption is consistent across sessions.

## Code Overview

The key components of the keylogger are:

- **Keystroke Capture:** Utilizes the `pynput` library to monitor and record keystrokes.
- **Encryption:** Employs the `cryptography` library's `Fernet` module to encrypt keystrokes before logging.
- **Decryption:** Reads the encrypted log file and decrypts its contents using the stored encryption key.
- **Termination:** Listens for the `Esc` key to stop the keylogger gracefully.
- **Persistent Encryption Key:** Ensures the encryption key remains consistent, enabling seamless decryption of logs from previous sessions.

## Ethical Considerations

This keylogger is developed for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain explicit consent before deploying this tool on any system.

## Acknowledgments

- [pynput library](https://pypi.org/project/pynput/)
- [cryptography library](https://cryptography.io/)

## References

- For more insights into creating keyloggers in Python, you can refer to the following resources:

  - [Design a Keylogger in Python - GeeksforGeeks](https://www.geeksforgeeks.org/design-a-keylogger-in-python/)
  - [Implementing a KeyLogger in Python - AskPython](https://www.askpython.com/python/examples/keylogger-in-python)
  - [Creating a Keylogger in Python - ByteScrum](https://blog.bytescrum.com/creating-a-keylogger-in-python)

