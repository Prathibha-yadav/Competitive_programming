max_len_stack = 5
stack = []
           
def pop():
    if(len(stack) <= 0):
        print("Stack is Empty !!")
    else:
        stack.pop()
        print("Removed last element.")
    return stack
def append(stack, element):
    if(len(stack) >= max_len_stack):
        print("Stack is full !!")
    else:
        stack.append(element)
    return stack
def clear(stack):
    stack.clear()
    print("Stack Cleared.")
def display(stack):
    print(stack,end = " ")

menu = """
1. Add Element
2. Remove Last Element
3. disply stack
4.Clear
5. Quit
"""
print(menu)
while True:
    chance = int(input("Enter our choice: "))
    if (chance == 1):
        n = int(input("enter input: ")) 
        append(stack, n)
    elif(chance == 2):
        pop()
    elif(chance == 3):
        display(stack)
    elif(chance == 4):
        clear(stack)
    else:
        print("Quit")
        break
