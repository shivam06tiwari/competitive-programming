class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        l = 0
        r = 1e9+1
        ans = 0
        while r-l > 1e-5:
            up = 0
            down = 0
            m = l + (r-l)/2
            for i in range(len(squares)):
                if m >= squares[i][1]+squares[i][2]:
                    up += 0
                    down += squares[i][2]**2
                elif m <= squares[i][1]:
                    up += squares[i][2]**2
                    down += 0
                else:
                    up += squares[i][2]*(squares[i][1]+squares[i][2]-m)
                    down += squares[i][2]*(m-squares[i][1])
            if up <= down:
                ans = m
                r = m
            else:
                l = m
        return(ans)