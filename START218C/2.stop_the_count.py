# cook your dish here
for _ in range(int(input())):
    n = int(input())
    string = input()
    ones = 0
    ways = 0
    
    for i in range(n):
        if string[i] == '1':
            ones+=1
        k = i+1
        if 2*ones > k:
            ways+=1
    print(ways)
    