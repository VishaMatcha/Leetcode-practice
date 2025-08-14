class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""  
        empty = "" 
        temp = 0 
        check = True 

        for i in range(len(num) - 2):
            if i + 2 < len(num) and num[i] == num[i + 1] == num[i + 2]:

                temp = max(temp, int(num[i]))
                check = False  

        if not check:
            ans += str(temp) * 3

        else: 
            return empty  

        return ans  