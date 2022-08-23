class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        a = 0 
        for i in range( len(nums) ):
            a += nums[i] 
            ans.append(a)
        return ans