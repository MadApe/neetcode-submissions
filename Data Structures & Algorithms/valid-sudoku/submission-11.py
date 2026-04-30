class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def convert_to_int(s: str) -> int | None:
            return None if s == '.' else int(s)
    
        size = len(board)
        s_size = size // 3

        values = []
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

                print(f"row={row}, col={col}, box={box}, n={n}")
                if n in squares[box] or n in rows[row] or n in columns[col]:
                    print(f"rows={rows}")
                    print(f"columns={columns}")
                    print(f"squares={squares}")
                    return False

                squares[box].add(n)
                rows[row].add(n)
                columns[col].add(n)

        return True

