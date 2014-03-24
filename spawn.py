import subprocess
import sys

if len(sys.argv) != 2:
    print "Requires 1 argument."
    sys.exit(1)

command = sys.argv[1]
subprocess.Popen(command, shell=True)
