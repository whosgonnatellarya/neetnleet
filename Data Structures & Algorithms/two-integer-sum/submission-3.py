class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we want to return the indices, so we create a hashmap
        # with the key being the index and the value being the number
        hashm = {}
        for i in range(0, len(nums)):
            num_rn = nums[i]
            complement = target - num_rn
            if complement in hashm:
                return [hashm[complement], i]
            else:
                hashm[num_rn] = i
            

       



        