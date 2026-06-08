import subprocess

def check_system_health():
    print("\n[*] Checking system health...")

    findings = []

    # Check OS updates
    result = subprocess.run(
        ["apt", "list", "--upgradable"],
        capture_output=True,
        text=True
    )
    upgradable = [
        line for line in result.stdout.splitlines()
        if "upgradable" not in line and line.strip()
    ]
    if upgradable:
        findings.append(
            f"[WARNING] {len(upgradable)} packages need updates — unpatched system risk"
        )
        print(f"[WARNING] {len(upgradable)} packages need updates")
    else:
        print("[SAFE] System is up to date")

    # Check fail2ban
    result = subprocess.run(
        ["systemctl", "is-active", "fail2ban"],
        capture_output=True,
        text=True
    )
    if "active" not in result.stdout:
        findings.append("[WARNING] fail2ban is not running — brute force risk")
        print("[WARNING] fail2ban is not running — brute force risk")
    else:
        print("[SAFE] fail2ban is active — brute force protection on")

    # Check automatic updates
    result = subprocess.run(
        ["systemctl", "is-active", "unattended-upgrades"],
        capture_output=True,
        text=True
    )
    if "active" not in result.stdout:
        findings.append("[WARNING] Auto updates are off — manual patching required")
        print("[WARNING] Auto updates are off")
    else:
        print("[SAFE] Automatic updates are enabled")

    return findings
