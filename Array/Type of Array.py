class Solution:
    def maxNtype(self , arr):
        if arr[0] == min(arr) and arr[-1] == max(arr):
            return 1
        elif arr[0] == max(arr) and arr[-1] == min(arr):
            return 2
        elif arr[0] < arr[-1]:
            return 3
        else:
            return 4
