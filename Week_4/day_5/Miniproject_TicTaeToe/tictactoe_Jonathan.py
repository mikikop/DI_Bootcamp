"""A text base TIC TAC TOE game."""
​
EMPTY = " "
X = "X"
O = "O"
​
def initialize_game():
	"""Initializes the game state: Clear board, Player X turn, Turn message, turn counter"""
	board = [
		[EMPTY,EMPTY,EMPTY],
		[EMPTY,EMPTY,EMPTY],
		[EMPTY,EMPTY,EMPTY],
	]
​
	player_mark = X
​
	message = "Player " + player_mark + "'s turn...\n"
​
	turn_counter = 0
​
	return (board, player_mark, message, turn_counter)
​
​
def display_game(board, message):
	"""Prints the board and game message."""
	text = "\nTIC TAC TOE\n*****************\n"
	for row in range(3):
		text += "*  "
		for col in range(3):
			value = EMPTY if board[row][col] == EMPTY else board[row][col]
			text += " " + value + " |"
		text = text[:len(text) - 1]	+ "  *"
		text += "\n*  ---|---|---  *\n"
	
	text = text[:len(text) - 18]
	text += "*****************\n"
	print(text)
	print(message)
​
​
def get_coordinates():
	"""Gets input coords from user and validates them coords."""
	allowed_range = [0,1,2]
	row = int(input("Enter row: ")) - 1
	col = int(input("Enter column: ")) - 1
​
	if row not in allowed_range or col not in allowed_range:
		print("Invalid Entry. Please try again.")
		return get_coordinates() #recursive
	
	return (row, col)
​
​
def update_game(board, row, col, player_mark, turn_counter):
	"""Updates the game state. Marks the board and messages the players."""
	if board[row][col] != EMPTY:
		print("You can't go there!")
		player_mark = switch_player(player_mark) # Because upcoming check_status will switch it back
		return (board, player_mark)
​
	turn_counter += 1	
	board[row][col] = player_mark
	return (board, player_mark, turn_counter)
​
​
def check_status(board, player_mark, turn_counter):
	"""Checks game status. Win vs In Play vs Draw."""
​
	if row_win(board) or col_win(board) or diag_win(board):
		message = "Player " + player_mark + " wins!"
		player_mark = "GG"
	elif turn_counter == 9:
		message = "The game is a draw!"
		player_mark = "GG"
	else:
		player_mark = switch_player(player_mark)
		message = "Player " + player_mark + "'s turn...\n"
​
	return (player_mark, message)
​
​
def play():
	"""Runs the main game loop..."""
	print("Welcome to TIC TAC TOE!")
	board, player_mark, message, turn_counter = initialize_game();
	while player_mark != "GG":
		display_game(board, message)
		row,col = get_coordinates()
		board, player_mark, turn_counter = update_game(board, row, col, player_mark, turn_counter)
		player_mark, message = check_status(board, player_mark, turn_counter)
	else:
		display_game(board, message)
​
​
def switch_player(player_mark):
	"""Switches player turn."""
	player_mark = X if player_mark == O else O
	return player_mark
​
​
def row_win(board):
	"""Checks rows for win status."""
	for row in range(3):
		if board[row][0] != EMPTY and board[row][0] == board[row][1] == board[row][2]:
			return True
	return False
​
​
def col_win(board):
	"""Checks columns for win status."""
	for col in range(3):
		if board[0][col] != EMPTY and board[0][col] == board[1][col] == board[2][col]:
			return True
	return False
​
​
def diag_win(board):
	"""Checks diagonals for win status."""
	if board[1][1] != EMPTY and (board[1][1] == board[0][2] == board[2][0] or board[1][1] == board[0][0] == board[2][2]):
		return True
	return False
​
​
if __name__ == "__main__":
	play()