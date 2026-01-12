# sorted array
def twoSum(arr, target_sum):
    
    l = 0
    r = len(arr) - 1

    while l<r:

      res = arr[l] + arr[r]

      if res  == target_sum:
        return [l,r]

      if res < target_sum:
        l+=1
      else:
        r-=1

    return [-1,-1]

print(twoSum([2,7,11,15], 9))