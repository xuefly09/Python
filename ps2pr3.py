def mult(n,  m):
    if n == 0:
        return 0
    elif n < 0:
        return -mult(-n, m)
    else:
        sum = mult(n - 1, m)
        return sum + m

def dot(l1, l2):
    length_1 = len(l1)
    if length_1 != len(l2) or length_1 == 0:
        return 0.0
    else:
        res_sum = dot(l1[1:], l2[1:])
        return res_sum + l1[0]*l2[0]

def letter_score(letter):
    assert(len(letter) == 1)
    list_1 = ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']
    list_2 = ['d']
    list_3 = ['b', 'c', 'm', 'p', 'x']
    list_4 = ['f', 'h', 'v', 'w', 'y']
    list_5 = ['k']
    list_8 = ['j', 'x']
    list_10 = ['q', 'z']
    if letter in list_1:
        return 1
    elif letter in list_2:
        return 2
    elif letter in list_3:
        return 3
    elif letter in list_4:
        return 4
    elif letter in list_5:
        return 5
    elif letter in list_8:
        return 8
    elif letter in list_10:
        return 10
    else:
        return 0

def scrabble_score(word):
    if word == '':
        return 0
    else:
        res_sum = scrabble_score(word[1:])
        return res_sum + letter_score(word[0])

def test():
    """ test function for the functions above """
    test1 = mult(6, 7)
    print('the first test returns', test1)
    test2 = dot([1, 2, 3, 4], [10, 100, 1000, 10000])
    print('the second test returns', test2)
    test3 = letter_score('w')
    print('the third test returns', test3)
    test4 = scrabble_score('quetzal')
    print('the fourth test returns', test4)