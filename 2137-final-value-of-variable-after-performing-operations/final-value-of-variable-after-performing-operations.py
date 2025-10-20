class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return operations.count("++X") + operations.count("X++") -  operations.count("--X") - operations.count("X--")