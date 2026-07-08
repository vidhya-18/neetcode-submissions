class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=collections.defaultdict(set)
        c=collections.defaultdict(set)
        s=collections.defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col]!='.':
                    val=board[row][col]
                    if  val in r[row] or val in c[col] or  val in s[row//3,col//3]:
                        return False
                    r[row].add(val)
                    c[col].add(val)
                    s[row//3,col//3].add(val) 
        return True           