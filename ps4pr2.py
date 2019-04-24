from ps4pr1 import *

def mul_bin(b1, b2):
    b1_decimal = bin_to_dec(b1)
    b2_decimal = bin_to_dec(b2)
    return dec_to_bin(b1_decimal*b2_decimal)

def add_bytes(b1, b2):
    b1_decimal = bin_to_dec(b1)
    b2_decimal = bin_to_dec(b2)
    res_bin = dec_to_bin(b1_decimal + b2_decimal)
    if len(res_bin) < 8:
        return (8 - len(res_bin))*'0' + res_bin
    else:
        return res_bin[1:]

