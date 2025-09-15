class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        count = 0
        
        for word in text.split():
            if not (set(word) & broken):
                count += 1
        return count