class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        max_num = max(arr)
        max_index = arr.index(max_num)
        if max_index == len(arr) - 1 or max_index == 0: return False
        for i in range(0, max_index):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(max_index, len(arr) -1):
            if arr[i] <= arr[i+1]:
                return False
        
        return True
