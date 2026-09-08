#https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#https://leetcode.com/submissions/detail/2135334912/

#8 September 2026

class Solution:
    def maxProduct(self, words):
        maximum = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):

                if len(set(words[i]) & set(words[j])) == 0:
                    maximum = max(maximum, len(words[i]) * len(words[j]))

        return maximum

"""
if set(words[i]).isdisjoint(set(words[j])):
we can also use the isdisjoint()
"""