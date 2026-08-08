from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # suffix[j] = latest possible index in word1 that can be used
        # to start an exact subsequence matching word2[j:]
        suffix = [-1] * (m + 1)
        suffix[m] = n

        i = n - 1

        # Match word2 from right to left
        for j in range(m - 1, -1, -1):
            while i >= 0 and word1[i] != word2[j]:
                i -= 1

            if i < 0:
                break

            suffix[j] = i
            i -= 1

        ans = []
        j = 0
        changed = False

        # Greedily choose the smallest possible indices
        for i in range(n):
            if j == m:
                break

            # Exact match: always take it
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed different character
            elif not changed:
                # After using the mismatch here, the rest of word2
                # must be exactly matchable after index i.
                if j == m - 1 or (
                    suffix[j + 1] != -1 and i < suffix[j + 1]
                ):
                    ans.append(i)
                    j += 1
                    changed = True

        return ans if j == m else []