class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        '''定义动态数组 dp[i][2]，其中：

dp[i][0] 表示以 nums[i] 结尾的成绩为正的连续子数组最大长度；
dp[i][1] 表示以 nums[i] 结尾的乘积为负的连续子数组的最大长度；
 '''
        
        dp = [[0]*2 for _ in range(len(nums))]
        dp[0][0] = 1 if nums[0] > 0 else 0
        dp[0][1] = 1 if nums[0] < 0 else 0
        
        res = dp[0][0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp[i][0] = dp[i-1][0] + 1 
                dp[i][1] = dp[i-1][1] + 1 if dp[i-1][1] > 0 else 0
            elif nums[i] < 0:
                
                dp[i][1] = dp[i-1][0] + 1 
                dp[i][0] = dp[i-1][1] + 1 if dp[i-1][1] > 0 else 0
                
            
            res = max(dp[i][0],res)
        return res
    
"""
class Solution {
    fun getMaxLen(nums: IntArray): Int {
        if (nums.isEmpty())
            return 0
        var dp = Array(nums.size) { IntArray(2) }
        //dp[i][0]: 表示以当前数结尾的乘积为正的最长子数组长度
        //dp[i][1]: 表示以当前数结尾的 < 0 的最长子数组长度
        dp[0][0] = if (nums[0] > 0) 1 else 0
        dp[0][1] = if (nums[0] < 0) 1 else 0
        var max = dp[0][0]
        for (i in 1 until nums.size) {
            if (nums[i] > 0) {
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = if (dp[i - 1][1] > 0) (dp[i - 1][1] + 1) else 0
            } else if (nums[i] < 0) {
                dp[i][0] = if (dp[i - 1][1] > 0) (dp[i - 1][1] + 1) else 0
                dp[i][1] = dp[i - 1][0] + 1
            }
            max = kotlin.math.max(max, dp[i][0])
        }
        return max
    }
}

"""
    
    
    
