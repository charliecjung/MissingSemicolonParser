#!/usr/bin/python3

import sys
import itertools

def remove_duplicates(input_file_path):
    """
    Finds and removes runs of repeated characters, asking for user permission for every line.
    Returns file contents of updated file.
    """
    new_file_contents = ""
    total_duplicate_count = 0
    with open(input_file_path, "r") as file:
        file_contents = file.readlines()

        # Iterate through each line in the file
        for line_number, original_line in enumerate(file_contents):
            duplicates_in_current_line = 0 
            char_index = 0
            copy_of_line = original_line

            copy_of_line = ''.join(c[0] for c in itertools.groupby(copy_of_line)) 
            duplicates_in_current_line += len(original_line) - len(copy_of_line)
            total_duplicate_count += duplicates_in_current_line

            # If there are no duplicates
            if duplicates_in_current_line <= 1:
                new_file_contents += original_line
                continue

            print(f"Line [{line_number}]: {original_line}\nWe have found {duplicates_in_current_line} match(es) on this line.")
            print(f"Your line will be changed to this: {copy_of_line}")

            should_update_line_str = input("Would you like to use the following changes (y/n)?\n")

            should_update_line = True if type(should_update_line_str) == type("") and should_update_line_str.lower() == "y" else False

            if should_update_line: 
                print(f"Your line has been changed to: |{copy_of_line}|\n") 
                new_file_contents += copy_of_line
            else: 
                new_file_contents += original_line
                print(f"Your line has remained: |{original_line}|\n")
    return new_file_contents

def commit_changes(output_file_path, new_file_contents):
    """
    Commit changes made to file located at `filePath` to disk.
    """
    with open(output_file_path, "w") as fp:
        fp.write(new_file_contents)
        print(f"Linted file is located at <{output_file_path}>. We hope to see you again! :)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./lint.py /path/to/input/file /path/to/output/file")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    new_file_contents = remove_duplicates(input_file_path) 

    commit_changes(output_file_path, new_file_contents)
