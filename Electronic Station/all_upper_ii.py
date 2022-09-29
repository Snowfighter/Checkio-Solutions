#!/usr/bin/env checkio --domain=py run all-upper-ii

# Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False.
# 
# Input:A string.
# 
# Output:a boolean.
# 
# Precondition:a-z, A-Z, 1-9 and spaces
# 
# 
# END_DESC

def is_all_upper(text: str) -> bool:
    # your code here
    return False


if __name__ == "__main__":
    print("Example:")
    print(is_all_upper("ALL UPPER"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")