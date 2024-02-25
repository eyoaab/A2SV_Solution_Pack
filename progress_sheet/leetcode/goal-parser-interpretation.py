class Solution:
    def interpret(self, command: str) -> str:

        good_str=command.replace('()','o')
        good_str= good_str.replace('(al)','al')

        return good_str