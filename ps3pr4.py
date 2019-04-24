def sort_bits(bits):
    return [x for x in bits if x == 0] + [x for x in bits if x == 1]

def remove_chr(c, s2):
    if c == s2[0]:
        return s2[1:]
    else:
        res_string = remove_chr(c, s2[1:])
        return s2[0] + res_string

def jscore(s1, s2):
    if len(s1) == 0:
        return 0
    else:
        if s1[0] in s2:
            res_number = jscore(s1[1:], remove_chr(s1[0], s2)) + 1
        else:
            res_number = jscore(s1[1:], s2)
        return res_number

def lcs(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return ''
    else:
        if s1[0] == s2[0]:
            LCS = s1[0] + lcs(s1[1:], s2[1:])
        else:
            LCS_1 = lcs(s1[1:], s2)
            LCS_2 = lcs(s2[1:], s1)
            if len(LCS_1) > len(LCS_2):
                LCS = LCS_1
            else:
                LCS = LCS_2
        return LCS
