# # method 1
# class Solution:
#     def searchInsert(self, nums, target):
#         if target in nums:
#             for i in range(len(nums)):
#                 if target == nums[i]:
#                     return i
#         else:
#             if target < min(nums):
#                 return 0
#             elif target > max(nums):
#                 return len(nums)
#             else:
#                 for i in range(len(nums)):
#                     if nums[i] < target and nums[i+1] > target:
#                         return i+1
# # con: time complex O(n), for some case only O(1)

# method 2
class Solution:
    def searchInsert(self, nums, target):
        for c in range(len(nums)):
            if nums[c] >= target:
                return c
        return len(nums)
# con: easy coding, however, worse result because it always have O(n) time complexity

nums = [1,3,5,7]
target = 9
a = Solution()
print(a.searchInsert(nums,target))