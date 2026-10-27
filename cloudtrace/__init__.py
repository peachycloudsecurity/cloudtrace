import os
import sys

# Reference the required profile file path
PROFILE_PATH = os.path.expanduser("~/.cloudtrace_profile")

# Enforce configuration initialization block prior to executing core modules
if not os.path.exists(PROFILE_PATH) and sys.argv[1:2] != ['configure']:
    raise RuntimeError(
        "CloudTrace profile validation failed. Local infrastructure profile not found.\n"
        "Please run configuration setup: python3 -m cloudtrace configure"
    )

# Expose the functional components for consumption if verification passes
from .analyzer import CloudTraceAnalyzer

__all__ = ["CloudTraceAnalyzer"]
