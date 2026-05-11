#!/usr/bin/env python3
"""Main Connect Four game loop and integration."""

from board import create_board, display_board, get_next_open_row
from input import get_player_input
from game_logic import drop_piece, check_win, check_draw


def main():
    """Main game loop."""
    board = create_board()
    current_player = 'X'
    
    while True:
        display_board(board)
        col = get_player_input(current_player)
        
        row = get_next_open_row(board, col)
        if row < 0:
            print("Column is full. Choose another column.")
            continue
        
        drop_piece(board, row, col, current_player)
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()
