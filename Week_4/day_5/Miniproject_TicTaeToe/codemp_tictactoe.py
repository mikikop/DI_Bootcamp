win_combinaisons = [
	           [(0,0), (0,1), (0,2)],
	           [(1,0), (1,1), (1,2)],
	           [(2,0), (2,1), (2,2)],
	           [(0,0), (1,0), (2,0)],
	           [(0,1), (1,1), (2,1)],
	           [(0,2), (1,2), (2,2)],
	           [(0,0), (1,1), (2,2)],
	           [(2,0), (1,1), (0,2)],	
]


index_code = {
	1: (0,0),
	2: (0,1),
	3: (0,2),
	4: (1,0),
	5: (1,1),
	6: (1,2),
	7: (2,0),
	8: (2,1),
	9: (2,2)
}

board = [
	['','',''],
	['','',''],
	['','','']
]

player1 = "x"
player2 = "o"
isWinner = False

# display the board
def display_board(player,board):
	move = player_input(player)
	for i in index_code:
		if i == move:
			board[index_code[i][0]][index_code[i][1]] = player
	print("-------------")
	print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
	print("-------------")
	print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
	print("-------------")
	print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |")
	print("-------------")
	boolean = check_win()
	print(boolean)
	

#get input position of the player
def player_input(player):
	answer = ""
	while answer not in range(1,10):
		answer = int(input(f"TURN OF PLAYER {player} TO GIVE A NUMBER OF THE CELL YOU WANT TO PLAY: "))
	return answer


#check winner
def check_win():
	print("avant")
	for win_combinaison in win_combinaisons:
		print("apres for")
		if board[win_combinaison[0][0]][win_combinaison[0][1]]==board[win_combinaison[0][0]][win_combinaison[0][1]]==board[win_combinaison[0][0]][win_combinaison[0][1]]:
			print("apres if")
			print(f'player {board[win_combinaison[0][0]][win_combinaison[0][1]]} wins')
			return True
			exit()
		else:
			return False
	else:
		print('no winner')
		return True


# main function
def play(isWinner):
	print("Play by choosing one of this case: ")
	print("-------------")
	print("| 1 | 2 | 3 |")
	print("-------------")
	print("| 4 | 5 | 6 |")
	print("-------------")
	print("| 7 | 8 | 9 |")
	print("-------------")

	while isWinner == False:
		isWinner = display_board(player1,board)
		isWinner = display_board(player2,board)


play(isWinner)









