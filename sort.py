import sys
import fileinput

for changed_file_name in sys.stdin:
    changed_file_name = changed_file_name.strip("\n ")

    if not changed_file_name:
        continue

    with open(changed_file_name, "r+") as changed_file:
        lines = changed_file.readlines()

        lines_without_import_groups = []
        import_group_dictionary = {}

        inside_import_group = False
        current_import_group = 0

        for line_number, line in enumerate(lines):
            if not inside_import_group and line.startswith("import "):
                current_import_group = line_number
                import_group_dictionary[current_import_group] = []
                inside_import_group = True

            if inside_import_group and not line.startswith("import ") and line.strip("\n "):
                inside_import_group = False

            if inside_import_group:
                import_group_dictionary[current_import_group].append(line)
                continue

            lines_without_import_groups.append(line)

        for import_group in import_group_dictionary.values():
            import_group.sort()

        for line_number, line in enumerate(lines_without_import_groups):
            if line_number in import_group_dictionary:
                for import_line in import_group_dictionary[line_number]:
                    print import_line

            print line



