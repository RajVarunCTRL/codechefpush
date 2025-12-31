# cook your dish here
for _ in range(int(input())):
    n = int(input())  # Len of st
    bits = input()      # The Actual string
    
    ones = 0
    zeros = 0
    goodPre = 0
    
    for ch in bits:
        if ch == '1':
            ones+=1
        else:
            zeros+=1
        
        if ones>=zeros:
            goodPre+=1
    print(goodPre)
    
    
    """
        LOL OUTPUT = 2 ints? requires max and min when returned, it requires 1 :D
    """
    