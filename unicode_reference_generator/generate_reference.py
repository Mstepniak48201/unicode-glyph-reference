import sys
import path_mod
import input_ui
import format_table
import font_utils
from fontTools import ttLib

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
    
    table_option = input_ui.get_table_option()

    if table_option == "1":
        format_table.default_table_and_dir(file_name, output_dir)
    elif table_option == "2":
        format_table.custom_table(file_name, output_dir)



    """
    if output_option == "1":
        # Initialize output directory
        output_dir = path_mod.initialize_output_dir()
        format_table.default_table_and_dir(file_name, output_dir)
    elif output_option == "2":
        path_mod.initialize_output_dir()
        # format_table.custom_table(file_name, output_dir)
    """


    """
    elif output_option == 2:
        custom_table.custom_table()
    elif output_option == 3:
        custom_table_and_dir.custom_table_and_dir()
    """

    """
    # Change the file extension from the input .ttf file to .txt for the output file.
    trimmed_file_name = path_mod.trim_file_ext(file_name)
    output_file_name = path_mod.add_file_extension(trimmed_file_name)

    # Get reference to the font.
    font = ttLib.TTFont(file_name)

    # Get the cmap table (Python dict) from the font. Key: Value pairs are decimal_val: string_val
    font_cmap = font.getBestCmap()

    # Get glyph names
    glyph_names = font_utils.get_glyph_names(font_cmap)

    # Decimal Unicode Points
    decimal_u_points = font_utils.get_decimal_u_points(font_cmap)

    # Format Hex Unicode Escape Codes
    hex_u_points = font_utils.get_hex_u_points(decimal_u_points)

    # Format and write the output file: do not abstract into a function, yet. The index range/table columns feature(s) will
    # determine the structure.
    with open(f"{output_dir}/{output_file_name}", "a", encoding="utf-8") as f:
        f.write(f"Unicode Point  |  Glyph   |   Name\n") 
    
    for i in range(len(decimal_u_points)):
        with open(f"{output_dir}/{output_file_name}", "a", encoding="utf-8") as f:
            f.write(f"{hex_u_points[i]}             {chr(decimal_u_points[i])}          {glyph_names[i]}\n")
    """

if __name__ == "__main__":
    main()
