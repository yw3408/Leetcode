# method 1
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        } # creat a dict
        num = 0
        for i, e in enumerate(s): # i represent the index, and e represent the element
            if i < len(s) - 1 and roman[e] >= roman[s[i + 1]]:  # for dict use []
                num = num + roman[e]
            elif i == len(s) - 1:  # special situation
                num = num + roman[e]
            else:
                num = num - roman[e]
        return num

