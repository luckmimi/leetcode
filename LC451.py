class Solution:
    def frequencySort(self, s: str) -> str:
        c = collections.Counter(s)
        print(c)
#         freq =collections.defaultdict()
        
#         for k, v in c.items():
#             freq[v] = freq.get(v,[])+[k]
        ans =''
#         print(freq)
        s = sorted(c.items(),key = lambda x:-x[1] )
        print(s)
        for k, v in s:
            print(k,v)
            ans += k * int(v)
        return ans
