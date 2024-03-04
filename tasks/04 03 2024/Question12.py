#  Write a function that takes a sentence as input and returns a new sentence 
# with the words reversed, while keeping the order of the words in the 
# sentence.


def reversewords(sentence):

    words = sentence.split()  # Split the sentence into words
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    reversed_sentence = ' '.join(reversed_words)  # Join the words back into a sentence
    return reversed_sentence

# Example usage:
input_sentence = input("Enter a sentence: ")
reversed_sentence = reversewords(input_sentence)
print("Reversed sentence:", reversed_sentence)
