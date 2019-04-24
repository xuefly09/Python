def add_spaces(s):
    if len(s) == 0:
        return ''
    else:
        res_string = add_spaces(s[1:])
        return  ' ' + s[0] + res_string

def num_diff(s1, s2):
    if len(s1) == 0:
        return 0
    else:
        res_number = num_diff(s1[1:], s2[1:])
        if s1[0] != s2[0]:
            res_number += 1
        return res_number

def index(elem, seq):
    if len(seq) == 0:
        return -1
    elif elem == seq[0]:
        return 0
    else:
        position_count = index(elem, seq[1:])
        if position_count == -1:
            return -1
        else:
            return position_count + 1

def one_dna_to_rna(c):
    assert(len(c) == 1)
    list_DNA = ['A', 'C', 'G', 'T']
    list_RNA = ['U', 'G', 'C', 'A']
    if c in list_DNA:
        if c == 'A':
            return 'U'
        elif c == 'C':
            return 'G'
        elif c == "G":
            return 'C'
        else:
            return 'A'
    else:
        return ''

def  transcribe(s):
    if len(s) == 0:
        return ''
    else:
        res_RNA = transcribe(s[1:])
        return one_dna_to_rna(s[0]) + res_RNA