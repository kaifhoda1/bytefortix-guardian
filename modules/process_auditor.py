import subprocess
import re

def audit_processes():
    print("\n[*] Auditing running processes...")

    suspicious = [
        "netcat", "nc", "ncat",
        "wireshark", "tcpdump",
        "keylogger", "xspy",
        "anydesk", "teamviewer",
        "ngrok", "reverse"
    ]

    result = subprocess.run(
        ["ps", "aux"],
        capture_output=True,
        text=True
    )

    findings = []

    for process in suspicious:
        if re.search(rf'\b{process}\b', result.stdout.lower()):
            findings.append(
                f"[WARNING] Suspicious process detected — {process}"
            )

    if findings:
        for f in findings:
            print(f)
    else:
        print("[SAFE] No suspicious processes detected")

    return findings
