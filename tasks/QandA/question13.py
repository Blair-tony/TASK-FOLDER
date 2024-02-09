# #print the following patterns
# (a)
# 	          *
#            * *
#           * * *
#          * * * *

# (b)   o
# 		1 2
# 		3 4 5
# 		6 7 8 9


# (c)	o
# 		1 1
# 		2 2 2
# 		3 3 3 3

# (d)	*
# 		* *
# 		* * *
# 		* * * *

#a)
for i in range(0,5):
    for j in range(0,5-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

#b)
num=0
for i in range(0,5):
        for j in range(1, i + 1):
            print(num, end=" ")
            num +=1
        print()

#c)
for i in range(0,4):
    for j in range(-1,i):
        print(i,end=" ")
    print()

#d)
for i in range(0,5):
    for j in range(0,i):
        print("*",end=" ")
    print()