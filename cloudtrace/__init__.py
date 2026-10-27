import os
import sys

TOKEN = os.path.expanduser("~/.cloudtrace_token")

if not os.path.exists(TOKEN) and sys.argv[1:2] != ['configure']:
    raise RuntimeError(
        "CloudTrace local profiling engine not initialised.\n"
        "Run: python3 -m cloudtrace configure"
    )
