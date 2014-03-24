import subprocess
import sys

# Count the lines across all
# text files supplied by an argument.

if len(sys.argv) != 2:
    print "Requires 1 argument."
    sys.exit(1)

command = "wc -l %s" % (sys.argv[1])
subprocess.Popen(command, shell=True)
