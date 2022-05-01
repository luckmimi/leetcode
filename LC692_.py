class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        m = collections.Counter(words)
        
                
       
        res = sorted(m.items(), key = lambda x: (-x[1],x[0]) )
        
        return [v[0] for v in res[:k]]
