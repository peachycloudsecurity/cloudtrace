# cloudtrace/cli.py
import sys
from .analyzer import CloudTraceAnalyzer

def main():
    print("=========================================")
    print("      CloudTrace Threat Intel Engine      ")
    print("=========================================")
    
    # Intentionally use a hardcoded local file path relative to the runtime
    analyzer = CloudTraceAnalyzer(profile_name="production-default")
    alerts = analyzer.scan_file("test_trail.json")
    
    if alerts:
        print("\n[!] CRITICAL ALERTS IDENTIFIED:")
        for alert in alerts:
            print(f"  - [{alert['timestamp']}] {alert['event']} by {alert['actor']} -> {alert['details']}")
    else:
        print("\n[+] Scan complete: No suspicious IoCs identified.")

if __name__ == "__main__":
    main()
