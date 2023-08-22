import time
import pywifi
from pywifi import const

def scan_wifi():
    wifi = pywifi.PyWiFi()  # Create a PyWiFi object
    iface = wifi.interfaces()[0]  # Get the Wi-Fi interface

    iface.scan()  # Start scanning for Wi-Fi networks
    time.sleep(2)  # Wait for the scan to complete

    scan_results = iface.scan_results()
    return scan_results

def main():
    networks = scan_wifi()
    
    print("Available Wi-Fi Networks:")
    for network in networks:
        ssid = network.ssid
        signal_strength = network.signal
        bssid = network.bssid
        print(f"SSID: {ssid}, Signal Strength: {signal_strength}, BSSID: {bssid}")

if __name__ == "__main__":
    main()
