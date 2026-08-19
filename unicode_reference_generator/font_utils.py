from fontTools import ttLib

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
