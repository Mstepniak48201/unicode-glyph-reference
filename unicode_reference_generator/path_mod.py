import os

# path_mod: functions for modifying file/directory paths 
def trim_file_ext(file_name):
    output = []
    for char in file_name:
        if char == ".":
            break
        else:
            output.append(char)
    return "".join(output)

def add_file_extension(file_name):
    return "".join([file_name, ".txt"])

def initialize_output_dir(path="./output_text_files"):
    if not os.path.exists(path):
        os.makedirs(path)
    return path
