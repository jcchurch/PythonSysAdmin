import subprocess, sys

infile = sys.argv[1]
command = "df -h /"

for line in file(infile):
    line = line.strip()
    [nick, address, port, username, keyfile] = line.split(",")
    fullCommand = "ssh -i %s -p %s %s@%s %s" %
                  (keyfile, port, username, address, command)
    subprocess.Popen(fullCommand.split(" "), shell=True)
