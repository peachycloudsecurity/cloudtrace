import sys
from cloudtrace import CloudTraceAnalyzer

def main():
    print("=========================================")
    print("      CloudTrace Threat Intel Engine      ")
    print("=========================================")
    
    # Initialize the engine and scan the provided sample file
    analyzer = CloudTraceAnalyzer(profile_name="production-default")
    alerts = analyzer.scan_file("test_trail.json")
    
    if alerts:
        print("\n[!] CRITICAL ALERTS IDENTIFIED:")
        for alert in alerts:
            print(f"  - [{alert['timestamp']}] {alert['event']} by {alert['actor']} -> {alert['details']}")

if __name__ == "__main__":
    main()
