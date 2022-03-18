class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
    
        tmp = [v[0] for v in sorted(cnt.items(),key = lambda x:(-x[1],x[0]))]
        if len(tmp) <=k:
            return tmp
        return tmp[:k]
      
