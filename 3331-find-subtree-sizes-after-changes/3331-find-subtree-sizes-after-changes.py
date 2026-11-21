class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n= len(parent)
        orig_children = [[] for _ in range(n)]
        for node in range(1, n):
            orig_children[parent[node]].append(node)

        new_parent = parent[:]
        last_node = [-1] * 26

        # Iterative DFS on original tree to find closest matching ancestor
        # Stack entries: (node, entering_flag, previous_ancestor_for_char)
        stack = [(0, True, -1)]
        while stack:
            u, entering, prev = stack.pop()
            c = ord(s[u]) - 97
            if entering:
                saved_prev = last_node[c]
                if u != 0 and saved_prev != -1:
                    new_parent[u] = saved_prev
                last_node[c] = u
                stack.append((u, False, saved_prev))
                for v in orig_children[u]:
                    stack.append((v, True, -1))
            else:
                last_node[c] = prev

        # Build final tree and compute subtree sizes via iterative post-order
        final_children = [[] for _ in range(n)]
        for node in range(1, n):
            final_children[new_parent[node]].append(node)

        subtree_size = [1] * n
        post_order = []
        dfs_stack = [0]
        while dfs_stack:
            u = dfs_stack.pop()
            post_order.append(u)
            for v in final_children[u]:
                dfs_stack.append(v)

        for u in reversed(post_order):
            total = 1
            for v in final_children[u]:
                total += subtree_size[v]
            subtree_size[u] = total

        return subtree_size