import pywifi
from pywifi import const
import time
import matplotlib.pyplot as plt

def get_security_type(network):
    if network.akm:
        if const.AKM_TYPE_WPA2PSK in network.akm:
            return "WPA2"
        elif const.AKM_TYPE_WPAPSK in network.akm:
            return "WPA"
        elif const.AKM_TYPE_WPA in network.akm:
            return "WPA"
        elif const.AKM_TYPE_NONE in network.akm:
            return "OPEN"
    if network.auth == const.AUTH_ALG_OPEN:
        return "OPEN"
    if network.auth == const.AUTH_ALG_SHARED:
        return "WEP"
    return "UNKNOWN"

def scan_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2) 
    results = iface.scan_results()
    networks = []
    for net in results:
        sec_type = get_security_type(net)
        networks.append({
            "SSID": net.ssid,
            "BSSID": net.bssid,
            "Signal": net.signal,
            "Channel": net.freq,
            "Security": sec_type
        })
    return networks

import numpy as np

def plot_networks(networks, explanations, warnings):
    ssids = [n['SSID'] for n in networks]
    signals = [n['Signal'] for n in networks]
    colors = ['red' if n['Security'] == 'OPEN' else 'green' for n in networks]

    x = np.arange(len(ssids))
    fig, ax = plt.subplots(figsize=(12, 7))
    bars = ax.bar(x, signals, color=colors, width=0.6)

    ax.set_ylabel('Signal Strength (dBm)')
    ax.set_xlabel('SSID')
    ax.set_title('WiFi Networks (Red = Open/Unsecure)')
    ax.set_xticks(x)
    ax.set_xticklabels(ssids, rotation=45, ha='right')

    plt.tight_layout(rect=[0, 0.2, 1, 1])  

    explanation_text = "Security Types:\n" + "\n".join([f"{k}: {v}" for k, v in explanations.items()])
    warning_text = "\n".join(warnings) if warnings else "No insecure networks found."

    full_text = explanation_text + "\n\nSecurity Warnings:\n" + warning_text
    fig.text(0.01, 0.01, full_text, fontsize=10, va='bottom', ha='left', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    plt.show()