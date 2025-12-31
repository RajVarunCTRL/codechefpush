# cook your dish here
for _ in range(int(input())): # T test Cases
    n = int(input())
    arr = list(map(int,input().split()))
    
    # dp
    
    mn = [[0] * n for _ in range(n)]
    mx = [[0] * n for _ in range(n)]
    
    # base 
    for i in range(n):
        mn[i][i] = arr[i]
        mx[i][i] = arr[i]
        
    for length in range(2,n+1):
        for i in range(n-length+1):
            j= i + length-1
            low = float('inf')  # 
            high = float('-inf')
            
            for k in range(i,j):
                low = min(low,mn[i][k] + 2*mn[k+1][j])
                high = max(high,mx[i][k] + 2*mx[k+1][j])
            mn[i][j] = low
            mx[i][j] = high
    
    print(mn[0][n-1], mx[0][n-1])
    