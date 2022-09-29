#!/usr/bin/env checkio --domain=py run duplicate-zeros

# "Sometimes, zeros resemble very tasty donuts. And every time we finish a donut, we want another,    and then another, and then another..."
# 
# You are given a list of integers. Your task in this mission is to double all the zeros in the given list (think about donuts ;-P).
# 
# Input:List.Output:List.
# 
# If you have solved this mission, you can enjoy a donut with peace of mind!=)
# 
# 
# 
# 
# END_DESC

def duplicate_zeros(donuts: list) -> list:
    # your code here
    return []


print("Example:")
print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))

assert duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]) == [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
assert duplicate_zeros([0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert duplicate_zeros([100, 10, 0, 101, 1000]) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")