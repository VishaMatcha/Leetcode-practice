class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = max(1, n.bit_length())
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfs(u, p, d):
            nonlocal timer
            tin[u] = timer
            timer += 1
            depth[u] = d
            up[u][0] = p
            for i in range(1, LOG):
                up[u][i] = up[up[u][i - 1]][i - 1]
            for v in g[u]:
                if v != p:
                    dfs(v, u, d + 1)
            tout[u] = timer
            timer += 1

        dfs(0, 0, 0)

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for i in range(LOG - 1, -1, -1):
                if depth[u] - (1 << i) >= depth[v]:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        fenwick = [0] * (2 * n + 1)

        def update_fenwick(i, delta):
            i += 1
            while i < len(fenwick):
                fenwick[i] ^= delta
                i += i & -i

        def query_fenwick(i):
            i += 1
            res = 0
            while i > 0:
                res ^= fenwick[i]
                i -= i & -i
            return res

        bit = [0] * n
        for i in range(n):
            mask = 1 << (ord(s[i]) - ord('a'))
            bit[i] = mask
            update_fenwick(tin[i], mask)
            update_fenwick(tout[i], mask)

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                old_mask = bit[u]
                if old_mask != new_mask:
                    delta = old_mask ^ new_mask
                    update_fenwick(tin[u], delta)
                    update_fenwick(tout[u], delta)
                    bit[u] = new_mask
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)
                mask = query_fenwick(tin[u]) ^ query_fenwick(tin[v]) ^ bit[w]
                ans.append((mask & (mask - 1)) == 0)

        return ans