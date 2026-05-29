class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#lengths different? no
#convert the strings to lists, sort them and then check if equal!

        if len(s)!=len(t):
            return False
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        if ls==lt:
            return True
        return False