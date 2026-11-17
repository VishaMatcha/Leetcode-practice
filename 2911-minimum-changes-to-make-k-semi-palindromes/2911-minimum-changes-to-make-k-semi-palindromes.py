class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divisors = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                divisors[j].append(i)

        modify = [[float('inf')] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                res = float('inf')
                for d in divisors[length]:
                    cnt = 0
                    for offset in range(d):
                        l = i + offset
                        r = j - (d - 1 - offset)
                        while l < r:
                            if s[l] != s[r]:
                                cnt += 1
                            l += d
                            r -= d
                    res = min(res, cnt)
                modify[i][j] = res

        memo = {}
        def dfs(i, j):
            if j == 1:
                return modify[i][n - 1]
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = float('inf')
            for tail_end in range(i, n - j):
                res = min(res, modify[i][tail_end] + dfs(tail_end + 1, j - 1))
            
            memo[(i, j)] = res
            return res

        return dfs(0, k)