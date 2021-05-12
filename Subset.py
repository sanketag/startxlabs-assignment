"""#1 Function with set difference method"""

def fun1(words):
    left = set(words[0].lower())
    right = set(words[1].lower())
    if len(right-left)==0:return True
    else:return False

print(fun1(['Hello','he']))



"""#2 Function with all function method"""

def fun2(words):
    left = set(words[0].lower())
    right = set(words[1].lower())
    if all(_ in left for _ in right):return True
    else:return False

print(fun2(['Alien','line']))



"""#3 Function with looping method"""

def fun3(words):
    left = set(words[0].lower())
    right = set(words[1].lower())
    while(len(right)>0):
        if right.pop() in left:pass
        else:return False
    return True

print(fun3(['ReQuIrEd','Rest']))



"""#4 Function with subset method"""

def fun4(words):
    left = set(words[0].lower())
    right = set(words[1].lower())
    if right.issubset(left):return True
    else:return False

print(fun4(['Yes','No']))



""" left is set of first string with unique alphabets """
""" right is set of second string with unique alphabets """
