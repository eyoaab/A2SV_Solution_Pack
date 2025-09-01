class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def gain(val, total):
            return (val + 1) / (total + 1) - val / total

        heap = []
        sum_ = 0.0

        for val, total in classes:
            sum_ += val / total
            heappush(heap, (-gain(val, total), val, total))

        for _ in range(extraStudents):
            current_gain, val, total = heappop(heap)
            sum_ -= val / total
            val += 1
            total += 1
            sum_ += val / total
            heappush(heap, (-gain(val, total), val, total))

        return sum_ / len(classes)