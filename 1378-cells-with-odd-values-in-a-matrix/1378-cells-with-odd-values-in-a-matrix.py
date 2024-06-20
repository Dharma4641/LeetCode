class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0] * n for _ in range(m)]
        for ri, ci in indices:
            for j in range(n):
                mat[ri][j] += 1
            for i in range(m):
                mat[i][ci] += 1
        odd_count = sum(1 for row in mat for cell in row if cell % 2 != 0)
        return odd_count


        