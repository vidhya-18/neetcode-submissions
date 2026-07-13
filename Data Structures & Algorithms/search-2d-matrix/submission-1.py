class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left,right=0,m*n-1
        while(left<=right):
            med=(left+right)//2
            row,col=med//n,med%n
            if(matrix[row][col]==target):
                return True
            elif(matrix[row][col]<target):
                left=med+1
            else:
                right=med-1
        return False               