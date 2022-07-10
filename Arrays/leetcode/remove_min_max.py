#Time Complexity O(n)
#Space Complexity O(1)
def minimumDeletions(nums):
    min_start = nums.index(min(nums)) 
    max_start = nums.index(max(nums)) 
    len_nums = len(nums)
        
        
    min_end = len_nums - min_start
    max_end = len_nums - max_start
    sum_min_max = min(min_end,min_start+1)+min(max_end,max_start+1)
        
    if min_start <= min_end and max_start <= max_end:
        return max(min_start+1, max_start+1)
    elif min_start >= min_end and max_start >= max_end:
        return max(min_end, max_end)
    elif sum_min_max <= max(min_end,min_start) and sum_min_max <= max(max_end,max_start):
        return sum_min_max
    else:
        return min(max(min_start,max_start)+1, max(max_end, min_end))

print(minimumDeletions([2,10,7,5,4,1,8,6]))