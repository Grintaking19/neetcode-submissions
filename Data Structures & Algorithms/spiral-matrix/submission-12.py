class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # edge cases
        if not matrix:
            return matrix
        
        res = []
        row = len(matrix)
        col = len(matrix[0])
        while matrix and len(res) < row*col:
            # right direction
            if matrix[0]:
                res.extend(matrix.pop(0))
            # print(res)
            # down direction
            if matrix and  matrix[0]:
                for i in range(len(matrix)):
                    # print(i)
                    res.append(matrix[i].pop())
            # print(matrix)
            # left direction
            if matrix:
                res.extend(matrix.pop()[::-1])
            print(res)
            # up direction
            if matrix and  matrix[0]:
                for i in range(len(matrix)-1, -1, -1):
                    res.append(matrix[i].pop(0))
        return res