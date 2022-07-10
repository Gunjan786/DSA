#Time Complexity O(n)
def getMinMax( a, n):
    min_ele = max_ele = a[0]
    i = 1
    
    while i < n:
        if a[i] < min_ele:
            min_ele = a[i]
        if a[i] > max_ele:
            max_ele = a[i]
        i += 1
    
    return [min_ele, max_ele]

print(getMinMax([1,2,-3,0,8,9,-10],7))