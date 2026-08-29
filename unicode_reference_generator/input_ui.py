from pathlib import Path
import ascii_escape_utils

def get_file_name():
    file_name = input("Input the font file name: ")
    
    if Path(file_name).is_file():
        return file_name
    else: 
        while not Path(file_name).is_file():
            ascii_escape_utils.move_cursor_up()
            ascii_escape_utils.overwrite_line("File does not exist. ")
            file_name = input("Input the font file name: ")
        ascii_escape_utils.move_cursor_up()
        ascii_escape_utils.erase_line()
        return file_name
        

def get_output_option():
    print("Enter the number for your output option.\n1 : Default output directory (./output_text_files)\n2 : Choose output directory")
    dir_option = input()

    if is_valid(dir_option):
        ascii_escape_utils.erase_lines(4)
        return dir_option
    else:
        while not is_valid(dir_option):
            ascii_escape_utils.erase_lines(4)
            print("Not a valid option! Enter the number for your output option.\n1 : Default output directory (./output_text_files)\n2 : Choose output directory")
            dir_option = input() 
        
        ascii_escape_utils.erase_lines(4)
        return dir_option

def get_table_option():
    print("Enter the number for your table option.\n1 : Default\n2 : Custom glyph table")
    table_option = input()

    if is_valid(table_option):
        ascii_escape_utils.erase_lines(4)
        return table_option
    else:
        while not is_valid(table_option):
            ascii_escape_utils.erase_lines(4)
            print("Not a valid option! Enter the number for your table option.\n1 : Default\n2 : Custom glyph table")
            table_option = input() 
        ascii_escape_utils.erase_lines(4)
        return table_option

def get_custom_table_range(glyph_arr):
    input_range = input("Enter the comma-separated (start_index, end_index) index range of the glyphs you want to examine: ") 
    split_input = input_range.split(", ", 1)
    max_index = len(glyph_arr) - 1

    if is_index(split_input, max_index):
        return is_index(split_input, max_index)
    else:
        while not is_index(split_input, max_index):
            input_range = input("Not a valid range! Enter the comma-separated (start_index, end_index) index range of the glyphs you want to examine:  ")
            split_input = input_range.split(", ", 1)
        return is_index(splite_input, max_index)
             
# Utility functions
def is_valid(option):
    if option == "1" or option == "2":
        return True
    else:
        return False

def is_index(arr, max_index):
    print("is_index called!")
    index_arr = []
    if len(arr) != 2:
        return False
    for el in arr:
        is_digit = el.isdigit()
        if not is_digit:
            return False
        if int(el) < 0 or int(el)> max_index:
            return False
        index_arr.append(int(el))
    return index_arr




