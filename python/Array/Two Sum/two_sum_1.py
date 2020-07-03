class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, number in enumerate(nums):

            make_positive = target - number

            if (make_positive in nums) and (nums.index(make_positive) != index):
                return [nums.index(make_positive), index]

# less code and more time complexity， and use nums.index need O(n) every times.