# Design Doc: Main Game Module

## Overview
The `main` module integrates all components and implements the Connect Four game loop.

## Functions

### `drop_piece(board, row, col, piece)`
- Places a player's piece on the board at the specified position
- Updates `board[row][col]` with the piece ('X' or 'O')

### `check_win(board, piece)`
- Checks for four consecutive pieces in all directions:
  - **Horizontal**: Checks rows for 4 consecutive pieces
  - **Vertical**: Checks columns for 4 consecutive pieces
  - **Diagonal (down-right)**: Checks bottom-left to top-right diagonals
  - **Diagonal (up-right)**: Checks top-left to bottom-right diagonals
- Returns `True` if a win is detected

### `check_draw(board)`
- Checks if the top row is completely full
- Returns `True` if no more moves are possible

### `main()`
- Initializes the game board
- Alternates between players X and O
- Loop executes:
  1. Display current board state
  2. Get player input (column choice)
  3. Validate and drop the piece
  4. Check for win condition
  5. Check for draw condition
  6. Switch to next player
- Prints winner or draw message at end

## Integration
- Imports from `board` module: `create_board`, `display_board`, `is_valid_location`, `get_next_open_row`
- Imports from `input` module: `get_player_input`
