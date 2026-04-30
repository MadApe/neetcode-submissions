class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        s_size = size // 3

        rows = {}
        squares = {}
        columns = {}
        for i in range(size):
            squares[i] = set()
            rows[i] = set()
            columns[i] = set()

        for row in range(size):
            for col in range(size):
                box = (row // s_size) * s_size + col // s_size
                if board[row][col] == '.':
                    continue
                
                n = int(board[row][col])
                if n in squares[box] or n in rows[row] or n in columns[col]:
                    return False

                squares[box].add(n)
                rows[row].add(n)
                columns[col].add(n)

        return True

