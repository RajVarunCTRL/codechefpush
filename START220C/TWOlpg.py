# cook your dish here
for _ in range(int(input())): # T test cases
    
    lst = list(map(int,input().split()))
    
    # lst[0] = x, lst[1] = y 
    # x  "biscuits" and y "cakes"
    if lst[0] % 2 == 0:
        print("Bob")
    else:
        print("Alice")
    
    