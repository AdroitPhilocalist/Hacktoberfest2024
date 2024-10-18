def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Ask the user for a word or phrase
word = input("Enter a word or phrase: ")

if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
