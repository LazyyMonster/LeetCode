class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        allSkills = sum(skill)
        n = len(skill)
        if allSkills % (n / 2) != 0:
            return -1

        teamSkill = int(allSkills / (n / 2))

        skillDict = {}
        for s in skill:
            skillDict[s] = skillDict.get(s, 0) + 1

        chemistry = 0
        visited = set()

        for key in skillDict:
            if key in visited:
                continue

            value = skillDict[key]
            if value != skillDict.get(teamSkill - key, 0):
                return - 1
            if key * 2 == teamSkill:
                chemistry += (key * (teamSkill - key)) * int((value) / 2)
            else:
                chemistry += (key * (teamSkill - key)) * (value)
            
            visited.add(teamSkill - key)
            
        return chemistry