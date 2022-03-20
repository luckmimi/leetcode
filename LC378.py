class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # the size of the matrix
        n = len(matrix)
        minHeap = []
        for i in range(min(k,n)):
            minHeap.append((matrix[i][0],i,0))
        print(minHeap)
        #heapipy ourlist 
        heapq.heapify(minHeap)
        #until we find k elements
        while k:
            element, r, c = heapq.heappop(minHeap)
            # if we have any new elment in the current row, add the
            if c < n - 1:
                heapq.heappush(minHeap,(matrix[r][c+1],r,c+1))
            k -= 1
        return element
