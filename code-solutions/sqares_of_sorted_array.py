import math
nums = [-4,-1,0,3,10]

def squaresOfSortedArray(nums):
  output = [0] * len(nums)

  l,r = 0, len(nums) -1
  index = len(nums) -1

  while l<=r:
    left =  pow(nums[l],2)
    right = pow(nums[r],2)

    if left > right:
      output[index] = left
      l+=1
    else:
      output[index] = right
      r-=1
    index -=1


  return output

print(squaresOfSortedArray(nums))