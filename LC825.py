class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = 0 
        N = len(ages)
        ages.sort()
        for i in range(N):
            a = ages[i]
            #lower = bisect.bisect(ages,0.5*a + 7)
            lower = self.search(ages,0.5*a + 7)
           # upper = bisect.bisect(ages,a)
            upper = self.search(ages,a)
            # print(lower, upper)
            cnt += max(0, upper - lower - 1)
        return cnt
    
    def search(self,ages,target):
        left = 0
        right = len(ages)
        while left < right:
            mid = left + (right - left)//2
            if ages[mid] <= target:
                left = mid + 1 
            else:
                right = mid 
                
        return left
        
        
            
        
