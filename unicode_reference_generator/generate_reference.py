import os
import sys
from pathlib import Path
from fontTools import ttLib
import path_mod


def main():
    # Initialize output directory
    # Use variable for now because future feature will allow user to enter a custom path.
    output_dir = "./output_text_files"
    initialize_output_directory(output_dir)

    # Get .ttf file from user input
    file_name = get_file_name()

    # Change the file extension from the input .ttf file to .txt for the output file.
    trimmed_file_name = trim_file_ext(file_name)
    output_file_name = add_file_extension(trimmed_file_name)

    # Get reference to the font.
    font = ttLib.TTFont(file_name)

    # Get the cmap table (Python dict) from the font. Key: Value pairs are decimal_val: string_val
    font_cmap = font.getBestCmap()

    # Get glyph names
    glyph_names = get_glyph_names(font_cmap)

    # Decimal Unicode Points
    decimal_u_points = get_decimal_u_points(font_cmap)

    # Format Hex Unicode Escape Codes
    hex_u_points = get_hex_u_points(decimal_u_points)

    with open(f"{output_dir}/{output_file_name}", "a", encoding="utf-8") as f:
        f.write(f"Unicode Point  |  Glyph   |   Name\n") 
    
    for i in range(len(decimal_u_points)):
        with open(f"{output_dir}/{output_file_name}", "a", encoding="utf-8") as f:
            f.write(f"{hex_u_points[i]}             {chr(decimal_u_points[i])}          {glyph_names[i]}\n")


#Utility functions

def get_file_name():
    is_file = False
    file_name = input("Input the font file name: ")
    
    if Path(file_name).is_file():
        return file_name
    else: 
        while not Path(file_name).is_file():
            overwrite_line("File does not exist. ")
            file_name = input("Input the font file name: ")
        return file_name

def overwrite_line(text):
    sys.stdout.write("\x1b[K")
    sys.stdout.write("\r" + text)
    sys.stdout.flush()


def get_glyph_names(cmap):
    result = []
    for key in cmap:
        result.append(cmap[key])
    return result

def get_decimal_u_points(cmap):
    result = []
    for key in cmap:
        result.append(key)
    return result
            
def get_hex_u_points(decimal_u_points):
    # Return array of formatted hex u points.
    hex_result = []

    # Iterate over array of decimal u points.
    for dec in decimal_u_points:
        # Construct an array to be joined as string.
        str_result = []
        hex_point = hex(dec)
        if dec < 65536:
            str_result.append("\\u00")
            str_result.append(hex_point[2:])
        else:
            str_result.append("\\U0000")
            str_result.append(hex_point[2:])
        hex_result.append("".join(str_result))

    return hex_result

        

if __name__ == "__main__":
    main()
