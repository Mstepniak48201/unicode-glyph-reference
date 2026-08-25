from pathlib import Path
import ascii_escape_utils

def get_file_name():
    file_name = input("Input the font file name: ")
    
    if Path(file_name).is_file():
        return file_name
    else: 
        while not Path(file_name).is_file():
            ascii_escape_utils.overwrite_line("File does not exist. ")
            file_name = input("Input the font file name: ")
        return file_name

def get_output_option():
    print("Enter the number for your output option.\n1 : Default output directory (./output_text_files)\n2 : Choose output directory")
    dir_option = input()

    if is_valid(dir_option):
        return dir_option
    else:
        while not is_valid(dir_option):
            ascii_escape_utils.erase_lines(4)
            print("Not a valid option! Enter the number for your output option.\n1 : Default output directory (./output_text_files)\n2 : Choose output directory")
            dir_option = input() 
        return dir_option


def get_table_option():
    print("Enter the number for your table option.\n1 : Default\n2 : Custom glyph table")
    table_option = input()

    if is_valid(table_option):
        return table_option
    else:
        while not is_valid(table_option):
            ascii_escape_utils.erase_lines(4)
            print("Not a valid option! Enter the number for your table option.\n1 : Default\n2 : Custom glyph table")
            table_option = input() 
        return table_option
    
# Utility functions
def is_valid(option):
    if option == "1" or option == "2":
        return True
    else:
        return False
