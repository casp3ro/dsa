# "Use a sliding window and a HashSet to track at most k recent elements."
nums = [1,2,3,1]
k =3
def containsDuplicateII(nums,k):

  visited = set()

  for i,val in enumerate(nums):
    
    if val in visited:
      return True
    visited.add(val)
    
    if len(visited) > k:
      visited.remove(nums[i-k])
    

  return False


print(containsDuplicateII(nums,k))