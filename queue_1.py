max_len_queue = 5
queue = []
      
def dequeue():
    if (len(queue) <= 0):
        print("Queue is empty !!")
    else:
        queue.pop(0)
        print("First element removed.")
    return queue
def enqueue(queue, element):
    if(len(queue) >= max_len_queue):
        print("Queue is full !!")
    else:
        queue.append(element)
        print("Element added.")
    return queue
def display():
    return queue
def clear(queue):
    queue.clear()
    print("Queue cleared.")

menu = """
1. Add Element
2. Remove First Element
3. disply queue
4.clear queue
5. Quit
"""
print(menu)
while True:
    chance = int(input("Enter your choice: "))
    if (chance == 1):
        n = int(input("enter input: ")) 
        enqueue(queue, n)
    elif(chance == 2):
        dequeue()
    elif(chance == 3):
        print(display())
    elif(chance == 4):
        clear(queue)
    else:
        print("Quit")
        break
