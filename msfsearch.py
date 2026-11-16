import re
import subprocess
import sys

def banner():
    return r"""
                   ____                                __
   ____ ___  _____/ __/     ________  ____ ___________/ /_
  / __ `__ \/ ___/ /_______/ ___/ _ \/ __ `/ ___/ ___/ __ \
 / / / / / (__  ) __/_____(__  )  __/ /_/ / /  / /__/ / / /
/_/ /_/ /_/____/_/       /____/\___/\__,_/_/   \___/_/ /_/

"""

print(banner())

if len(sys.argv) < 2:
    search_term = input("Enter search term: ").strip()
else:
    search_term = " ".join(sys.argv[1:]).strip()

if not search_term:
    print("A search term is required.")
    sys.exit(1)

if not re.fullmatch(r"[A-Za-z0-9 _-]+", search_term):
    print("Use only letters, numbers, spaces, underscores, or hyphens.")
    sys.exit(1)

subprocess.run(
    ["msfconsole", "-q", "-x", f"search {search_term}; exit"],
    check=False,
)
