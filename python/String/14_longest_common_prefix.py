# method 1
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        cp = ''
        l = [len(st) for st in strs] #lengths for each string
        for i in range(min(l)): # scan from first letter to min str lengths
            tmp = [s[i] for s in strs] #get i-th letter from each string
            if min(tmp)==max(tmp): #check if all of them are the same， min(string) find the smallest of string
                cp = cp + tmp[0]
            else:
                return cp
        return cp
# con: by using the min size of string to speed the time complexity; min(string)

# class Solution:
#     def longestCommonPrefix(self, strs):
#         if len(strs) == 0:
#             return ""
#         prefix = strs[0]
#         for i in range(1, len(strs)):
#             s = min(len(prefix), len(strs[i]))
#             for j in range(s):
#                 if prefix[j] != strs[i][j]:
#                     prefix = prefix[0:j - 1]
#                     break
#
#         if prefix:
#             return ""
#
#         return prefix


a = Solution()
str = ["flower","flow","flight"]
print(a.longestCommonPrefix(str))
