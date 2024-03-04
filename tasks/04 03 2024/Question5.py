# Implement a program that reads a text file and counts the occurrences of 
# each word, ignoring case sensitivity.



# Read the text file
with open("sample.txt", "r") as text_file:
    word_count = {}
    for line in text_file:
        line = line.strip().lower()
        words = line.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print(f"{word}: {count}")
