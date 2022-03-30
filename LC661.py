class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                d = [(1,0),(-1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,-1),(-1,1)]
                sm = img[i][j]
                cnt = 1
                for tx,ty in d:
                    x = tx + i
                    y = ty + j
                    if 0<= x < m and 0 <= y < n:
                        cnt += 1
                        sm += img[x][y]
                res[i][j] = sm // cnt
        return res
