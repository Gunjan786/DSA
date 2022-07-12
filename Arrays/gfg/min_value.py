#time Complexity O(nlogn)
#Space Complexity O(1)
#1*6+1*5+3*4 = 6+5+12 = 23 is the minimum sum
def minValue(a, b, n):
    a.sort()
    b.sort(reverse = True)
    product = a[0] * b[0]
        
    for i in range(1, n):
        product += a[i] * b[i]
            
    return product

print(minValue([3,1,1],[6,5,4],3))
