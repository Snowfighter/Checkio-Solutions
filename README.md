# Checkio-Solutions
My perosnal notes and solutions for Checkio tasks

## Initiation
### First Word Simplified
Apparently the quickest way to find the first word in this exercise is not to use `.split()` method but to find the index of the space symbol `str.find(" ")`.
### Number Length
Why on Earth have I decided to make a list ofintegers out of a number, when I can just calculate the length of `str(number)` ?
### The Most Frequent
Should look at the `statistics` module
### End Zeros
Found a `.group()` method inregex that returns an entire match
### Remove All Before
Could use lambda function for speed but I like exceptions, more straightforward
### Replace First
Another way is to use `deque` object from `collections` class and `rotate` method.
### Split Pairs
The gist of this task is to construct pairs from the string. I have done the following way:
```python
pairs = list(map(''.join, zip(*[iter(initial_string+'_')]*2)))
```
Seems cumbersome, but basically it combines two iterator objects of the same list and combines into pairs -> ['iter1 -> 1st el  iter2 -> 2nd el', 'iter1 -> 3rd el iter2 -> 4th el]

Another way is to use regex again:
```python
pairs = re.findall('..', initial_string+'_')
```
### Correct Sentences
Could have used a oneliner by separating the sentece in three parts: first letter + rest of the sentence + if condition on fullstop.
### Is Even
I tried to used fancy bitwise operations, because `even_number AND 1 == 0`. Ex: 4_(10) = 000100_(2) => 000100_(2) & 000001_(2) == 0. Fo some reason I wrote oneliner `return not bool(n & 1)`, but could have used just `n & 1 == 0`.   
### Nearest Value
Was stupid to me not to apply `min` function on the set, but rather on the list.

