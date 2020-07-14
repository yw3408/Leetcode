# # method 1
# class Solution:
#     def singleNumber(self, nums):
#         a = 0
#         for i in nums:
#             a ^= i  # XOR operator
#         return a
# # con: best one

# # method 2
# class Solution:
#     def singleNumber(self, nums):
#
#         no = []
#         for i in nums:
#             if i not in no:
#                 no.append(i)
#             else:
#                 no.remove(i)
#
#         return no.pop()
# # con: not work for 'no result', because list.pop() return false for empty list

nums = [3,1,2,3,4,2,1]
a = Solution()
print(a.singleNumber(nums))