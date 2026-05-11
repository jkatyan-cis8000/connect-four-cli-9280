# Design Doc: Input Module

## Overview
The `input` module handles player input validation and conversion for the Connect Four game.

## Functions

### `validate_column_input(user_input)`
- Validates that user input can be converted to an integer
- Checks that the integer is within valid column range (1-7)
- Returns `True` if input is valid, `False` otherwise

### `get_player_input(player)`
- Prompts the specified player to choose a column
- Uses a loop to retry on invalid input
- Converts 1-indexed user input (1-7) to 0-indexed column (0-6)
- Returns the 0-indexed column number

## Implementation Details
- Input validation ensures only integers 1-7 are accepted
- Invalid inputs (non-numeric, out of range) trigger a retry with error message
- Conversion from 1-indexed to 0-indexed happens after validation
