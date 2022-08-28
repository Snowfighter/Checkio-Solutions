#!/usr/bin/env checkio --domain=py run the-most-frequent

# You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence. It can be only one.
# 
# Input:non empty list of strings.
# 
# Output:a string.
# 
# 
# END_DESC



def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
   

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