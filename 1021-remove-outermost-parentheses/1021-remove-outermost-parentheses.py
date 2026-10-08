class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        level = 0
        
        for char in s:
            if char == '(':
                if level > 0:
                    res.append(char)
                level += 1
            else:
                level -= 1
                if level > 0:
                    res.append(char)
                    
        return "".join(res)