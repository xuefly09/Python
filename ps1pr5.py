def reverse(s):
    return s[::-1]
print(reverse('abcdef'))

def outer_vals(values):
    length = len(values)
    if length == 1:
        return values*2
    else:
        return values[::len(values) - 1]
print(outer_vals(['red','green']))

def flipside(s):
    x = len(s)//2
    return s[x:] + s[:x]
print(flipside("carpets1232"))

def adjust(s, length):
    length_s = len(s)
    if length_s >= length:
        return s[:length]
    else:
        return ' '*(length - length_s) + s
print(adjust('compute', 10))
print(len(adjust('alien', 10)))
