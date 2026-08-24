from fontTools import ttLib
import path_mod

# font_utils: functions for extracting and modifying data from .ttf files
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

def get_font_data(file_name):
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

    # Output index array and formatting output doc
    glyph_index = []
    for i in range(len(decimal_u_points)):
        glyph_index.append(i)

    font_data = {
        "font_cmap": font_cmap,
        "glyph_names": glyph_names,
        "decimal_u_points": decimal_u_points,
        "hex_u_points": hex_u_points,
        "index": glyph_index
    }

    return font_data    
