class Solution:
    def sortArray(self, nums):
        
        def radix_sort(arr):
            if not arr:
                return arr

            max_num = max(arr)
            exp = 1

            while max_num // exp > 0:
                counting_sort(arr, exp)
                exp *= 10

            return arr

        def counting_sort(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for num in arr:
                digit = (num // exp) % 10
                count[digit] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            for i in range(n - 1, -1, -1):
                digit = (arr[i] // exp) % 10
                output[count[digit] - 1] = arr[i]
                count[digit] -= 1

            for i in range(n):
                arr[i] = output[i]

        negatives = [-x for x in nums if x < 0]
        positives = [x for x in nums if x >= 0]

        radix_sort(negatives)
        radix_sort(positives)

        negatives = [-x for x in negatives]
        negatives.reverse()

        return negatives + positives