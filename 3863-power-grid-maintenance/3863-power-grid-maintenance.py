class DSU:
    def __init__(self, n):
        # Step 1: Initialize DSU
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Step 2: Merge connected components
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px


class Solution:
    def processQueries(self, c, connections, queries):
        # Step 1: Initialize DSU for all nodes
        dsu = DSU(c)

        # Step 2: Apply union for all given connections
        for a, b in connections:
            dsu.union(a, b)

        # Step 3: Build map of root → sorted list of nodes
        from collections import defaultdict
        import bisect
        groups = defaultdict(list)
        for i in range(1, c + 1):
            root = dsu.find(i)
            groups[root].append(i)
        for g in groups.values():
            g.sort()

        # Step 4: Initialize offline tracker and result container
        isOffline = [False] * (c + 1)
        res = []

        # Step 5: Process queries
        for typ, node in queries:
            if typ == 1:
                # Step 6: Handle query for smallest online node
                if not isOffline[node]:
                    res.append(node)
                else:
                    root = dsu.find(node)
                    arr = groups.get(root, [])
                    res.append(arr[0] if arr else -1)
            else:
                # Step 7: Mark node offline and update group
                if not isOffline[node]:
                    isOffline[node] = True
                    root = dsu.find(node)
                    arr = groups.get(root, [])
                    idx = bisect.bisect_left(arr, node)
                    if idx < len(arr) and arr[idx] == node:
                        arr.pop(idx)

        # Step 8: Return final results
        return res