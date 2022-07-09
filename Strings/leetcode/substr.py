#find first occurance of needle in haystack
#1. If needle is empty
#2. If needle doesn't exists in haystack
#3. important test case haystack = "mississippi" needle = "issip"
#4. Time complexity = O(n) where n is length of string haystack
def strStr(haystack, needle):
        if not needle:
            return 0
        
        h_i = 0
        n_i = 0
        h_len = len(haystack)
        n_len = len(needle)
        #give the value to first_occ which is unreachable in string
        first_occ = h_len + 1 
        
        while(h_i < h_len):

            #check if length of needle so shouldn't get out of range error
            if n_i <= n_len - 1 and haystack[h_i] == needle[n_i]:

                #if first_occ == h_len+1 means we haven't find the substring yet
                if first_occ == h_len + 1:
                    first_occ = h_i 
                    n_i += 1

                #else we are have find few characters in the string but still checking for other characters
                else:    
                    n_i += 1

            #when few characters of string is there but whole substring didn't match
            elif first_occ!= h_len + 1 and n_i != n_len:
                h_i = first_occ 
                first_occ = h_len + 1
                n_i = 0

            h_i += 1

        #we have traversed whole substring this occurs only if we have found substring(neeedle) in haystack    
        if n_i == n_len:
            return first_occ
        else:
            return -1

haystack = input()
needle = input()
print(strStr(haystack, needle))