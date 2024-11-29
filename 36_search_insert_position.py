nums = [1,2,3,5,6]
target = 7

class Solution(object):
    def searchInsert(self, nums, target):

        if target not in nums:
            nums.append(target)
            nums.sort()

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif target < nums[mid]:
                right = mid - 1

            else:
                left = mid + 1

test = Solution()
print(test.searchInsert(nums, target))