
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
class Solution:
    def removeDuplicates(self, nums):

        len_ = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[len_] = nums[i]
                len_ += 1
        print(nums)
        return len_


nums = [1,1,2]
a = Solution()
print(a.removeDuplicates(nums))