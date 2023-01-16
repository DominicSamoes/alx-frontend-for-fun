#!/usr/bin/python3
"""
    Script changes Markdown to HTML
"""

import sys
from os import path
import re
import hashlib

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not path.exists(sys.argv[1]) or not str(sys.argv[1]).endswith(".md"):
        sys.stderr.write("Missing " + sys.argv[1] + '\n')
        exit(1)

    exit(0)
