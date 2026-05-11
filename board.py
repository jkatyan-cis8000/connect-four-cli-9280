def create_board():
    """Create a 7x6 Connect Four board initialized with empty spaces."""
    board = []
    for _ in range(6):
        row = [' '] * 7
        board.append(row)
    return board


def display_board(board):
    """Display the Connect Four board with column numbers."""
    print()
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print('-' * 29)
    print('  1   2   3   4   5   6   7  ')


def is_valid_location(board, col):
    """Check if a column has space for a new piece."""
    return board[0][col] == ' '


def get_next_open_row(board, col):
    """Find the first empty row in a column where a piece can land."""
    for row in range(5, -1, -1):
        if board[row][col] == ' ':
            return row
    return -1
