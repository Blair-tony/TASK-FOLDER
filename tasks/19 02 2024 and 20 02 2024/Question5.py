#Write a Python program to implement a stack using a list.(push and pop) 

def create_stack():
    return [] #function initialize return empty list

def push(stack, item):
    stack.append(item) # function appends an item to the end of the stack list
    
def empty(stack):
    return len(stack) == 0 #function checks whether the stack is empty by checking its length

def peek(stack):
    if not empty(stack):
        return stack[-1] # returns the top element of the stack
    else:
        print("Stack is empty.")
        return None #checks if the stack is empty before starting

def pop(stack):
    if not empty(stack):
        return stack.pop() # removes and returns the top element
    else:
        print("Stack is empty.")
        return None # returns none if stack is empty 



stack = create_stack()
input = input("Enter the elements and add space : ")

    
elements = input.split()

    
for element in elements:
    push(stack, element)

print("Top element:", peek(stack)) # prints the top element of the stack using peek()

print("Popped elements:")

while not empty(stack):
        print(pop(stack)) # pops and prints all elements from the stack
