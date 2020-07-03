class Solution:
    def twoSum(self, nums, target):

        h = {} # creat a dict
        for i, j in enumerate(nums):   # i is the index, j is the int
            n = target - j  # n is the complement of j for target
            if n not in h:  # 1. not found  2. not exist
                h[j] = i   # add dict to h
            else:
                return [h[n] , i]   # find the result


nums = [2,7,11,15]
target = 9
a = Solution() # at first initializing class , otherwise we will get wrong
print(a.twoSum(nums, target))
