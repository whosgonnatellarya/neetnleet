class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        for i in range (0, len(nums)):
            for j in range (i+1, len(nums)):
                if nums [i] == nums [j]:
                    count+=1
            if count>0:
                return True
        return False
    
        