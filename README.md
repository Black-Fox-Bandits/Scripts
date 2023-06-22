# Scripts

### Ransom(RDP)
The script implements a basic ransomware program. It defines a Ransomware class that generates a symmetric encryption key and provides methods to encrypt files in a specified folder on a different virtual machine (VM) using RDP, as well as to decrypt files using the same key. The script prompts the user for actions: encrypting a folder on a different VM or decrypting a folder. It uses the cryptography library for encryption and decryption operations.

### Ransomeware(SSH)
The script represents a ransomware program targeting Windows servers. It defines a Ransomware class that generates a symmetric encryption key and provides methods to encrypt and decrypt files on a Windows server, display a ransom note, and change the server's background. The script utilizes the paramiko library for establishing SSH connections to the target server.
The Ransomware class also includes methods for changing the server's background and displaying a ransom note, but these methods are currently implemented for Linux and need modification for Windows.
The attack_windows_server() method prompts the user for actions: encrypting files, displaying a ransom note, changing the server's background, decrypting files, or exiting. Depending on the user's input, the corresponding method is called to perform the chosen action.
