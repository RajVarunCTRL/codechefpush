# cook your dish here
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    curr_sum = sum(lst)
    
    if curr_sum >= 0:
        print(0)
    else:
        d_temp = abs(curr_sum)
        x=(d_temp+n-1)//n 
        print(x)