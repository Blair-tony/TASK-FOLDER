# 3) print the following patterns: 

# a) 
# 0 
# 0 0 
# 0 0 0 
# 0 0 0 0 

# b) 
#     * 
#   * * * 
#  * * * * * 
# * * * * * * * 

# c) 
# 0 
# 1 1 
# 2 2 2 
# 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 5 

# d) 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# e) 
# * * * * * * 
# * * * * * 
# * * * * 
# * * *  
# * * 
# * 

# f) 
# @ @ @ @ @ @ @ 
# @ @ @ @ @ @ @ 
# @ @ @ @ @ @ @ 
# @ @ @ @ @ @ @


#a)
for i in range(1,5):
    for j in range(0,i):
        print(0,end=" ")
    print()

#b)
for i in range(0,4):
    for j in range(0,5-i-1):#this loop is to create spaces
        print(" ",end=" ")
    for j in range(0,2* i + 1):#this loop is to print stars in odd number
        print("*",end=" ")
    print()

#c)
for i in range(0,6):
    for j in range(-1,i):
        print(i,end=" ")
    print()

#d)
for i in range(0,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#e)
for i in range(1,7):
    for j in range(7-i,0,-1):
        print("*",end=" ")
    print()

#f)
for i in range(0,4):
    for j in range(0,7):
        print("@",end=" ")
    print()