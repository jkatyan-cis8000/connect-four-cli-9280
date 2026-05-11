# Design Doc: Board Module

## Overview
The `board` module provides core functionality for managing the Connect Four game state.

## Functions

### `create_board()`
- Returns a 6x7 grid (list of lists) initialized with empty spaces (' ')
- Indexes: rows 0-5, columns 0-6

### `display_board(board)`
- Prints the board to stdout
- Shows column numbers (1-7) at the bottom for player reference
- Uses pipe characters for visual separation

### `is_valid_location(board, col)`
- Checks if the top row (row 0) in the specified column is empty
- Returns `True` if the column is valid for placing a piece
- Column must be 0-indexed (0-6)

### `get_next_open_row(board, col)`
- Finds the lowest empty row in the specified column
- Iterates from bottom (row 5) to top (row 0)
- Returns the row index where a piece can land
- Returns -1 if column is full (should not be called if `is_valid_location` is checked first)

## Implementation Details
- Board uses 0-indexed coordinates internally
- Player-facing column input is 1-indexed (1-7), converted to 0-indexed (0-6)
- Empty cells are represented by single space character ' '
