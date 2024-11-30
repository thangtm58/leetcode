n = 5

class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return '1'

        prev = self.countAndSay(n-1)
        result = ''
        i = 0
        while i < len(prev):
            curr = prev[i]
            count = 0
            while i < len(prev) and prev[i] == curr:
                count +=1
                i +=1
            result = result + str(count) + curr

        return result

test = Solution()
print(test.countAndSay(n))