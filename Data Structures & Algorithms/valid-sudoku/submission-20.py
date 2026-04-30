class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        s_size = size // 3

        rows = {}
        columns = {}
        squares = {}

        for i in range(size):
            rows[i] = set()
            columns[i] = set()
            squares[i] = set()
        
        for r in range(size):
            for c in range(size):
                square = (r // s_size) * s_size + c // s_size
                if board[r][c] == '.':
                    continue
                
                n = int(board[r][c])
                if n in squares[square] or n in rows[r] or n in columns[c]:
                    return False

                squares[square].add(n)
                rows[r].add(n)
                columns[c].add(n)

        return True

