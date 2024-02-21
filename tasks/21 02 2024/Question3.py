# Write a Python program to append text to a file and display the text. 

f=open("C:\\Users\\HP\\OneDrive\\Documents\\python demo\\21 02 2024\\text file.txt","a")
f.write(input("enter string to be appended"))
f.close()

f=open("C:\\Users\\HP\\OneDrive\\Documents\\python demo\\21 02 2024\\text file.txt","rt")
print(f.read())