class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [([0] * n) for _  in range(n)]
        
        T = 0
        D = n - 1
        L = 0
        R = n - 1
        
        r = 0
        c = 0
        val = 1
        
        while T <= D:
            c = L
            while c <= R:
                matrix[T][c] = val
                c += 1
                val += 1
            T += 1
            
            r = T
            while r <= D:
                matrix[r][R] = val
                r += 1
                val += 1
            R -= 1
            
            c = R
            while c >= L:
                matrix[D][c] = val
                c -= 1
                val += 1
            D -= 1
            
            r = D
            while r >= T:
                matrix[r][L] = val
                r -= 1
                val += 1
            L += 1
            
        return matrix