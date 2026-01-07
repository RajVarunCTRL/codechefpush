# cook your dish here
from collections import Counter
for _ in range(int(input())): #T inputs
    n = int(input())
    st = input()
    found = False
    
    filtered = [char.lower() for char in st if char.isalpha()]
    letterCount = Counter(filtered)
    
    
    for v in letterCount.values():
        if v>=2:
            found = True
            break
        
    print("Yes" if found else "No")
    
    