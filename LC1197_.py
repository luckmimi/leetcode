class Solution:
    def minKnightMoves(self, xx: int, yy: int) -> int:
        dirs = ((1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1))
        from collections import deque
        q = deque([(0,0)])
        distance = {(0,0):0}
        visited = {(0,0)}
        while q:
            if (xx,yy) in distance:
                    return distance[(xx,yy)]
            (x,y) = q.popleft()
            for tx,ty in dirs:
                new_x = x + tx
                new_y = y + ty
                if (new_x, new_y) in distance:
                    continue
                q.append((new_x,new_y))
                distance[(new_x,new_y)] = distance[(x,y)] + 1

            
        
#         if x == 0 and y == 0:
#             return 0
#         from queue import Queue
#         q = Queue(maxsize = 0)
#         q.put((0,0,0))
#         visited = set((0,0))
#         x = abs(x)
#         y = abs(y)
#         while not q.empty():
#             n = q.qsize()
#             for _ in range(n):
#                 x0,y0,dist = q.get()
                
#                 for tx,ty in dirs:
#                     cur_x = x0 + tx
#                     cur_y = y0 + ty
#                     if cur_x == x and cur_y == y:
#                         return dist + 1
#                     if cur_x >= -2 and cur_y >= -2 and (cur_x,cur_y) not in visited:

#                         q.put((cur_x,cur_y,dist+1))
#                         visited.add((cur_x,cur_y))
 
                
                
