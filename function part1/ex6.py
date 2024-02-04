def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

# Read the sentence from the user
user_input = input("Enter a sentence: ")

# Reverse the sentence
reversed_sentence = reverse_sentence(user_input)

# Display the reversed sentence
print("Reversed sentence:", reversed_sentence)