class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b = ""
        for i in digits:
            b += str(i)
        digits = list(str(int(b) + 1))
        out = []
        for i in digits:
            out.append(int(i))
        return out
