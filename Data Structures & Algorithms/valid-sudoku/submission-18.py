class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize 9 integers to 0
        # Each integer acts as a "set" of 9 bits
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                # Convert "5" -> bit 5 (1 << 5)
                # Bitwise shifting is extremely fast
                val = int(board[r][c])
                mask = 1 << val
                
                sq_idx = (r // 3) * 3 + (c // 3)
                
                # Use Bitwise AND (&) to check if the bit is already set
                if (rows[r] & mask) or (cols[c] & mask) or (squares[sq_idx] & mask):
                    return False
                
                # Use Bitwise OR (|) to "add" the number to our masks
                rows[r] |= mask
                cols[c] |= mask
                squares[sq_idx] |= mask
                
        return True