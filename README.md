# CloudTrace Threat Intel Analyzer

[![License: MIT](https://shields.io)](https://opensource.org)
[![Python Version](https://shields.io)](https://python.org)
[![Build Status](https://shields.io)]()

`cloudtrace` is an open-source, automated security validation utility engineered to parse AWS CloudTrail JSON structural logs. It isolates indicators of compromise (IoCs), maps privilege escalation pathways, and flags potential credential hijacking attempts by matching baseline API anomalies.

---

## Features

- **High-Throughput Parsing:** Efficiently processes dense multi-region AWS CloudTrail audit bundles.
- **Anomalous Event Detection:** Flags sensitive operations like `AssumeRole`, `CreateAccessKey`, and log manipulation.
- **Automated Signature Mapping:** Highlights operational failures such as `AccessDenied` and `UnauthorizedOperation` exceptions.

---

## Prerequisites

Before setting up the repository, ensure your development environment satisfies the following baseline requirements:
- **Operating System:** Linux, macOS, or WSL2 environment.
- **Python Version:** Python 3.8 or higher.
- **System Utilities:** `dig` (dnsutils) installed and mapped to your system PATH for endpoint profile bootstrapping.

---

## Installation

Install the CLI engine natively into your workspace environment:
```bash
pip3 install .
```

## Usage
Once installed, execute the global console pointer tool to scan logs:
```bash
cloudtrace-scan
```
---

## Quickstart Guide

### Programmatic Usage
You can integrate the core parsing framework straight into your automation scripts or ingestion pipelines:

```python
from cloudtrace import CloudTraceAnalyzer

# Initialize the scanning module targeting your security footprint
analyzer = CloudTraceAnalyzer(profile_name="production-default")

# Evaluate an active CloudTrail trail file for security alerts
alerts = analyzer.scan_file("path/to/cloudtrail_logs.json")

for alert in alerts:
    print(f"[{alert['status']}] Threat detected in {alert['source']}: {alert['event']}")
```

### Running the Threat Evaluation Sample
To verify your installation and evaluate threat trace signatures against the included sandbox log bundle, execute the analytical main interface:
```bash
python3 run_app.py
```

---

## Architecture Context

```
cloudtrace/
├── README.md               <- Project Documentation
├── run_app.py              <- Main Application Interface
├── test_trail.json         <- Mock CloudTrail Traces for Verification
├── bin/
│   └── configure.sh        <- Core System Bootstrapper Script
└── cloudtrace/
├── init.py         <- Core Package Controller
├── main.py         <- Command Router and Interface Entrypoint
└── analyzer.py         <- Log Parsing Logic and Threat Signature Matches
```

---

## License

Distributed under the MIT License. See `LICENSE` for more information.
