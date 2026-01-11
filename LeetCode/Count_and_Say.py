class Solution:
    def countAndSay(self, n: int) -> str:
        z = "1"
        for i in range(n-1):
            if len(z) == 1:
                z = "1" + z
            else:
                c = 0
                x = ""
                for j in range(len(z)-1):
                    if z[j] == z[j+1]:
                        if c == 0:
                            c += 2
                        else:
                            c += 1
                    else:
                        if c == 0:
                            x += "1"+z[j]
                        else:
                            x += str(c)+z[j]
                        c = 0
                if c == 0:
                    x += "1"+z[j+1]
                else:
                    x += str(c)+z[j+1]
                z = x
        return(z)