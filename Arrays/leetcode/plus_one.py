#Time Complexity O(n)
#Space Complexity O(1)
# arr = [9,9,9] add 1 to arr and result = [1,0,0,0]
# arr = [8,9,9] add 1 to arr and result = [9,0,0]
def plusOne(digits):
        
    i = len(digits)-1
        
    while i >= 0:
        if digits[i] != 9:
            break
        digits[i] = 0
        i-=1
        
    if i == -1:
        digits[0] = 1
        digits.append(0)
    else:
        digits[i] += 1
                 
    return digits

print(plusOne([1,9,9,8,9]))