#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
#Sample Items : green-red-yellow-black-white 
#Expected Result : black-green-red-white-yellow

def hyphen(sequence):
    words = sequence.split('-')
    swords = sorted(words)
    ssequence = '-'.join(swords)

    return ssequence

inputs=input("enter the sequence")
ssequence=hyphen(inputs)
print(ssequence)