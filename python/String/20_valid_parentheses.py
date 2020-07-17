# # method 1
# class Solution:
#     def isValid(self, s):
#         mapping = {')':'(',
#                   ']': '[',
#                   '}': '{'}
#         stack = [] # creat stack
#         if len(s) == 0:
#             return True
#         elif len(s) % 2 == 1:
#             return False
#         else:
#             for p in s:
#                 if p in mapping: # go though the key of duct
#                     if stack: # judge if the stack is empty
#                         top_p = stack.pop()
#                         if top_p != mapping[p]:
#                             return False
#                     else:
#                         return False
#                 else:
#                     stack.append(p)
#
#             return not stack
# # con: time complex O(n), not an idea method

# method 2
class Solution:
    def isValid(self, s):
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''
# con: time complexity O(n)

a = Solution()
s = '(([]))'
print(a.isValid(s))


