# Script that sorts imports in files

The __sort.py__ script scans file paths from standard input, finds groups of lines with prefix __import__ separated by lines with any other content and sorts those groups in place. Sorting routine compares lines using their lowercased copies that are also stripped of dots and semicolons - see tests for examples. Line prefixes are hardcoded to be __import__ as in haxe source code files.

The __sort_changed.sh__ script gets changed files from __git__ and passes file paths to __sort.py__. It filters out __*.hx__ files, which are haxe source code files. Warning: it will add all files to git before operating, which might be not what you wanted, but as a result you will be able to see exactly what changes the script did to your files.

The __sort_diff.sh__ script is designed to be applied, when you have already committed all the work to your feature branch, and want to sort the imports as a possible refactoring. Make sure you don't have any changes hanging and run the script, it will take all files from branch diff with develop, filter out __*.hx__ files, and run the script on them. If one of the files was deleted, it will show a warning for the particular file and continue to sort the rest.

The __test.sh__ script copies __*.test__ files, sorts imports in them, and compares them to corresponding __*.verify__ files. It prints out the status of comparison for sorted test files.

If you found a bug, please create an issue with issue reproduced in __issue_name.test__ file and expected result in __issue_name.verify__ files attached.