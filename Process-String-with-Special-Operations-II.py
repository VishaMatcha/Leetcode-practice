1class Solution:
2    def processStr(self, s: str, k: int) -> str:
3        lengths = []
4        current_length = 0
5        
6        for char in s:
7            if char.isalpha():
8                current_length += 1
9            elif char == '*':
10                if current_length > 0:
11                    current_length -= 1
12            elif char == '#':
13                current_length *= 2
14            elif char == '%':
15                pass
16            lengths.append(current_length)
17        
18        if k < 0 or k >= current_length:
19            return '.'
20        
21        for i in range(len(s) - 1, -1, -1):
22            char = s[i]
23            prev_length = lengths[i-1] if i > 0 else 0
24            
25            if char == '%':
26                k = prev_length - 1 - k
27            elif char == '#':
28                if k >= prev_length:
29                    k -= prev_length
30            elif char == '*':
31                pass
32            else:
33                if k == lengths[i] - 1:
34                    return char
35                
36        return '.'