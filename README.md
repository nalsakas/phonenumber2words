# phonenumber to all possible words
For a given phone number, determine all possible combinations of words that can be constructed from corresponding character on keypad.

# Problem Statement
For a given phone number, determine all possible words which can be contructed from the keypad for given phone number.

# Solution
-Problem is by its nature is dfs / permutation. We need to create a product of list of chars for given number. 
-In each recursion of phone number increase current index.
-Loop through all corresponding chars of current number.
-Pass phone number and next index to down recursion.
-Termination condition is when all numbers are depleted (index == len(phonenumber) for a given phone number. 
-Combine characters and collect all possible combinations
-Return result.
