nums = [4,3,2,7,8,2,3,1]
def findAllDisapiaredNums(nums):

  # 1-n
  
  numsSet = set(nums)
  output = []

  for num in range(1,len(nums)+1):
    if not num in numsSet:
      output.append(num)

  return output


print(findAllDisapiaredNums(nums))
