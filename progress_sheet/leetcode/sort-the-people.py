class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_dict = zip(heights, names)
        sorted_dict = sorted(height_dict, reverse=True)
        return [name for height, name in sorted_dict]