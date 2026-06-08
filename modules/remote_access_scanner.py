import subprocess

def scan_remote_access_tools():
    print("\n[*] Scanning for remote access tools...")
    
    tools = [
        "anydesk",
        "teamviewer", 
        "rustdesk",
        "vnc",
        "xrdp"
    ]
    
    findings = []
    
    for tool in tools:
        result = subprocess.run(
            ["ps", "aux"],
            capture_output=True,
            text=True
        )
        if tool in result.stdout.lower():
            findings.append(
                f"[WARNING] {tool} is running — unauthorized remote access risk"
            )
    
    if findings:
        for f in findings:
            print(f)
    else:
        print("[SAFE] No remote access tools detected")
    
    return findings
