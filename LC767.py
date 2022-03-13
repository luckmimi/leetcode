class Solution:
    def reorganizeString(self, s: str) -> str:
        c = collections.Counter(s)
        maxHeap = [[-v,k] for k, v in c.items()]
        prev = None
        heapq.heapify(maxHeap)
        res = ''
        while maxHeap or prev:
            if prev and not maxHeap:
                return ''
            cnt,char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None
            if cnt != 0 :
                prev =[cnt,char]
        return res
