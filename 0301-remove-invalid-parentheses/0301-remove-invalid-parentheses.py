class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(st: str) -> bool:
            count = 0
            for char in st:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        curr_level = {s}
        
        while True:
            valid = [st for st in curr_level if isValid(st)]
            if valid:
                return sorted(list(valid))
            
            next_level = set()
            for st in curr_level:
                for i in range(len(st)):
                    if st[i] in ('(', ')'):
                        next_level.add(st[:i] + st[i+1:])
            curr_level = next_level