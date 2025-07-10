SECURITY_EXPLANATIONS = {
    "OPEN": "No password protection. Anyone can join. Not secure.",
    "WEP": "WEP is outdated and insecure. Avoid using.",
    "WPA": "WPA is better than WEP but still vulnerable.",
    "WPA2": "WPA2 is currently the standard for secure WiFi.",
    "WPA3": "WPA3 is the latest and most secure standard."
}

SECURITY_TIPS = [
    "Prefer WPA2 or WPA3 for your WiFi security.",
    "Change default router passwords.",
    "Disable WPS if not needed.",
    "Use strong, unique passwords.",
    "Place your router centrally to minimize signal leakage."
]

def print_security_explanations():
    print("\nWiFi Security Types Explained:")
    for sec, expl in SECURITY_EXPLANATIONS.items():
        print(f"  {sec}: {expl}")

def print_security_tips():
    print("\nTips for Improving WiFi Security:")
    for tip in SECURITY_TIPS:
        print(f"  - {tip}")
