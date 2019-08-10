PLAYERS = {1: "X", 2: "O"}
TURN = 1

TURNS_LEFT = 9


def make_new_board():
    # Creates a new board to start the game with.

    return [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]

def add_piece(board, coords):
    # Adds the piece to the board at the selected coords.
    
    board[coords[0]][coords[1]] = PLAYERS[TURN]
    _switch_turns()
    return board

def winner(board) -> int:
    # Checks every possible win condition for a potential win. If there are none, then
    # the function will check if there have been 9 turns made, effectively meaning that
    # a draw has happened. 
    
    global TURNS_LEFT
    win = False
        
    for row in board:
        if (row[0]==row[1] and row[1]==row[2]) and row[0] != " ":
            win = True
            return(row[0])

    for i in range(3):
        if (board[0][i]==board[1][i] and board[1][i]==board[2][i]) and board[0][i] != " ":
            win = True
            return(board[0][i])

    if (board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]) and board[1][1] != " ":
        win = True
        return(board[1][1])

    else:
        if TURNS_LEFT == 0 and win == False:
            return("DRAW")
        return None

def validate_type(prop_type):
    return _validate_type(prop_type)

def validate_turn(board, row, column):
    return _validate_turn(board, row, column)

def _validate_type(prop_type):
    if prop_type == "AI" or prop_type == "Human":
        return True
    return False


def _validate_turn(board, row, column):
    try:
        int(row)
        int(column)
    except:
        return False

    row, column = int(row)-1, int(column)-1
    if row not in range(3) or column not in range(3):
        return False
    
    if board[row][column] == " ":
        return True
    return False

def _switch_turns():
    global TURN
    global TURNS_LEFT

    TURNS_LEFT -= 1
    TURN = 2 if TURN == 1 else 1


