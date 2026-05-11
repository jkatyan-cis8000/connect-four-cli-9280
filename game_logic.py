def drop_piece(board, row, col, piece):
    """Place a piece at the specified position on the board."""
    board[row][col] = piece


def check_win(board, piece):
    """Check if the given piece has won by getting 4 in a row."""
    for row in range(6):
        for col in range(7):
            if board[row][col] == piece:
                if check_direction(board, row, col, 0, 1, piece):
                    return True
                if check_direction(board, row, col, 1, 0, piece):
                    return True
                if check_direction(board, row, col, 1, 1, piece):
                    return True
                if check_direction(board, row, col, 1, -1, piece):
                    return True
    return False


def check_direction(board, row, col, delta_row, delta_col, piece):
    """Check for 4 consecutive pieces in a direction."""
    count = 0
    for i in range(4):
        r = row + i * delta_row
        c = col + i * delta_col
        if 0 <= r < 6 and 0 <= c < 7 and board[r][c] == piece:
            count += 1
        else:
            break
    return count == 4


def check_draw(board):
    """Check if the board is full (draw condition)."""
    for col in range(7):
        if board[0][col] == ' ':
            return False
    return True
