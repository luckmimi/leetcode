class Solution:
#     def beautifulArray(self, n: int) -> List[int]:
#         res = [1]
#         while len(res) < n:
#             res = [i * 2 - 1 for i in res]  + [i * 2 for i in res]
        
#         return [i for i in res if i <=n]
    
#     def beautifulArray(self, n: int) -> List[int]:
#         if n == 1: return [1]
#         odd = [i*2 - 1 for i in self.beautifulArray(n/2 + n %2)]
#         even = [i* 2 for i in self.beautifulArray(n/2)]
#         return odd+ even
    
     def beautifulArray(self, n: int) -> List[int]:
            return sorted(range(1,n+1),key = lambda x: bin(x)[:1:-1])
