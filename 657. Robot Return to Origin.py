class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = {"U" : 0, "D" : 0, "L" : 0, "R" : 0}

        for m in moves:
            directions[m] += 1
        
        if (directions["D"] == directions["U"]) and (directions["L"] == directions["R"]):
            return True
            
        return False