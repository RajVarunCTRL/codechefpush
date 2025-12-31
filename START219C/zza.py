# cook your dish here
for _ in range(int(input())):
    x,y = map(int,input().split())
    
    smollArea = 10*10
    largeArea = 15*15
    
    smol = smollArea * y
    large = largeArea * x
    
    if smol > large:
        print("Small")
    elif large>smol:
        print("Large")
    else:
        print("Equal")