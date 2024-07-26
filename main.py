"""Basic tic tac toe game in a cmd line interface
Player X always goes first
"""
def new_board() -> list[list[str]]:
    """Makes a new empty 3X3 board 

    Returns:
        list[list[str]]: a 3X3 board for tic tac toe
    """
    board = [ [' ']*3 for i in range(3)]
    return board

def render(board: list[list[str]]) -> None:
    """Renders the game board

    Args:
        board (list[list[str]]): 3X3 list of the game board
    """
    print("  0 1 2")
    print("  ------")
    print("0|" + " ".join(board[0])+ "|")
    print("1|" + " ".join(board[1])+ "|")
    print("2|" + " ".join(board[2])+ "|")
    print("  ------")

def change_player(player: str) -> str:
    """Switches players turn as a string

    Args:
        player (str): the current player

    Returns:
        str: the next player
    """
    if player == 'X':
        return 'O'
    else:
        return 'X'

def get_move() -> list[int]:
    """Gets a move from the user

    Returns:
        list[int]: returns the move in a list of format [row, column]
    """
    move_input = []
    move_input.append(int(input("Pick your row: ")))
    move_input.append(int(input("Pick your column: ")))
    return move_input

def make_move(board: list[list[str]], current_move: list[int], current_player: str) -> list[list[str]]:
    """Makes the given move

    Args:
        board (list[list[str]]): 3X3 list of the game board
        current_move (list[int]): the current move being performed in [row, column] format
        current_player (str): the current player as a string, 'X' or 'O'

    Raises:
        ValueError: the move given was invalid

    Returns:
        list[list[str]]: A new board with the updated move
    """
    if not is_valid_move(board, current_move):
        raise ValueError(f"{current_move} is an invalid move!")
    board_copy = board.copy()
    board_copy[current_move[0]][current_move[1]] = current_player
    return board_copy

def check_winning_row(board: list[list[str]], row: int) -> bool:
    """Checks for a winning row

    Args:
        board (list[list[str]]): 3X3 list of the game board
        row (int): row of the last played move

    Returns:
        bool: returns True if the player made a winning move
    """
    if board[row][0] == board[row][1] == board[row][2]:
        return True
    return False

def check_winning_col(board: list[list[str]], col: int) -> bool:
    """Checks for a winning column

    Args:
        board (list[list[str]]): 3X3 list of the game board
        col (int): column of the last played move

    Returns:
        bool: returns True if the player made a winning move
    """
    if board[0][col] == board[1][col] == board[2][col]:
        return True
    return False

def check_winning_diagonals(board: list[list[str]]) -> bool:
    """Checks for a winning diagonal

    Args:
        board (list[list[str]]): 3X3 list of the game board

    Returns:
        bool: returns True if the player made a winning move
    """
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[2][0] == board[1][1] == board[0][2] != ' ':
        return True
    return False

def is_winner(board: list[list[str]], current_move: list[int]) -> bool:
    """Checks if the player made a winning move

    Args:
        board (list[list[str]]): 3X3 list of the game board
        current_move (list[int]): the current move being performed in [row, column] format

    Returns:
        bool: _description_
    """
    if check_winning_row(board, current_move[0]):
        return True
    if check_winning_col(board, current_move[1]):
        return True
    if check_winning_diagonals(board):
        return True
    return False

def is_valid_move(board: list[list[str]], current_move: list[int]):
    """Checks if the move made was valid

    Args:
        board (list[list[str]]): 3X3 list of the game board
        current_move (list[int]): the current move being performed in [row, column] format

    Returns:
        _type_: Returns True if the move is valid
    """
    if current_move[0] < 0 or current_move[0] > 2:
        return False
    if current_move[1] < 0 or current_move[1] > 2:
        return False
    if board[current_move[0]][current_move[1]] != ' ':
        return False
    return True

def is_board_full(board: list[list[str]]) -> bool:
    """Checks for a full board the hard way

    Args:
        board (list[list[str]]): 3X3 list of the game board

    Returns:
        bool: Returns True if the game board is full
    """
    for col in board:
        for element in col:
            if element == ' ':
                return False
    return True

def play_again() -> bool:
    """Asks the user if they want to play again

    Returns:
        bool: Returns True if the player wants to play again
    """
    while True:
        answer = input("Do you want to play again? (Y/N): ")
        if answer in ('Y', 'y'):
            return True
        if answer in ('N', 'n'):
            return False
        print("Invalid input, try again.")

def print_scores(scores: list[int]) -> None:
    """prints out the current scores in format

    Args:
        scores (list[int]): scores in list as ['X' wins, 'O' wins, Ties]
    """
    print(f"Current score is: X:{scores[0]}, O:{scores[1]}, Ties:{scores[2]}")

def main():
    """Main drive of the script"""
    #setting up some starting conditions
    player = 'X'
    board = new_board()
    render(board)
    scores = [0, 0, 0] #storing scores as ['X' wins, 'O' wins, ties]

    #main loop
    while True:
        print(f"Player {player}'s turn!")
        move = []

        #loop until a valid move is inputted
        while True:
            move = get_move()
            if is_valid_move(board, move):
                break
            print("Invalid move, try again.")

        #update and render board
        board = make_move(board, move, player)
        render(board)
        #check end of game options
        if is_winner(board, move):
            print(f"Congratulations, Player {player} wins!")
            if player == 'X':
                scores[0] += 1 #increment 'X' win counts
            else:
                scores[1] += 1 #increment 'O' win counts
            print_scores(scores)
            if play_again():
                board = new_board()
                render(board)
            else:
                break
        if is_board_full(board):
            print("Oh thats a tie... awkward.")
            scores[2] += 1 #increment ties count
            print_scores(scores)
            if play_again():
                board = new_board()
                render(board)
            else:
                print("Thanks for playing!")
                break
        player = change_player(player)
        #repeat until done playing

main()
