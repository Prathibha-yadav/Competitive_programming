def isValid(s):
    dict = {'(':')','{':'}','[':']'}
    stack = []
    for i in s:
        if i in dict.keys():
            stack.append(i)
        elif len(stack) == 0 or i != dict[stack.pop()]:
            return False
    return len(stack) == 0

string = "(){}[()]"
print(isValid(string))