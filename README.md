# wordtokeypadnumber
For a given phone number, determine all possible combinations of words.

# Problem Statement
For a given phone number, determine all possible words which can be contructed from the keypad for given phone number.

# Solution
Problem is by its nature is dfs. In each recursion of phone numbers:
Loop through all corresponding chars of current number.
Pass remaining phone number to down recursion.
Termination condition is when all numbers are depleted for a given phone number. 
Collect all possible combinations of words
Return result.