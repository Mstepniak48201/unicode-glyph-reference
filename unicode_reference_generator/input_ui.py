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
    print("Enter the number for your output option.\n1 : Default table and output directory\n2 : Custom table, default output directory\n3 : Custom table and custom output directory")
    option = input()
    return option
