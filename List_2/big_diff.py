'''
Given an array length 1 or more of ints, return the difference between the
largest and smallest values in the array. Note: the built-in min(v1, v2) and
max(v1, v2) functions return the smaller or larger of two values.
'''
def big_diff(nums):
  if len(nums) < 1:
    return False
  if len(nums) == 1:
    return 0
  minv = maxv = nums[0]
  for i in range(len(nums) - 1):
    minv = min(minv,nums[i + 1])
    maxv = max(maxv,nums[i + 1])
  big_diff = maxv - minv
  return big_diff
