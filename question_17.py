#Palindrome Checker
# Take input
user_input = input("Enter word/number: ")

print("\nOriginal:", user_input)

original = str(user_input)

reversed_value = original[::-1]

print("Reversed:", reversed_value)

if original.lower() == reversed_value.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")