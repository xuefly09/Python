def mystery2(s):
    """ takes a string s and does something with it """
    if len(s) <= 1:
        return s
    else:
        result_rest = mystery2(s[1:])
        if s[0] == s[-1]:
            return result_rest
        else:
            return result_rest + s[0]


test = 'xuefly09'

print(test[3:2:1])
print([1, 2, 3] + [[11, 13, 12][1]] + [22, 33, 44, 55][1:])
