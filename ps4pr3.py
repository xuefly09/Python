def bitwise_and(b1, b2):
    if len(b1) == 0:
        return len(b2)*'0'
    elif len(b2) == 0:
        return len(b1)*'0'
    else:
        res_bitwise = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == '1' and b2[-1] == '1':
            return res_bitwise + '1'
        else:
            return res_bitwise + '0'

def add_bitwise(b1, b2):
    if len(b1) == 0:
        return b2
    elif len(b2) == 0:
        return b1
    else:
        res_add = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == b2[-1]:
            if b1[-1] == '0':
                return res_add + '0'
            else:
                return add_bitwise(res_add, '1') + '0'
        else:
            return res_add + '1'