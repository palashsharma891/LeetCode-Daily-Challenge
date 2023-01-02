class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        ct = 0
        if word.isupper():
            return True
        for i in range(1, n):
            if word[i].isupper():
                return False

        return True
