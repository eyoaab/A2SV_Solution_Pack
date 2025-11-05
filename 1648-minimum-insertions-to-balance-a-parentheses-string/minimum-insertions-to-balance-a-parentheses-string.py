class Solution:
    def minInsertions(self, s: str) -> int:
        
        missing_closed = 0 

        required_open = 0

        required_closed = 0

        prev_closed = 0

        for c in s:

            if c == '(':
                if required_closed % 2 == 1: 
                    missing_closed += 1  
                    required_closed -= 1

                required_closed += 2
                prev_closed = False
                
            else:

                if required_closed:
                    required_closed -= 1

                elif prev_closed:
                    required_closed -= 1

                else:
                    required_open += 1
                    required_closed += 1

                prev_closed = not prev_closed

        return required_open + required_closed + missing_closed