import sys
import fileinput

for file_name in sys.stdin:
    file_name = file_name.strip("\n ");

    if not file_name:
        continue

    for line in fileinput.input(file_name):
        print line