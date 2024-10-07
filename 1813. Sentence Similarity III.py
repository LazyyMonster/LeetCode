class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        
        if len(sentence1) == len(sentence2):
            return False
        
        arr1 = sentence1.split(" ")
        arr2 = sentence2.split(" ")
        arr1Len = len(arr1)
        arr2Len = len(arr2)
        if arr1Len < arr2Len:
            if arr2[:arr1Len] == arr1:
                return True
            if arr2[-arr1Len:] == arr1:
                return True
            if arr1[0] != arr2[0] or arr1[-1] != arr2[-1]:
                return False
            
            if arr1[0] == arr2[0] and arr1[-1] == arr2[-1]:
                for c, w in enumerate(arr1):
                    if w != arr2[c]:
                        break
            if arr1[c:] == arr2[-(arr1Len - c):]:
                return True

        else:
            if arr1[:arr2Len] == arr2:
                return True
            if arr1[-arr2Len:] == arr2:
                return True
            if arr1[0] != arr2[0] or arr1[-1] != arr2[-1]:
                return False
            
            if arr1[0] == arr2[0] and arr1[-1] == arr2[-1]:
                for c, w in enumerate(arr2):
                    if w != arr1[c]:
                        break
            if arr2[c:] == arr1[-(arr2Len - c):]:
                return True

        return False