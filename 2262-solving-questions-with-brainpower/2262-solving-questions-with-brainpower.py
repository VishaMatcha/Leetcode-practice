class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        c = [0] * len(questions)
        def btm(i):
            if i >= len(questions):
                return 0
            if c[i]:
                return c[i]
            reward, cost = questions[i]
            c[i] = max(btm(i+1),reward + btm(i+1+cost))
            return c[i]
        return btm(0)