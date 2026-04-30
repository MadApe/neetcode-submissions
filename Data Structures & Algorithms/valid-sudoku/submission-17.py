class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)
        s_size = size // 3

        # rows = defaultdict(set)
        # columns = defaultdict(set)
        # squares = defaultdict(set)

        rows = {}
        columns = {}
        squares = {}

        for i in range(size):
            rows[i] = set()
            columns[i] = set()
            squares[i] = set()
        
        for row in range(size):
            for col in range(size):
                square = (row // s_size) * s_size + col // s_size
                if board[row][col] == '.':
                    continue
                
                n = int(board[row][col])
                if n in squares[square] or n in rows[row] or n in columns[col]:
                    return False

                squares[square].add(n)
                rows[row].add(n)
                columns[col].add(n)

        return True

