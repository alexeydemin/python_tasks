class Solution:
    def twoSum(self, nums, target):
        ndict = {}
        for i, a in enumerate(nums):
            if(target-a in ndict):
                return (ndict[target-a], i)
            else:
                ndict[a] = i


a = Solution.twoSum(None, [2, 3, 5, 6, 11, 15, 17], 16)
print(a)

# def simpleArraySum(ar):
#     sum = 0
#     for a in ar:
#         sum += a
#     return sum
#
#
# print (simpleArraySum([1, 2, 3, 4, 5]))
