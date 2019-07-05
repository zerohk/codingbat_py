'''
Given an array of ints length 3, return an array with the elements "rotated
left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
'''

#卡了很久，还是列表的基本操作不太熟
#参考：https://zhidao.baidu.com/question/1244520812319200859.html
def rotate_left3(nums):
  if len(nums) < 3:
    return 0
  nums.append(nums[0])#是nums.append(),下面是del nums[index]
  del nums[0]
  return nums
