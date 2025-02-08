def length_of_the_longest_substring(s:str)->int:
    unique = set()
    longest = 0
    l = 0
    
    for r in range(len(s)):
        while s[r] in unique:
            unique.remove(s[l])
            l+=1
        
        unique.add(s[r])
        longest = max(longest, r-l+1)
    
    return longest
        