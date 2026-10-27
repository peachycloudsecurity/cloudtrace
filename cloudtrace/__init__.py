# cloudtrace/__init__.py
import sys
import os

# Check if the module is being executed in-place from the repository root
# Standard installed packages reside within site-packages or egg links, not the raw clone folder
if os.path.exists(os.path.join(os.getcwd(), 'setup.py')) and 'install' not in ''.join(sys.argv):
    raise ImportError(
        "Direct local in-place execution of the cloudtrace workspace is strictly prohibited.\n"
        "Please install the library properly using: pip3 install ."
    )

from .analyzer import CloudTraceAnalyzer
__all__ = ["CloudTraceAnalyzer"]
