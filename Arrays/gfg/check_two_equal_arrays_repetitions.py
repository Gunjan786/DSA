#Time Complexity O(n)
#Space Complexity O(n
#Default dictionary is sub-class of dictionary which holds default values for every key
from collections import defaultdict
def check(A,B,N):
    
    count_dict = defaultdict(int)

    for i in A:
        count_dict[i] += 1
        
    for j in B:
        if count_dict[j] == 0:
            return False
        count_dict[j] -= 1
            
    return True

print(check([2,3,1,4,5,2], [4,5,2,2,1,3], 6))
