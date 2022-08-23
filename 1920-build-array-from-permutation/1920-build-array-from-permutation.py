class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range( len(nums) ) :
            b = nums[nums[i]]
            ans.append(b)
        return ans
            