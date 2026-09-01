import sys
import path_mod
import input_ui
import format_table
import ansi_utils

def main():

    # Get .ttf file from user input
    file_name = input_ui.get_file_name()

    output_option = input_ui.get_output_option()

    # Initialize output directory
    if output_option == "1":
        output_dir = path_mod.initialize_output_dir()
    elif output_option == "2":
        input_dir = input("Enter the path for your output directory: ")
        output_dir = path_mod.initialize_output_dir(input_dir)
        ansi_utils.move_cursor_up()
        ansi_utils.erase_line()
    
    table_option = input_ui.get_table_option()

    if table_option == "1":
        format_table.default_table_and_dir(file_name, output_dir)
    elif table_option == "2":
        format_table.custom_table(file_name, output_dir)

if __name__ == "__main__":
    main()
