# method 1
# class Solution:
#     def removeElement(self, nums , val):
#         t = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[t] = nums[i]  # actually change part of the nums
#                 t = t + 1
#         # didn't remove the element and just know the num
#         return t
# con: time complexity O(n), space complexity

# method 2
class Solution:
    def removeElement(self, nums, val):
        while True:
            try:
                nums.remove(val)
            except:
                break

        return len(nums)
# con: actually remove the element with O(n)


nums = [2,3,1,3,4,2,2,2]
val = 2
a = Solution()
print(a.removeElement(nums,val))