# Build the table T with (2 n) entries, one for each pair
def create_table(string_length):
    # Initialize the table with "*"
    table = [["*" for _ in range(string_length+1)] for _ in range(string_length+1)]
    
    for i in range(string_length+1):
        for j in range(string_length+1):
            if i == j:
                table[i][j] = i
            elif i > j:
                table[i][j] = "∅" 
    return table

# Read the productions of the grammar
def productions_input(nonterminals_strings):
    productions = {}

    for i in range(nonterminals_strings[0]):
        line = input().split()
        non_terminal = line[0]
        production_rules = set(line[1:])
        productions[non_terminal] = production_rules

    return productions

# Read each string to process
def strings_input(nonterminals_strings):
    strings = []

    for i in range(nonterminals_strings[1]):
        string = input()
        strings.append(string)

    return strings

# Determine if the string is in the grammar with the CKY algorithm
def process_strings(productions, strings, string):
    word = strings[string]
    table = create_table(len(strings[string]))

    # Substrings of length 1
    for i in range(len(table)):
        for j in range(i+1, len(table)):
            if i == j-1:
                for key, value in productions.items():
                    if word[i] in value:
                        table[j][i] = key

    # Substrings of length n
    for n in range(2, len(word)+1):
        for i in range(len(table)):
            for j in range(i+1, len(table)):
                # Check the length of the substring
                if j-i == n:
                    # Split the substring in two parts
                    for k in range(i+1, j):
                        for key, value in productions.items():
                            for prod in value:
                                if table[k][i] == prod[0] and table[j][k] == prod[1]:
                                    table[j][i] = key
    
    return table


def CKY_algorithm(cases):
    for case in range(cases):
        # Read the number of nonterminals and the strings to process
        nonterminals_strings = list(map(int, input().split()))
        productions = productions_input(nonterminals_strings)
        strings = strings_input(nonterminals_strings)

        for i in range(len(strings)):
            table = process_strings(productions, strings, i)
            if table[-1][0] == "S":
                print("yes")
            else:
                print("no")
    # print(productions)
    

        
def main():
    cases = int(input())
    CKY_algorithm(cases)

if __name__ == "__main__":
    main()