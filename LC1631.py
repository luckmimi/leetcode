class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        return self.bfs(heights,0,0)
        
    def bfs(self,heights,i,j):
        distance = {(i,j):0}
        # q = collections.deque([(i,j)])
        q = []
        heapq.heappush(q,(0,i,j))
        dirs = [(0, 1),(0, -1),(-1, 0),(1,0)]
        
        while q:
            
            dst, x, y = heapq.heappop(q)
            if x == len(heights) -1 and y == len(heights[0]) -1:
                     return dst
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if not self.is_valid(heights, new_x, new_y):
                    continue
                tmp = max(dst,abs(heights[x][y]- heights[new_x][new_y]))
                if (new_x,new_y) not in distance or distance[(new_x,new_y)] > tmp:
                        distance[(new_x,new_y)]  = tmp
                        heapq.heappush(q,(tmp,new_x,new_y))
        
        return -1
    
    def is_valid(self,heights,x,y):
        if x < 0 or y < 0 or x >= len(heights) or y >= len(heights[0]):
            return False
        return True
