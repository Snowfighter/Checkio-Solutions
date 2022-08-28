#!/usr/bin/env checkio --domain=py run multiply-intro

# (At the top right of the mission description there is always a list of available translations)
# 
# This is an intro mission, the purpose of which is to explain how to solve missions on CheckiO and how to get the most out of solving them. As you solve missions more stations become available to you, containing more complex missions.
# 
# This mission is the easiest one. Write a function that will receive 2 numbers as input and it should return the multiplication of these 2 numbers.
# 
# Input:Two arguments. Both are of type int.
# 
# Output:Int.
# 
# Example:
# 
# assert mult_two(3, 2) == 6
# assert mult_two(0, 1) == 0How does it work?
# 
# When you start working on the problem, the initial code consists of an “empty” function (which you will need to populate with your code). Asserts are included in the code to check whether the function performs as expected. Pay attention that your function returns values, and does not print them.In order to do this, use the return command instead of the print function.Check this short explanation.
# 
# The asserts in the code can be used in order to check your solution by pressing the “Run Code” button. CheckiO also uses several additional tests in order to check your solution when you click the “Check Solution” button.
# 
# Last but not least, some tasks have a list of hints for helping you solve them at the end. But since in this task we’ve already described to you how to solve it, in hints we’ll instead add some interesting facts about CheckiO.
# 
# 
# END_DESC

def mult_two(a, b):
    return a*b


if __name__ == '__main__':
    print("Example:")
    print(mult_two(3, 2))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")