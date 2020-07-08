
# method 1
# class Solution:
#     def removeDuplicates(self, nums):
#         rep = []
#         h = 0
#         if len(nums) == 0:
#             return 0
#         for i in range(len(nums)):
#             if nums[i] not in rep:
#                 rep.append(nums[i])
#                 nums[h] = nums[i]
#                 h = h + 1
#         return len(rep)
# con: too slow

# method 2
# class Solution:
#     def removeDuplicates(self, nums):
#
#         len_ = 1
#         if len(nums) == 0:
#             return 0
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[len_] = nums[i]
#                 len_ += 1
#         print(nums)
#         return len_

# method 3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter=len(nums)-1  # start with the last element
        while counter>0: # means the list is not empty
            if nums[counter]==nums[counter-1]:
                nums.pop(counter-1)    # remove the redundant element
            counter=counter-1
        return len(nums)
# con: faster, O(n) time complexity, O(1) space complexity

nums = [1,1,2]
a = Solution()
print(a.removeDuplicates(nums))