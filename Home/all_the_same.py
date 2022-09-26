#!/usr/bin/env checkio --domain=py run all-the-same

# In this mission you should check if all elements in the given list are equal.
# 
# Input:List.
# 
# Output:Bool.
# 
# The idea for this mission was found onPython Tricks series by Dan Bader
# 
# Precondition:all elements of the input list are hashable
# 
# 
# END_DESC

from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    # your code here
    return all(map(lambda i: i == elements[0], elements))


print("Example:")
print(all_the_same([1, 1, 1]))

assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([2, 1, 1, 1]) == False
assert all_the_same([]) == True
assert all_the_same([1]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")