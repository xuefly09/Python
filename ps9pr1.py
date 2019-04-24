# 
# ps9pr1.py - Problem Set 9, Problem 1
#
# String-method puzzles
#

s1 = 'Oh! How now brown cow!'
s2 = 'A maddening method to my MADNESS'

# Example puzzle (puzzle 0):
# Count all occurrences of the letter O (both lower- and upper-case) in s1.
answer0 = s1.lower().count('o')     
print('answer0 =', answer0)

# puzzle 1
answer1 = s2.lower().count('mad')
print('answer1 =', answer1)

# puzzle 2
answer2 = s1.split('w')
print('answer2 =', answer2)

# puzzle 3
answer3 = s2.upper().split('MAD')
print('answer3 =', answer3)

# puzzle 4
answer4 = s1.replace('ow', 'ee')
print('answer4 =', answer4)

# puzzle 5
answer5 = s2.lower().replace('m', 's')
print('answer5 =', answer5)