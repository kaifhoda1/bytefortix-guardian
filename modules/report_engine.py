from datetime import datetime

def generate_report(findings):
    print("\n" + "="*50)
    print("  ByteFortix Guardian — Security Report")
    print("="*50)
    print(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Total Issues Found: {len(findings)}")
    print("="*50)

    if not findings:
        print("\n[✓] Your system looks clean. Stay vigilant.")
        return

    print("\n[!] Issues Detected:\n")
    for i, finding in enumerate(findings, 1):
        print(f"  {i}. {finding}")

    print("\n[!] Suggestions:\n")
    suggestions = {
        "22": "Restrict SSH — run: sudo ufw allow from YOUR_IP to any port 22",
        "11434": "Restrict Ollama — run: sudo ufw delete allow 11434",
        "updates": "Update system — run: sudo apt upgrade",
        "fail2ban": "Install fail2ban — run: sudo apt install fail2ban",
        "remote": "Remove remote access tools if not needed"
    }

    for key, suggestion in suggestions.items():
        for finding in findings:
            if key in finding.lower():
                print(f"  → {suggestion}")

    print("\n" + "="*50)
    print("  Stay secure. ByteFortix Guardian.")
    print("="*50)
