import subprocess

def scan_open_ports():
    print("\n[*] Scanning open ports...")
    result = subprocess.run(
        ["ss", "-tuln"],
        capture_output=True,
        text=True
    )
    
    dangerous_ports = {
        22: "SSH - Remote login risk",
        23: "Telnet - Unencrypted risk",
        3389: "RDP - Remote desktop risk",
        11434: "Ollama AI - Exposed AI server"
    }
    
    findings = []
    
    for port, reason in dangerous_ports.items():
        if f":{port}" in result.stdout:
            findings.append(f"[WARNING] Port {port} open — {reason}")
    
    if findings:
        for f in findings:
            print(f)
    else:
        print("[SAFE] No dangerous ports detected")
    
    return findings
