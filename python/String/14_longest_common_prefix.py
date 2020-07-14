class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            s = min(len(prefix), len(strs[i]))
            for j in range(s):
                if prefix[j] != strs[i][j]:
                    prefix = prefix[0:j - 1]
                    break

        if prefix:
            return ""

        return prefix

a = Solution()
str = ["flower","flow","flight"]
print(a.longestCommonPrefix(str))
