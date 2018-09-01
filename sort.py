import fileinput
import sys

import_line_prefix = "import "

def readImportsGroup(changed_file):
    result = []
    while True:
        line = changed_file.readline()

        if not line.startswith(import_line_prefix):
            break

        if not line.endswith("\n"):
            line = line + "\n"

        result.append(line)

    return result

def writeImportsGroup(changed_file, imports):
    for import_line in imports:
        changed_file.write(import_line)

def sortImportsInGroup(changed_file, group_start_position):
    changed_file.seek(group_start_position)
    imports = readImportsGroup(changed_file)

    imports.sort(key=lambda x: x.translate(None, ".;").lower())

    changed_file.seek(group_start_position)
    writeImportsGroup(changed_file, imports)

def sortImportsInFile(changed_file_name):
    with open(changed_file_name, "r+") as changed_file:
        while True:
            line_start_position = changed_file.tell()
            line = changed_file.readline()

            if not line:
                break

            if line.startswith(import_line_prefix):
                sortImportsInGroup(changed_file, line_start_position)

for changed_file_name in sys.stdin:
    changed_file_name = changed_file_name.strip("\n ")

    try:
        sortImportsInFile(changed_file_name)
    except IOError:
        print "File cannot be processed: " + changed_file_name