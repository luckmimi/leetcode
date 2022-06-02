class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        DIRECTIONS = [(0,1),(0,-1),(-1,0),(1,0),(0,0)]
        def flip(s, x, y):
            for dx, dy in DIRECTIONS:
                tx = dx + x
                ty = dy + y
                if not self.is_valid(tx, ty, mat): continue
                s ^= (1 << tx * n + ty)
           
            return s
        steps = 0 
        seen = [0]* (1 << ( n * m) )
        
        start = 0 
        for x in range(m):
            for y in range(n):
                start |= (mat[x][y] << ( x * n + y))
        
        q = collections.deque([])
        q.append(start)
        seen[start] = 1
        while q:
            size = len(q)
            for i in range(size):
                s = q.popleft()
                if s == 0: return steps
                
                for x in range(m):
                    for y in range(n):
                        t = flip(s, x, y)
                        if seen[t]:
                            continue
                        seen[t] = 1
                        q.append(t)
            steps += 1
        return -1
                                    
    
    def is_valid(self, i, j, mat):
        if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
            return False
        return True
