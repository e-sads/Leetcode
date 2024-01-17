class Solution:
    def romanToInt(self, s: str) -> int:
        st = s.strip().lower()
        ans = 0
        temp = 0

        for i in st:
            
            if (i == 'm'):
                ans += 1000
                if (temp != 0 and st[temp-1] == 'c'):
                    ans-=200
            elif (i == 'd'):
                ans += 500
                if (temp != 0 and st[temp-1] == 'c'):
                    ans-=200
            elif (i == 'c'):
                ans += 100
                if (temp != 0 and st[temp-1] == 'x'):
                    ans-=20
            elif (i == 'l'):
                ans += 50
                if (temp != 0 and st[temp-1] == 'x'):
                    ans-=20
            elif (i == 'x'):
                ans += 10
                if (temp != 0 and st[temp - 1] == 'i'):
                    ans-=2
            elif (i == 'v'):
                ans += 5
                if (temp != 0 and st[temp - 1] == 'i'):
                    ans -= 2

            elif (i == 'i'):
                ans += 1
            temp += 1 
        return ans