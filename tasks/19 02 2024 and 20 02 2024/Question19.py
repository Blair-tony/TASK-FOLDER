# Write a Python program to count the number of vowels in a string.

sentence = input("Enter any string:")
sentence = sentence.lower()
count = 0
for i in sentence:
    if i == "a" or i == "e" or i == "i" or i == "o" or i =="u":
        count = count + 1 
print("Total vowel count : ",count) # if the vowels are found then count is incremented to +1

vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0} # initializes the counts for each vowel to 0

for char in sentence:
    if char in vowel_count: #iterates through each character in the sentence
        vowel_count[char] += 1 # updates the count for the respective vowel 

for vowel, count in vowel_count.items():
    print(f"Number of '{vowel}'in string : {count}")