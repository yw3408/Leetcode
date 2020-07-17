# # method 1;brute force
# class Solution:
#     def maxSubArray(self, nums):
#         presum = []
#         if len(nums) == 1:
#             return nums[0]
#         for i in range(len(nums)):
#             if i == 0:
#                 presum.append(nums[0])
#             else:
#                 presum.append(presum[i - 1] + nums[i])
#
#         # sub = nums[0]
#         sub = []
#
#         for i in range(len(nums) - 1):
#             for j in range(i+1, len(nums)):
#                 # sub = max(sub, presum[j] - presum[i])
#                 sub.append(presum[j] - presum[i])
#         return sub, presum,i,j

# method 2:
class Solution:
    def maxSubArray(self, nums):
        l = g = float("-inf") # set the l and g
        for i in nums:
            l = max(l+i,i)
            g = max(g,l)
        return g

nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-2,-1]
a = Solution()
print(a.maxSubArray(nums))
