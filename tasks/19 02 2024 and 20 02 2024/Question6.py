# Write a Python program to implement a queue using a list.(enqueue and dequeue) 


queue = []

num_elements = int(input("Enter the number of elements for the queue: "))
print("Enter the elements for the queue:")
for _ in range(num_elements):
    element = input()
    queue.append(element)

print("Initial queue:")
print(queue)

dequeue = []
while queue:
    dequeue.append(queue.pop(0))


print("\nElements dequeued from the queue:")
for element in dequeue:
    print(element)

print("\nQueue after removing elements:")
print(queue)
