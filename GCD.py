class Solution(object):
    def gcdPairSum(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        prefix = []
        mx = 0

        for x in nums:
            if x > mx:
                mx = x
            prefix.append(gcd(x, mx))

        prefix.sort()

        left = 0
        right = len(prefix) - 1
        ans = 0

        while left < right:
            ans += gcd(prefix[left], prefix[right])
            left += 1
            right -= 1

        return ans