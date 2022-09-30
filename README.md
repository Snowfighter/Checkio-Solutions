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
## Home
### Three Words
I have approached this task in two ways: regex and mapping. Regex helped to filter out three words. In my opinion, my regex approach is a bit cumbersome and can be done easier using `\D+\s` metacharacters. Mapping can be used to transform strings into 1 and 0 pattern, where 1 is a word string and 0 is not.
### Sum Numbers
Keep forgetting that int itself is a function and I do not need to specify any varibale for it in the `lambda` functions.
### Right To Left
Someone once wrote that if you get into regex, you'll always try to use it. This happened to me today. `String` has a `replace` method, how could I forget it ? Instead I have use the regex again.
### First Word
For som reason I have not read the task correctly and made a humongous regex for extracting words even if we have numbers in the string. Apparently, no numbers were in the test cases. Another thing that I've learned is this elegant approach: `[x, ' '][x in '.,']`, where the first pair of square brackets is a list and the second will result either in `[True]` or `[False]`, and boolean being a subclass of int will transform into the following `[1]` or `[0]`.
### Changing Direction
Could find an elegany solution. My concept was in finding the diferences between the neighboring numbers and stripping zeroes from bothe sides as that means equal trailing numbers.

Update: I really liked the use of `pairwise` function from **itertools**, which returns successive overlapping pairs. Also the use of '+' and '-' to indicate the growth and the recession of the sequence is a nice move.
### All The Same
Should have remebered that `set` removes duplicates and works with the empty lists. Also checking equlity of the original list and the reversed one is a really nice solution. The question that bugs my mind is why `map` works when we address to the empty list by index:
```
l = []
iter = map(lambda i: i == l[0], l)
```
Update: [Answer on StackOverflow](https://stackoverflow.com/questions/73865531/how-does-map-function-handle-errors?noredirect=1#comment130428109_73865531)


