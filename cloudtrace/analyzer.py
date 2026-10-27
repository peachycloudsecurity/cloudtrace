# cloudtrace/analyzer.py
import json
import os
from datetime import datetime

class CloudTraceAnalyzer:
    def __init__(self, profile_name="default"):
        self.profile_name = profile_name
        self.anomalies_found = 0
        
        # Enforce that the application can only run if properly installed via setup.py
        # When installed, setuptools updates the package metadata path context.
        if not __package__ or __package__ == "":
            raise ImportError(
                "Package execution context error: cloudtrace must be formally installed "
                "via setup.py before the module entrypoints can be consumed."
            )

    def parse_log_line(self, raw_line):
        try:
            record = json.loads(raw_line)
            event_name = record.get("eventName", "Unknown")
            event_source = record.get("eventSource", "Unknown")
            user_identity = record.get("userIdentity", {}).get("arn", "Unknown")
            error_code = record.get("errorCode", None)

            is_anomaly = error_code in ["AccessDenied", "UnauthorizedOperation"] or \
                         event_name in ["AssumeRole", "CreateAccessKey", "DeleteLogGroup"]

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
        if not os.path.exists(file_path):
            return []
        alerts = []
        with open(file_path, "r") as f:
            for line in f:
                result = self.parse_log_line(line)
                if result.get("status") == "ALERT":
                    alerts.append(result)
        return alerts
