def abs_list_lc(values):
    return [abs(x) for x in values]

def abs_list_rec(values):
    if len(values) == 0:
        return print('values is empty!')
    if len(values) == 1:
        return [abs(values[0])]
    else:
        res_list = abs_list_lc(values[1:])
        return [abs(values[0])] + list(res_list)

def num_factors(x):
    if x == 0:
        print('Zero doesn\'t have factors!' )
    else:
        abs_x = abs(x)
        factors_list = [i for i in range(1, abs_x + 1) if abs_x%i == 0]
        return len(factors_list)

def most_factors(values):
    number_list = [[num_factors(x), x] for x in values]
    return max(number_list)[1]