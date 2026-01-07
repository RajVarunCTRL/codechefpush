# cook your dish here
# GTG URGENT STUFF NEED TO GO!
import sys

input = sys.stdin.readline

for _ in range(int(input())): # T test cases
    n = int(input())

    lst = list(map(int, input().split()))   # Row 1
    lst1 = list(map(int, input().split()))  # Row 2 (was lst2 in your code)
    
    prefix_min = [float('inf')] * n 
    prefix_min[0] = min(lst[0], lst1[0])
    
    for i in range(1, n):
        prev_val = prefix_min[i-1]
    
        if prev_val == float('inf'): 
            break 
            
        candidates = []
        if lst[i] >= prev_val: candidates.append(lst[i])
        if lst1[i] >= prev_val: candidates.append(lst1[i])
        
        if candidates:
            prefix_min[i] = min(candidates)
        else:
            prefix_min[i] = float('inf')

    suffix_max = [float('-inf')] * n
    
    suffix_max[n-1] = max(lst[n-1], lst1[n-1])
            
    for i in range(n-2, -1, -1):
        next_val = suffix_max[i+1]
        
        if next_val == float('-inf'):
            break
            
        candidates = []
        if lst[i] <= next_val: candidates.append(lst[i])
        if lst1[i] <= next_val: candidates.append(lst1[i])

        if candidates:
            suffix_max[i] = max(candidates)
        else:
            suffix_max[i] = float('-inf')
            
    possible = False
    for k in range(n):
        configurations = [(lst[k], lst1[k]), (lst1[k], lst[k])]
        
        for top, bot in configurations:
            if top > bot:
                continue
    
            valid_left = True
            if k > 0:
                if prefix_min[k-1] == float('inf') or prefix_min[k-1] > top:
                    valid_left = False
        
            valid_right = True
            if k < n - 1:
                if suffix_max[k+1] == float('-inf') or bot > suffix_max[k+1]:
                    valid_right = False
            
            if valid_left and valid_right:
                possible = True
                break
        
        if possible:
            break
    
    if possible:
        print("Yes")
    else:
        print("No")
        # 