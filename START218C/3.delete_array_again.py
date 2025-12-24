# cook your dish here
for _ in range(int(input())): # T inputs
    n = int(input())
    lst1 = list(map(int,input().split()))
    lst2 = list(map(int,input().split()))
    
    res = 0
    curr_min = lst2[0]
    
    for i in range(n):
        if lst2[i] < curr_min:
            curr_min=lst2[i]
        
        res+=lst1[i] * curr_min
    print(res)