class Solution:
    def getSum(self, a: int, b: int) -> int:

        MASK = 0xffffffff
        MAX = 0x7fffffff

        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK

        if a <= MAX:
            return a
        else:
            return ~(a ^ MASK)