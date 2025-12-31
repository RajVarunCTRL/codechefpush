# cook your dish here
for _ in range(int(input())):
    
    n = int(input())  # Len of st
    bits = list(input().strip())      # The Actual string
    swaps = 0
    curr_ones = 0
    curr_zeros = 0
    balance = 0
    onesPos = [i for i, x in enumerate(bits) if x == '1']
    zerosPos = [i for i, x in enumerate(bits) if x == '0']
    
    ones = len(onesPos)
    best = n
    """
    if 2*ones<n:
        best = 2*n  # How one mistake can cause a whole code to collapse..
    """
    
    if 2*ones<n:
        best=2*ones 
    
    for _ in range(best):
        idx1 = onesPos[curr_ones] if curr_ones < len(onesPos) else float('inf')
        idx0 = zerosPos[curr_zeros] if curr_zeros < len(zerosPos) else float('inf')
        
        if idx1<idx0:
            curr_ones+=1 
            balance+=1 
        else:
            if balance>0:
                curr_zeros+=1 
                balance-=1 
            else:
                swaps+=idx1-(curr_ones+curr_zeros)
                curr_ones+=1 
                balance+=1 
    print(best,swaps)
    
    """
        ones = bits.count('1')
        best = n
        if 2*ones<n:
            best = 2*ones
        
        curr_ones = bits[:ones].count('1')
        swaps = ones - curr_ones
        print(best,swaps)
   """ 