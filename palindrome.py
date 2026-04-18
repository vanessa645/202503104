# Take user input
word = input("Enter a word: ")

# Convert to character array (list in Python)
original = list(word)
reversed_arr = [''] * len(original)

# Reverse the array
for i in range(len(original)):
    reversed_arr[i] = original[len(original) - 1 - i]

# Compare arrays
is_palindrome = True

for i in range(len(original)):
    if original[i] != reversed_arr[i]:
        is_palindrome = False
        break

# Output result
if is_palindrome:
    print("The word is a palindrome")
else:
    print("The word is NOT a palindrome")