class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        
        sum = 0
        for x in nums:
            for y in nums:
                sum = nums[x] + nums[y]
                if sum == target:
                    break
        return sum

    init = twoSum([1,2,3], 3)   

        