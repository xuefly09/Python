__author__ = 'Jeffrey'

# 1
def add_spaces(s):
    res = ''
    for val in s:
        val += ' '
        res += val
    return res[:-1]

# 2
def num_diff(s1, s2):
    the_longer = ''
    the_shorter = ''
    difference = 0
    if len(s1) >= len(s2):
        the_longer = s1
        the_shorter = s2
        difference = len(s1) - len(s2)
    else:
        the_longer = s2
        the_shorter = s1
        difference = len(s2) - len(s1)
    for index in range(len(the_shorter)):
        if the_longer[index] != the_shorter[index]:
            difference += 1
    return difference

# 3
def index(elem, seq):
    for i in range(len(seq)):
        if elem == seq[i]:
            return i
    return -1


