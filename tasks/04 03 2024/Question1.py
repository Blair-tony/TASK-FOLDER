# Read and Print the Contents of a Text File 

f = open(input("enter the path of file"), "rt") #input any text file path which needed to be read

print(f.read())

f.close()