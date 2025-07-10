from scanner import scan_networks, plot_networks
from security_check import get_security_warnings
from security_explanation import SECURITY_EXPLANATIONS, print_security_tips
import pandas as pd

def main():
    print("Scanning for WiFi networks...")
    networks = scan_networks()
    df = pd.DataFrame(networks)
    print(df)
    
    warnings = get_security_warnings(networks)  
    plot_networks(networks, SECURITY_EXPLANATIONS, warnings)
    print_security_tips()

if __name__ == "__main__":
    main()
