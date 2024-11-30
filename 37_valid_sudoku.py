board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]

class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):

            # Row check
            row = board[i]
            if (9 - row.count(".")) > (len(list(set(row))) - list(set(row)).count(".")):
                return False

            # Col check
            col = [sub[i] for sub in board]
            if (9 - col.count(".")) > (len(list(set(col))) - list(set(col)).count(".")):
                return False

        # Matrix 3x3 check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                matrix = [sub[i:i+3] for sub in board[j:j+3]]
                arr = matrix[0] + matrix[1] + matrix[2]
                if (9 - arr.count(".")) > (len(list(set(arr))) - list(set(arr)).count(".")):
                    return False


        return True
test = Solution()
print(test.isValidSudoku(board))