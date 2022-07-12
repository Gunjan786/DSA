#Time Complexity O(n)
#Space Complexity O(1)
def minimumDeletions(nums):
    min_start = nums.index(min(nums)) 
    max_start = nums.index(max(nums)) 
    len_nums = len(nums)
        
        
    min_end = len_nums - min_start
    max_end = len_nums - max_start
        
    # remove one element from beginning and one from end
    sum_start_end = min(min_end,max_end) + min(max_start,min_start) + 1
        
    #minimum of removing both elements from beggining or both elements from end or sum_min_max
    return min(max(min_start, max_start) + 1, max(min_end, max_end), sum_start_end)

print(minimumDeletions([2,10,7,5,4,1,8,6]))