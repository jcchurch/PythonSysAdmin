import subprocess
import sys

# Lists the regular users on a system

command = "cat /etc/passwd"
process = subprocess.Popen(command.split(" "),
          stdin=subprocess.PIPE,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE)

(stdout, stderr) = process.communicate()

stdout = stdout.strip()
for line in stdout.split("\n"):
    parts = line.split(":")
    username = parts[0]
    userid = int(parts[2])

    if userid >= 1000 and userid <= 60000:
        print username
