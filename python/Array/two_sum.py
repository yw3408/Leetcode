#method 1
# class Solution:
#     def twoSum(self, nums, target):
#
#         h = {} # creat a dict
#         for i, j in enumerate(nums):   # i is the index, j is the int
#             n = target - j  # n is the complement of j for target
#             if n not in h:  # 1. not found  2. not exist
#                 h[j] = i   # add dict to h
#             else:
#                 return [h[n] , i]   # find the result

# # method 2
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for index, number in enumerate(nums):
#
#             make_positive = target - number
#
#             if (make_positive in nums) and (nums.index(make_positive) != index):
#                 return [nums.index(make_positive), index]
#
# # less code and more time complexity， and use nums.index need O(n) every times.

# METHOD 3
class Solution:
    def twoSum(self, nums, target):
        for index, number in enumerate(nums):

            make_positive = target - number

            if (make_positive in nums) and (nums.index(make_positive) != index):
                return [nums.index(make_positive), index]


nums = [2,7,11,15]
target = 9
a = Solution() # at first initializing class , otherwise we will get wrong
print(a.twoSum(nums, target))
