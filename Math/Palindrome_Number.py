class Solution:
    def isPallindrome(self,n : int) -> bool:
        t = n
        s = 0
        if n < 0:
            return False
        while n != 0:
            r = n % 10
            s = s * 10 + r
            n = n // 10
        if s == t:
            return True
        else:
            return False

s = Solution()
n = int(input())
if s.isPallindrome(n):
    print(True)
else:
    print(False)