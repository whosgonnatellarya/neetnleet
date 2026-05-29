class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashmap again
        dict1 = {}
        for i in range (0, len(nums)):
            dict1[nums[i]] = dict1.get(nums[i], 0) + 1

        for i in dict1:
            if dict1[i] > 1:
                return True
        return False
    
        