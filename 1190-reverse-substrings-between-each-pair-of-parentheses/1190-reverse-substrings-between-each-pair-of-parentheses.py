class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current = []
        
        for char in s:
            if char == '(':
                stack.append(current)
                current = []
            elif char == ')':
                current.reverse()
                prev = stack.pop()
                current = prev + current
            else:
                current.append(char)
                
        return "".join(current)