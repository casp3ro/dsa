
nums = [8,1,2,2,3]

def smallerNumbersThenCurrent(nums):
  sorted_nums = sorted(nums)
  smaller = {}

  for i,v in enumerate(sorted_nums):
    #this is a trick
    if v not in smaller:
      smaller[v] = i

  output = []

  for n in nums:
    output.append(smaller[n])
  
  return output


print(smallerNumbersThenCurrent(nums))