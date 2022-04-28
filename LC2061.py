class Type:
    EMPTY = 0 
    OBJECT = 1
class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        state = 0
        visited = set()
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        x, y = 0, 0 
        room[x][y] = -1
        cleaned = 1
        while True:
            dx, dy = dirs[state]
            if 0 <= x + dx < len(room) and 0 <= y + dy < len(room[0]) and room[x+dx][y+dy] != 1:
                x += dx
                y += dy
                if room[x][y] == 0:
                    room[x][y] = -1
                    cleaned += 1 
            else:
                state = (state + 1) % 4
           
            if (x,y,state) not in visited:
                visited.add((x,y,state))
            else:
                return cleaned
                
        
                
            
                
                
