# heap sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapify(nums, n, i): # n the size of the heap that we are working on
        # the index of the current node we want to fix
            largest = i

            left = 2 * i + 1 # left children of index i
            right = 2 * i + 2 # right children of index i

            if left < n and nums[left] > nums[largest]:
                largest = left
            
            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]

                heapify(nums, n, largest) # this part help us recheck the node that we have gone throught before (we have to check again after swapping)
        
        n = len(nums)
            
        # build max heap
        # in heap: nodes after n//2 - 1 are leaves and we dont need to heapify them
        for i in range(n//2 - 1, -1, -1):
            heapify(nums, n, i)
        
        # move the biggest element to the end
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, i, 0)
        
        return nums
