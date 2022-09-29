#!/usr/bin/env checkio --domain=py run convert-and-aggregate

# You are given a list of tuples. Each tuple consists of two values: a string    and an integer.    You need to create and return a dictionary,    where keys are string values from input tuples and values are aggregated (summed) integer    values from input tuples for each specific key. The resulted dictionary    should not include items with empty key or zero value.
# 
# Input:List of tuples.
# 
# Output:Dictionary.
# 
# Examples:
# 
# assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
# assert conv_aggr([]) == {}
# assert conv_aggr([("a", 5), ("a", -5)]) == {}
# assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
# END_DESC

def conv_aggr(data: list[tuple[str, int]]) -> dict[str, int]:
    # your code here
    return {}


print("Example:")
print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))

assert conv_aggr([("a", 7), ("b", 8), ("a", 10)]) == {"a": 17, "b": 8}
assert conv_aggr([]) == {}
assert conv_aggr([("a", 5), ("a", -5)]) == {}
assert conv_aggr([("a", 5), ("a", 5), ("a", 0)]) == {"a": 10}
assert conv_aggr([("a", 5), ("", 15)]) == {"a": 5}

print("The mission is done! Click 'Check Solution' to earn rewards!")