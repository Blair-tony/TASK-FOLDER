# Write a Python program to read first n lines of a file.

f=open("C:\\Users\\HP\\OneDrive\\Documents\\python demo\\21 02 2024\\text file.txt","r")
n=n=int(input("no of lines to be printed : "))  
for i in range(0,n):
    line = f.readline().rstrip()
    print(line)