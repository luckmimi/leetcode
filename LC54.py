class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        upper = 0
        lower = len(matrix) - 1
        right = len(matrix[0]) - 1
        left = 0
         
        while len(res) < len(matrix)* len(matrix[0]):
            # 从左到右
            if upper <= lower:
                for i in range(left, right+1):
                    res.append(matrix[upper][i])
                upper += 1
            # 从上倒下
            if left <= right:
                for j in range(upper, lower+1):
                    res.append(matrix[j][right])
                right -= 1

            # 从右边向左
            if upper <= lower:
                for i in range(right, left -1, -1 ):
                    res.append(matrix[lower][i])
                lower -= 1            
            
            # 从下向上
            if left <= right:
                for j in range(lower,upper -1, -1):
                    res.append(matrix[j][left])
                left += 1
        return res
