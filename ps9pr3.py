import random

# 1
def create_dictionary(filename):
    # read the file
    file = open(filename)
    words = file.read().split()
    file.close()
    current_word = '$'                       # set up the first key
    dic = {}
    for next_word in words:                 # do loop in words with the first character
        if current_word not in dic:
            dic[current_word] = [next_word]
        else:
            dic[current_word] += [next_word]
        if '.' in next_word or '?' in next_word or '!' in next_word:
            current_word = '$'
        else:
            current_word = next_word
    return dic

# 2
def generate_text(word_dict, num_words):
    dic = create_dictionary(word_dict)
    # the last word
    former_w = random.choice(dic['$'])
    # the current word
    following_w = ''
    res_string = former_w
    for index in range(num_words - 1):
        if '.' in former_w or '?' in former_w or '!' in former_w:
            # the beginning of a sentence
            former_w = random.choice(dic['$'])
            res_string += ' ' + former_w
        else:
            # continue making the current sentence
            following_w = random.choice(dic[former_w])
            former_w = following_w
            res_string += ' ' + following_w
    return res_string

