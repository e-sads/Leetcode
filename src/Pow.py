class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n == 0):
            return 1
        if (n < 0):
            n = abs(n)
            x = pow(x,-1)

        ans = pow(x,n)
    
        return ans