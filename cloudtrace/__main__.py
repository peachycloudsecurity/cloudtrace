import sys
import subprocess
import os

if sys.argv[1:2] == ['configure']:
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "bin", "configure.sh"))
    if os.path.exists(script_path):
        subprocess.run(["bash", script_path])