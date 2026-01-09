class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mn = 201
        ind = 0
        mnn = 201
        if len(strs) == 1:
            return(strs[0])
        for i in range(len(strs)):
            mn = len(strs[i])
            if mn < mnn:
                mnn = mn
                ind = i
        sub = ""
        for j in range(len(strs)-1):
            if j == 0:
                for k in range(mnn):
                    if strs[j][k] == strs[j+1][k]:
                        sub += strs[j][k]
                    else:
                        break
            else:
                for k in range(mnn):
                    if len(sub) >= k+1:
                        if strs[j][k] != strs[j+1][k] or strs[j][k] != sub[k]:
                            sub = sub[0:k]
                        else:
                            continue
        return(sub)

        