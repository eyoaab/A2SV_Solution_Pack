class Solution:
    def average(self, salary: List[int]) -> float:

        _min=min(salary)
        _max=max(salary)

        salary.remove(_min)
        salary.remove(_max)

        return sum(salary)/len(salary) 

        