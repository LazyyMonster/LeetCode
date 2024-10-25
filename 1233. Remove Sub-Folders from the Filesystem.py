class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folSet = set(folder)
        folders = []
        for f in folder:
            splitted = f.split("/")[1:]
            prefix = ""
            exist = False
            for sub in splitted[:-1]:
                prefix += "/" + sub 
                if prefix in folSet:
                    exist = True
                    break
            if not exist:
                folders.append(f)
            
        return folders