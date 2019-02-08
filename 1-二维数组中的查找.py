# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def find(self, target, array):
        # write code here
        if not array: return False
        for i in array:
            if self.binary_search_recursion(0, len(i), target, i): return True
        return False

    def find(self, target, array):
        # write code here
        if not array: return False
        for i in array:
            if self.binary_search_no_recursion(0, len(i), target, i): return True
        return False

    def find(self, target, array):
        # write code here
        if not array: return False
        return self.help_func(0, len(array[0]) - 1, array, target)

    def help_func(self, row, column, array, target):
        if row >= len(array) or column < 0: return False
        cur = array[row][column]
        if cur > target:
            column = column - 1
        elif cur < target:
            row = row + 1
        else:
            return True
        return self.help_func(row, column, array, target)

    def binary_search_recursion(self, left, right, target, nums):
        if left >= right: return False
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            return True
        return self.binary_search_recursion(left, right, target, nums)

    def binary_search_no_recursion(self, left, right, target, nums):
        while left < right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                return True
        return False

