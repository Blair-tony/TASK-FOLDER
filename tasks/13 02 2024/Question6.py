# Write a Python program to create Fibonacci series up to n using Lambda. 

# Fibonacci series upto 2: 

# [0, 1] 

# Fibonacci series upto 5: 

# [0, 1, 1, 2, 3] 

# Fibonacci series upto 6: 

# [0, 1, 1, 2, 3, 5] 

series= lambda n: [0, 1] if n == 2 else series(n - 1)+[series(n - 1)[-1]+series(n - 1)[-2]]

for n in [2,5,6]:
    print(series(n))