from fontTools import ttLib
import path_mod
import font_utils

def default_table_and_dir(file_name, output_dir):
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

    # Output index array and formatting output doc
    glyph_index = []
    # May need two arrays, or a better way of handling string/int conversions.
    for i in range(len(decimal_u_points)):
        glyph_index.append(i)

    column_len = get_column_len("Index", glyph_index, 3) 
    
    fld_name = "Index"
    fld_name_len = len(fld_name)
    fld_name_space = f"{(column_len - fld_name_len) * ' '}"

    # Format and write the output file: do not abstract into a function, yet. The index range/table columns feature(s) will
    # determine the structure.
    with open(f"{output_dir}/{output_file_name}", "a", encoding="utf-8") as f:
        f.write(f"{fld_name}{fld_name_space}|   Unicode Point  |  Glyph   |   Name\n") 
    
    for i in range(len(decimal_u_points)):
        val_space = f"{(column_len - len(str(glyph_index[i]))) * ' '}"
        with open(f"{output_dir}/{output_file_name}", "a", encoding="utf-8") as f:
            f.write(f"{glyph_index[i]}{val_space}        {hex_u_points[i]}         {chr(decimal_u_points[i])}          {glyph_names[i]}\n")

def get_column_len(fld_name, arr, space):
    str_fld_name = str(fld_name)
    str_arr = []
    for i in range(len(arr)):
        str_arr.append(str(arr[i]))
 
    max_el = max(str_arr, key=len)
    max_el_len = len(max_el)
    fld_name_len = len(str_fld_name)
    
    column_len = 0
    
    if fld_name_len > max_el_len:
        column_len = fld_name_len + space
    else:
        column_len = max_el_len + space
    return column_len
    
    
