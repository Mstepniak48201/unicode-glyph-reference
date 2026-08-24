from fontTools import ttLib
import path_mod
import font_utils

def default_table_and_dir(file_name, output_dir):
    # Change the file extension from the input .ttf file to .txt for the output file.
    trimmed_file_name = path_mod.trim_file_ext(file_name)
    output_file_name = path_mod.add_file_extension(trimmed_file_name)

    # Get font data
    font_data = font_utils.get_font_data(file_name)
    glyph_names = font_data["glyph_names"]
    decimal_u_points = font_data["decimal_u_points"]
    hex_u_points = font_data["hex_u_points"]
    glyph_index = font_data["index"]
      
    fld_name = "Index"
    column_len = get_column_len(glyph_index, 3, fld_name) 
    fld_name_len = len(fld_name)
    fld_name_padding = get_padding(column_len, fld_name)

    hex_column_len = get_column_len(hex_u_points, 3)
    name_column_len = get_column_len(glyph_names, 3, "Name")

    # Format and write the output file: do not abstract into a function, yet. The index range/table columns feature(s) will
    # determine the structure.
    with open(f"{output_dir}/{output_file_name}", "a", encoding="utf-8") as f:
        f.write(f"{fld_name}{fld_name_padding}|   Unicode Point  |  Name              |   Glyph\n") 
    
    for i in range(len(glyph_index)):
        index_padding = get_padding(column_len, glyph_index[i])
        padding_left = "    "
        hex_padding = get_padding(hex_column_len, hex_u_points[i])
        name_padding = get_padding(name_column_len, glyph_names[i])
        
        with open(f"{output_dir}/{output_file_name}", "a", encoding="utf-8") as f:
            f.write(
                f"{glyph_index[i]}{index_padding}"
                f"{padding_left}{hex_u_points[i]}{hex_padding}"
                f"{padding_left}{glyph_names[i]}{name_padding}"
                f"{padding_left}{chr(decimal_u_points[i])}\n"
            )

# def custom_table(file_name, output_dir):




# Utility Functions
def get_column_len(arr, space, fld_name=""):
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
    
def get_padding(column_len, el):
    el_len = len(str(el))
    return f"{(column_len - el_len) * ' '}"

    
