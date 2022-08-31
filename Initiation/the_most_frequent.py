#!/usr/bin/env checkio --domain=py run the-most-frequent

# You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence. It can be only one.
# 
# Input:non empty list of strings.
# 
# Output:a string.
# 
# 
# END_DESC


from collections import Counter

def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    c = Counter(data)
    return c.most_common(1)[0][0]

def most_frequent_map(data: list) -> str:
    d = []
    for i in data:
        num = sum(list(map(lambda x: int(x==i), data)))
        d.append((i, num))
        
    return sorted(d, key=lambda x: x[1])[1][0]
  

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]))
    
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')