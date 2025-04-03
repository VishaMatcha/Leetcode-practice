class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        c = [0]*len(questions)
        def most(i):
            if i >= len(questions):
                return 0
            if c[i]:
                return c[i]
            reward, cost = questions[i]
            c[i] = max(most(i+1),reward+most(i+1+cost))
            return c[i]
        return most(0)