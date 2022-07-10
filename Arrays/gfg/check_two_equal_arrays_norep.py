#Time Complexity is O(n)
#Space Complexity is O(1)
def check(A,B,N):
    xor_a = xor_b = 0

    for i in A:
        xor_a ^= i
    
    for j in B:
        xor_b ^= j

    return (xor_a^xor_b == 0)

#True which is not right so doesn't work for the arrays having repetition of elements(even count)
print(check([3,3],[5,5],2)) 

print(check([1,2,3,4],[1,3,2,5],4))
