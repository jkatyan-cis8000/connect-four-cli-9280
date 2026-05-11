def validate_column_input(user_input):
    """Validate that user input is a valid column number (1-7)."""
    try:
        col = int(user_input)
        return 1 <= col <= 7
    except ValueError:
        return False


def get_player_input(player):
    """Prompt player for column input, validate, and return 0-indexed column."""
    while True:
        user_input = input(f"Player {player}, choose a column (1-7): ")
        if validate_column_input(user_input):
            col = int(user_input) - 1
            return col
        print("Invalid input. Please enter a number between 1 and 7.")
