import sys
import subprocess
import os
from .cli import main

if sys.argv[1:2] == ['configure']:
    # Locate the external setup hook script path
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "bin", "configure.sh"))
    if os.path.exists(script_path):
        subprocess.run(["bash", script_path])
else:
    main()