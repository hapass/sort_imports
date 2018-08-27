import fileinput
import sys

debug = False
file_mask = ".hx"
import_line_prefix = "import "

for changed_file_name in sys.stdin:
    changed_file_name = changed_file_name.strip("\n ")

    if not changed_file_name or not changed_file_name.endswith(file_mask):
        continue

    with open(changed_file_name, "r+") as changed_file:
        lines_without_imports = []
        import_group_dictionary = {}

        inside_import_group = False
        current_import_group = 0

        for line_number, line in enumerate(changed_file.readlines()):
            if not inside_import_group and line.startswith(import_line_prefix):
                current_import_group = line_number
                import_group_dictionary[current_import_group] = []
                inside_import_group = True

            if inside_import_group and not line.startswith(import_line_prefix):
                inside_import_group = False

            if inside_import_group:
                import_group_dictionary[current_import_group].append(line)
                continue

            lines_without_imports.append(line)

        for import_group in import_group_dictionary.values():
            import_group.sort(key=lambda x: x.lower())

        total_import_lines = 0
        changed_file.seek(0)
        changed_file.truncate()

        for line_number, line in enumerate(lines_without_imports):
            def get_actual_line_number():
                return total_import_lines + line_number

            if get_actual_line_number() in import_group_dictionary:
                for import_line in import_group_dictionary[get_actual_line_number()]:
                    if debug:
                        print ("%d: %s" % (get_actual_line_number(), import_line))
                    else:
                        changed_file.write(import_line)

                    total_import_lines += 1

            if debug:
                print ("%d: %s" % (get_actual_line_number(), line))
            else:
                changed_file.write(line)