'''
Given an array of ints, return True if one of the first 4 elements in the array
is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
'''

def array_front9(nums):
    size = len(nums)
    if size <= 4:
        if 9 in nums:
            return True
        else:
            return False
    else:
        if 9 in nums[:4]:
            return True
        else:
            return False

        '''
Solution:

def array_front9(nums):
  # First figure the end for the loop
  end = len(nums)
  if end > 4:
    end = 4

  for i in range(end):  # loop over index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False
        '''
