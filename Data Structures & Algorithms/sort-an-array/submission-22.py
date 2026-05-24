class Solution:
    def sortArray(self, nums):

        def quicksort(left, right):

            # Base case
            if left >= right:
                return

            # Choose pivot
            pivot = nums[(left + right) // 2]

            # Two pointers
            i = left
            j = right

            # Partition
            while i <= j:

                # Find value >= pivot from left
                while nums[i] < pivot:
                    i += 1

                # Find value <= pivot from right
                while nums[j] > pivot:
                    j -= 1

                # Swap wrong values
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]

                    i += 1
                    j -= 1

            # Sort left side
            quicksort(left, j)

            # Sort right side
            quicksort(i, right)

        quicksort(0, len(nums) - 1)

        return nums