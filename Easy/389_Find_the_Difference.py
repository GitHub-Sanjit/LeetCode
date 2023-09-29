from collections import Counter
# s = "Sanjit"
# t = "Torun"
# # t = Counter("Ssaaaaanjit")

# # print(t["a"])
# q = ''.join((Counter(t) - Counter(s)).keys())
# print(q)



# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         count_s, count_t = Counter(s),Counter(t)

#         for c in count_t:
#             if c not in count_s:
#                 return c
#             if count_s[c] < count_t[c]:
#                 return c


# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         sum_s, sum_t = 0, 0
#         for c in s:
#             sum_s += ord(c)
#         for c in t:
#             sum_t += ord(c)
#         return chr(sum_t - sum_s)

# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         res = 0
#         for c in s:
#             res = res ^ ord(c)
#         for c in t:
#             res = res ^ ord(c)
#         return chr(res)
        
