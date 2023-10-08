

def assigner(words):
    x = words[1]
    print(x)
    value = 4
    globals()[x]= value
    print(x)
    return x