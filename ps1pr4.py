def ends_match(s):
    a = s[0]
    b = s[-1]
    if a == b:
        return True
    else:
        return False
print(ends_match('h'))

def front3(s):
    length = len(s)
    if length <= 3:
        return s*3
    else:
        return s[:3]*3
print(front3('chocolate'))

def every_other(values):
    return values[::2]
print(every_other([1, 2, 3, 4, 5, 6, 7]))

def begins_with(word, prefix):
    if word[:len(prefix)] == prefix:
        return True
    else:
        return False
print(begins_with('computer', 'come'))

