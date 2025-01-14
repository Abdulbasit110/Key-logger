# Python Keylogger

This project is a simple keylogger implemented in Python. It captures user keystrokes and stores them in an encrypted log file. The logging process can be terminated by pressing the `Esc` key.

## Key Logger Flow

![image](https://github.com/user-attachments/assets/e48945c5-6605-44dd-baaf-6275e7df7fd7)

## Features

- **Keystroke Logging:** Records all keystrokes made by the user.
- **Encryption:** Utilizes the `cryptography` library to encrypt logged keystrokes, ensuring data security.
- **Termination with Esc Key:** Pressing the `Esc` key stops the keylogger gracefully.

## Prerequisites

Ensure you have the following installed:

- **Python 3.x**
- **pynput library**: For capturing keyboard input.
- **cryptography library**: For encrypting the logged keystrokes.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/python-keylogger.git
   cd python-keylogger
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

   - Use the same encryption key generated during the logging session to decrypt and read the contents.

## Code Overview

The key components of the keylogger are:

- **Keystroke Capture:** Utilizes the `pynput` library to monitor and record keystrokes.
- **Encryption:** Employs the `cryptography` library's `Fernet` module to encrypt keystrokes before logging.
- **Termination:** Listens for the `Esc` key to stop the keylogger gracefully.

## Ethical Considerations

This keylogger is developed for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain explicit consent before deploying this tool on any system.

## Acknowledgments

- [pynput library](https://pypi.org/project/pynput/)
- [cryptography library](https://cryptography.io/)

**Important Notes:**

- Replace `https://github.com/yourusername/python-keylogger.git` with the actual URL of your GitHub repository.
- Ensure that the `LICENSE` file is included in your repository if you reference it in the `README.md`.
- This `README.md` provides clear instructions and information about your project, facilitating understanding and proper usage by others.

**References:**

- For more insights into creating keyloggers in Python, you can refer to the following resources:

  - [Design a Keylogger in Python - GeeksforGeeks](https://www.geeksforgeeks.org/design-a-keylogger-in-python/)

  - [Implementing a KeyLogger in Python - AskPython](https://www.askpython.com/python/examples/keylogger-in-python)

  - [Creating a Keylogger in Python - ByteScrum](https://blog.bytescrum.com/creating-a-keylogger-in-python)

