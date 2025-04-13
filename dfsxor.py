from typing import List
from functools import lru_cache


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(i: int, j: int, xor: int) -> int:
            # Check bounds first
            if i >= m or j >= n:
                return 0

            # Now safe to access grid
            xor ^= grid[i][j]

            # Base case: reached bottom-right cell
            if i == m - 1 and j == n - 1:
                return 1 if xor == k else 0

            # Combine both movements in one line using modulo
            return (dfs(i + 1, j, xor) + dfs(i, j + 1, xor)) % MOD

        try:
            return dfs(0, 0, 0)
        finally:
            dfs.cache_clear()
# Example usage:
solution = Solution()
grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]]
k = 11
print(solution.countPathsWithXorValue(grid, k))  # Output: 3
