class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        s = s.split()
        if len(s) != len(pattern):
            return False
        s_mapping = {}
        p_mapping = {}
        for i, c in enumerate(pattern):
            if s[i] not in s_mapping:
                s_mapping[s[i]] = c
            elif s_mapping[s[i]] != c:
                return False

            if c not in p_mapping:
                p_mapping[c] = s[i]
            elif p_mapping[c] != s[i]:
                return False

        return True
        '''
        #or
        s = s.split()
        return len(set(s)) == len(set(pattern)) == len(set(zip_longest(pattern, s)))
'''
        for key in mapping:
            if len(set(mapping[key])) > 1:# != len(set(mapping[key])):
                return False
        return True'''
