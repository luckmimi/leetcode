class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        print(nums1)
        pos = sorted([(val,i) for i, val in enumerate(nums2)],key = lambda x:x[0])
        start = 0
        res = [0]*len(nums1)
        right = len(nums1)-1
        
        while pos:
            val,r = pos.pop() 
            
            if nums1[right] > val:
                res[r] = nums1[right]
                right -= 1
            else:
                res[r] = nums1[start]
                start += 1
          
        return res
        
