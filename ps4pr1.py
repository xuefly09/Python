def dec_to_bin(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        binary_string = dec_to_bin(n//2)
        if n%2 == 0:
            return binary_string + '0'
        else:
            return binary_string + '1'

def bin_to_dec(b):
    if len(b) == 0:
        return 0
    else:
        decimal_num = bin_to_dec(b[1:])
        return decimal_num + int(b[0])*2**(len(b) - 1)

