def get_security_warnings(networks):
    warnings = []
    for n in networks:
        if n['Security'] == 'OPEN':
            warnings.append(f"[!] Network '{n['SSID']}' is OPEN and NOT SECURE!")
        elif n['Security'] == 'WEP':
            warnings.append(f"[!] Network '{n['SSID']}' uses WEP, which is insecure.")
    return warnings