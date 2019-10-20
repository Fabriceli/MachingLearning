# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-03 12:32
# @Author   : Fabrice LI
# @File     : algtest.py
# @User     : liyihao
# @Software: PyCharm
# @Description: todo
# Reference:**********************************************
import collections
import heapq
import re


class Solution(object):
    def findKthLargest_heap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        :time consuming: O(nlogk)
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res

    def findKthLargest_sort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        :time consuming: O(nlogn)
        """

        pass

    def findKthLargest_semi_quick_sort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        :time consuming: O(n)
        """
        pass

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        length = len(arr)
        left = 0
        right = length - 1
        remove_nums = length - k
        while remove_nums:
            if (x - arr[left]) >= (arr[right] - x):
                left += 1
            else:
                right -= 1
            remove_nums -= 1
        return arr[left:right + k]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if left == len(nums):
            return -1
        return left

    def searchRangeRight(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return -1
        left = 0
        right = len(nums)
        res = []
        while left < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if right == 0:
            res.append(left)
            return -1
        return right - 1 if nums[right - 1] == target else -1


def range_sum_query(nums, start, end):
    if not nums:
        return
    length = len(nums)
    sum = []
    temp = 0
    for i in range(length):
        temp = temp + nums[i]
        sum.append(temp)
    print(sum)
    res = sum[end] - sum[start] + nums[start]
    return res


def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    ans = 0
    for k, v in collections.Counter(s).items():
        ans += int(v / 2) * 2
        if ans % 2 == 0 and v % 2 == 1:
            ans += 1
    return ans


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    length_h = len(haystack)
    length_n = len(needle)
    for i in range(length_h - length_n + 1):
        if haystack[i:i + length_n] == needle:
            return i
    return -1


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return True
    s = ''.join(re.findall(r'[0-9a-zA-Z]', s))
    s = s.lower()
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0
        length = len(s)
        status = [[False for _ in range(length)] for _ in range(length)]
        res = s[0]
        long = 1
        for r in range(length):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or status[l + 1][r - 1]):
                    status[l][r] = True
                    temp = r - l + 1
                    if long < temp:
                        long = temp
                        res = s[l:r + 1]
        return res
    def test2(self, s):
        str_length = len(s)
        max_length = 0
        start = 0
        for i in range(str_length):
            if i - max_length >= 1 and s[i - max_length - 1:i + 2] == s[i - max_length - 1:i + 2][::-1]:
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >= 0 and s[i - max_length:i + 2] == s[i - max_length:i + 2][::-1]:
                start = i - max_length
                max_length += 1
        return s[start:start + max_length + 1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        r = len(obstacleGrid)
        if not r:
            return 0
        c = len(obstacleGrid[0])
        status = [[0 for _ in range(c)] for _ in range(r)]
        print(status)
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            status[0][0] = 1
        # first row
        for i in range(1, r):
            if obstacleGrid[i][0] != 1:
                status[i][0] = status[i - 1][0]
        # first clo
        for j in range(1, c):
            if obstacleGrid[0][j] != 1:
                status[0][j] = status[0][j - 1]

        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] != 1:
                    status[i][j] = status[i - 1][j] + status[i][j - 1]
        return status[-1][-1]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0
        status = [[0 for _ in range(n)] for _ in range(m)]
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(dp)
        # first row
        for i in range(n):
            status[0][i] = 1
        for j in range(m):
            status[j][0] = 1
        for j in range(1, m):
            for i in range(1, n):
                status[j][i] = status[j - 1][i] + status[j][i - 1]

        return status[-1][-1]

    def climbStairs(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        # 行
        row = len(grid)
        if row == 1:
            return sum(grid)
        # 列
        clo = len(grid[0])

        dp = [[0 for _ in range(clo)] for _ in range(row)]
        dp[0][0] = grid[0][0]

        # for first row
        for i in range(1, clo):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for j in range(1, row):
            dp[j][0] = dp[j - 1][0] + grid[j][0]
        for j in range(1, row):
            for i in range(1, clo):
                dp[j][i] = min(dp[j - 1][i], dp[j][i - 1]) + grid[j][i]

        return dp[-1][-1]

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        row = len(triangle)
        for i in range(1, row):
            triangle[i][0] += triangle[i - 1][0]
            clo = len(triangle[i])
            for j in range(1, clo - 1):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
            triangle[i][-1] += triangle[i - 1][-1]
        return min(triangle[-1])


    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        length = len(nums)
        dp = [0] * length
        dp[0] = 1
        for i in range(length):
            for j in range(i):
                if dp[j] and nums[j] + j >= i:
                    dp[i] = 1
                    break
        return True if dp[-1] else False


    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        length = len(nums)
        position = length - 1
        for i in range(length - 1, -1, -1):
            if nums[i] + i >= position:
                position = i
        return position == 0


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            # 右移
            mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid
        return left if nums[left] == target else -1

    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) << 1
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                left = mid + 1
            else:
                right = mid
        return left if left == right and nums[left] == target else -1

if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 4, 6, 2, 7]
    # start = 3
    # end = 6
    # print(nums)
    # print(range_sum_query(nums, start, end))
    # data = [1,2,3,4,5]
    # k = 4
    # x = 5
    # res = Solution()
    # print(res.findClosestElements(data, k, x))
    # data = [5, 7, 7, 8, 8, 10]
    # target = 6
    # res = Solution()
    # print(res.searchRangeRight(data, target))
    # s = "abccccdd"
    # longestPalindrome(s)
    # print(isPalindrome("A man, a plan, a canal: Panama"))
    res = Solution2()
    d = [4,5,6,7,0,1,2]
    m = 0
    n = 2
    print(res.search(d, m))
