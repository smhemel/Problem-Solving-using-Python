def to_hex(dec):

    hex_str = ''
    hex_digits = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
    rem = dec % 16

    while dec >= rem:
        remainder = dec % 16
        quotient = dec / 16
        if quotient == 0:
            hex_str += hex_digits[remainder]
        else:
            hex_str += str(remainder)
        dec = quotient

    return hex_str[::-1]
