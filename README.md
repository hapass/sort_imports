# Script that sorts imports in files

The __sort.py__ script scans file paths from standard input, finds groups of lines with prefix __import__ separated by lines with any other content and sorts those groups in place.

The __sort.sh__ script gets changed files from git and passes file paths to __sort.py__.

The __test.sh__ script copies __*.test__ files, sorts imports in them, and compares them to corresponding __*.verify__ files. It prints out the status of comparison for sorted test files.