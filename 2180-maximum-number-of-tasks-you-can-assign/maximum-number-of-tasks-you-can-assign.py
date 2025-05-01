class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def can_assign(k):
            avail = worker_str[-k:]
            remain = total
            for req in reversed(task_req[:k]):
                if avail and avail[-1] >= req:
                    avail.pop()
                else:
                    if remain <= 0:
                        return False
                    threshold = req - pill_boost
                    idx = bisect_left(avail, threshold)
                    if idx == len(avail):
                        return False
                    avail.pop(idx)
                    remain -= 1
            return True

        task_req = sorted(tasks)
        worker_str = sorted(workers)
        total = pills
        pill_boost = strength
        
        low, high, answer = 0, min(len(tasks), len(workers)), 0
        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans