class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = ((1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1))
        if x == 0 and y == 0:
            return 0
        from queue import Queue
        q = Queue(maxsize = 0)
        q.put((0,0,0))
        visited = set((0,0))
        x = abs(x)
        y = abs(y)
        while not q.empty():
            n = q.qsize()
            for _ in range(n):
                x0,y0,dist = q.get()
                
                for tx,ty in dirs:
                    cur_x = x0 + tx
                    cur_y = y0 + ty
                    if cur_x == x and cur_y == y:
                        return dist + 1
                    if cur_x >= -2 and cur_y >= -2 and (cur_x,cur_y) not in visited:

                        q.put((cur_x,cur_y,dist+1))
                        visited.add((cur_x,cur_y))
 
                
                
