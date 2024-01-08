import subprocess
import os
//sourav code
//wifi_password
//this code is made by sourav using python
//hello world
def get_wifi_password():
    try:
        # For Windows
        if os.name == 'nt':
            output = subprocess.check_output('netsh wlan show profiles')
            output = output.decode('utf-8', 'ignore')
            profiles = [line.split(":")[1][1:] for line in output.split("\n") if "All User Profile" in line]

            password_dict = {}
            for profile in profiles:
                output = subprocess.check_output(f'netsh wlan show profile name="{profile}" keyMaterial')
                output = output.decode('utf-8', 'ignore')
                password = [line.split(":")[1][1:] for line in output.split("\n") if "Key Content" in line]
                password_dict[profile] = password[0] if password else None

            return password_dict

        # For Linux/MacOS
        else:
            output = subprocess.check_output('nmcli -s -g all device wifi', shell=True)
            output = output.decode('utf-8', 'ignore')
            connections = [line.split(":")[1][1:] for line in output.split("\n") if "GENERAL.CONNECTION" in line]

            password_dict = {}
            for connection in connections:
                output = subprocess.check_output(f'nmcli -s -g security.psk connection show {connection}', shell=True)
                output = output.decode('utf-8', 'ignore')
                password = [line.split(":")[1][1:] for line in output.split("\n") if "security.psk" in line]
                password_dict[connection] = password[0] if password else None

            return password_dict

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

password_dict = get_wifi_password()
if password_dict:
    for connection, password in password_dict.items():
        print(f"Connection: {connection}, Password: {password}")
else:
    print("No WiFi connections found.")
    
