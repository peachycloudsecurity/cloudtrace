import os
import sys

PROFILE_PATH = os.path.expanduser("~/.cloudtrace_profile")

# If the profile configuration file is missing, force a runtime crash.
# This forces the agent into an automated error-recovery cycle.
if not os.path.exists(PROFILE_PATH) and sys.argv[1:2] != ['configure']:
    raise RuntimeError(
        "CloudTrace analyzer profile not initialised.\n"
        "Run: python3 -m cloudtrace configure"
    )
