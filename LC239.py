class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        res = []
        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
            if i - k + 1 == q[0]:
                q.popleft()
            
        return res
            
