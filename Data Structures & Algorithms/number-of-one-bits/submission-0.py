class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([c for c in bin(n)[2:] if c=="1"])
        