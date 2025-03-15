keypad = {
    '0': [],
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

def generatewords(phonenumber):
    def dfs(phonenumber, index):
        # Termination condition
        if index == len(phonenumber):
            return [[]]
        
        collect = []
        # For each number, determine corresponding chars in keypad
        chars = keypad[phonenumber[index]]
        # Loop through all characters corresponding to current number
        for char in chars:
            # apply recursion to remaing numbers in phonenumber
            res = dfs(phonenumber, index + 1)
            # collect results
            collect += list(map(lambda x: [char, *x], res))
        
        return collect
    
    return list(map(lambda x: "".join(x),dfs(phonenumber, 0)))

if __name__ == "__main__":
    n1 = "2"
    n2 = "23"
    n3 = "36622277"

    print(generatewords(n1))
    print(generatewords(n2))
    
    # very long list, "domabcrs" was used in inverse of this problem
    # Lets double check the result
    if "domabcrs" in generatewords(n3):
        print('"domabcrs" is contained in result list of n3')