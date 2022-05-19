class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         from collections import Counter
#         cnt = Counter(nums)
#         if k  > len(cnt.keys()):
#             return cnt.values()
#         else:
#             s = sorted(cnt.items(),key = lambda x: -x[1])
           
#             return [key for key,v in s][:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        val = list(cnt.values())
        res = collections.defaultdict(list)
        for key,v in cnt.items():
            res[v].append(key)
            
        self.helper(val,0, len(val)-1,k)
        
        ans = set()
        for i in  val[len(val) - k:]:
            for v in res[i]:
                ans.add(v)
        return list(ans)
    def helper(self,val, left, right,k):
        if left >= right:
            return
        partition = self.partition(val,left,right)
        if partition == len(val) - k:
            return
        else:
            if partition > len(val) - k:
                self.helper(val,left, partition - 1,k)
            else:
                self.helper(val, partition + 1, right,k)
    def partition(self, val,left, right):
        pos = val[right]
        wall = left
        for i in range(left, right):
            if val[i] < pos:
                val[i],val[wall] = val[wall],val[i]
                wall += 1
        val[right], val[wall] = val[wall],val[right]
        return wall
