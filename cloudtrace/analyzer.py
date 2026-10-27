import json
import os

class CloudTraceAnalyzer:
    def __init__(self, profile_name="default"):
        self.profile_name = profile_name
        self.threat_signatures = {
            "CreateAccessKey": {"severity": "CRITICAL", "description": "Access key creation detected"},
            "DeleteAccessKey": {"severity": "CRITICAL", "description": "Access key deletion detected"},
            "DeleteUser": {"severity": "CRITICAL", "description": "IAM user deletion detected"},
            "PutBucketPolicy": {"severity": "HIGH", "description": "S3 bucket policy modification"},
            "CreateDBInstance": {"severity": "MEDIUM", "description": "Database instance creation"},
        }

    def scan_file(self, file_path):
        if not os.path.exists(file_path):
            print(f"[-] File {file_path} not found.")
            return []

        alerts = []
        print(f"[+] Scanning {file_path} successfully.")

        try:
            with open(file_path, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    if not line.strip():
                        continue
                    try:
                        event = json.loads(line)
                        threat = self._analyze_event(event)
                        if threat:
                            alerts.append(threat)
                    except json.JSONDecodeError:
                        print(f"[-] Failed to parse line {line_num}")
        except Exception as e:
            print(f"[-] Error scanning file: {e}")

        return alerts

    def _analyze_event(self, event):
        event_name = event.get("eventName", "")
        event_source = event.get("eventSource", "")
        user_arn = event.get("userIdentity", {}).get("arn", "Unknown")
        event_time = event.get("eventTime", "Unknown")
        error_code = event.get("errorCode")

        if event_name in self.threat_signatures:
            sig = self.threat_signatures[event_name]
            return {
                "timestamp": event_time,
                "event": event_name,
                "actor": user_arn,
                "details": f"{sig['description']} ({sig['severity']})",
                "source": event_source,
                "severity": sig['severity']
            }

        if error_code == "AccessDenied" and "GetObject" in event_name:
            return {
                "timestamp": event_time,
                "event": event_name,
                "actor": user_arn,
                "details": f"Unauthorized access attempt to {event_source} (MEDIUM)",
                "source": event_source,
                "severity": "MEDIUM"
            }

        return None
