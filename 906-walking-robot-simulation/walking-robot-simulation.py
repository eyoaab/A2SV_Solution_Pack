class Solution:
    def robotSim(self,commands,obstacles):
        x,y,d = 0,0,0
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        answer = 0
        obstacles = set(map(tuple,obstacles))
        
        for cmd in commands:
            if cmd == -1:
                d = (d+1) % 4
            elif cmd == -2:
                d = (d-1) % 4
            else:
                for _ in range(cmd):
                    nweX,newY = x + direction[d][0], y + direction[d][1]
                    if (nweX,newY) in obstacles:
                        break
                    x,y = nweX,newY

                    answer = max(answer, x*x + y*y)
        
        return answer