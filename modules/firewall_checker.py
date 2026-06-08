import subprocess

def check_firewall():
    print("\n[*] Checking firewall status...")

    result = subprocess.run(
        ["sudo", "ufw", "status"],
        capture_output=True,
        text=True
    )

    if "inactive" in result.stdout.lower():
        print("[CRITICAL] Firewall is OFF — your system is fully exposed")
        return ["Firewall inactive"]

    findings = []

    risky_ports = {
        "22": "SSH open to everyone — brute force risk",
        "23": "Telnet open — unencrypted traffic",
        "3389": "RDP open — remote desktop exposed",
        "11434": "Ollama AI open to everyone — data exposure"
    }

    for port, reason in risky_ports.items():
        if port in result.stdout and "ALLOW" in result.stdout:
            findings.append(f"[WARNING] Port {port} — {reason}")

    if findings:
        for f in findings:
            print(f)
        print("\n[SUGGESTION] Restrict these ports to trusted IPs only")
    else:
        print("[SAFE] Firewall rules look clean")

    return findings
