class Solution:
    def romanToInt(self, s: str) -> int:
        a = {"I": 1,
             "V" : 5,
             "X" : 10,
             "L" : 50,
             "C" : 100,
             "D" : 500,
             "M" : 1000}
        ans = 0
        for i in range( len(s) - 1):
            if a[s[i]] < a[s[i+1]]:
                ans = ans - a[s[i]]
            else:
                ans = ans + a[s[i]]
        ans = ans + a[s[-1]]
        return ans