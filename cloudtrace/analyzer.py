import json
import os
from datetime import datetime

class CloudTraceAnalyzer:
    def __init__(self, profile_name="default"):
        self.profile_name = profile_name
        self.anomalies_found = 0

    def parse_log_line(self, raw_line):
        """Parses a standard CloudTrail JSON log record entry."""
        try:
            record = json.loads(raw_line)
            event_name = record.get("eventName", "Unknown")
            event_source = record.get("eventSource", "Unknown")
            user_identity = record.get("userIdentity", {}).get("arn", "Unknown")
            error_code = record.get("errorCode", None)

            # Highlight potential target indicators
            is_anomaly = False
            if error_code in ["AccessDenied", "UnauthorizedOperation"]:
                is_anomaly = True
            elif event_name in ["AssumeRole", "CreateAccessKey", "DeleteLogGroup"]:
                is_anomaly = True

            if is_anomaly:
                self.anomalies_found += 1
                return {
                    "status": "ALERT",
                    "timestamp": record.get("eventTime", datetime.utcnow().isoformat()),
                    "source": event_source,
                    "event": event_name,
                    "actor": user_identity,
                    "details": f"Triggered by error: {error_code}" if error_code else "Sensitive API Call"
                }
            return {"status": "INFO", "event": event_name}
        except Exception:
            return {"status": "ERROR", "message": "Malformed log string entry"}

    def scan_file(self, file_path):
        """Scans an entire target log file for active infrastructure threats."""
        if not os.path.exists(file_path):
            print(f"[-] Target file {file_path} not found.")
            return

        print(f"[+] Scanning {file_path} using profile: [{self.profile_name}]...")
        alerts = []
        with open(file_path, "r") as f:
            for line in f:
                result = self.parse_log_line(line)
                if result.get("status") == "ALERT":
                    alerts.append(result)
        
        print(f"[+] Scan completed. Identified {self.anomalies_found} threat signatures.")
        return alerts
