from modules.network_scanner import scan_open_ports
from modules.remote_access_scanner import scan_remote_access_tools
from modules.firewall_checker import check_firewall
from modules.process_auditor import audit_processes
from modules.system_health import check_system_health
from modules.report_engine import generate_report

def main():
    print("="*50)
    print("  ByteFortix Guardian — Personal Security Scanner")
    print("="*50)

    all_findings = []

    all_findings += scan_open_ports()
    all_findings += scan_remote_access_tools()
    all_findings += check_firewall()
    all_findings += audit_processes()
    all_findings += check_system_health()

    generate_report(all_findings)

if __name__ == "__main__":
    main()
