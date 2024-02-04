def is_palindrome(word):
    return word == word[::-1]

# Prompt the user to enter a word or phrase
word = input("Enter a word or phrase: ").replace(" ", "")

# Check if the input word or phrase is a palindrome
print(f"The word or phrase '{word}' is {'a palindrome' if is_palindrome(word) else 'not a palindrome'}.")
