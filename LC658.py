class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0 
        high = len(arr) - k 
        while low  < high:
            mid = low + (high - low) //2
            print(low, high)
            if x - arr[mid] > arr[mid+k] - x:
                low = mid + 1
            else:
                high = mid
        print(low,high)
        # if x - arr[low] > arr[high] - x:
        #     return arr[high:high+k]
        # else:
        return arr[low:low + k]
        
