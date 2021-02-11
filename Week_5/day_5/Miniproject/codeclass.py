allowed_list = [
	(0,1),
	(0,3),
	(0,5),
	(0,7),
	(1,0),
	(1,2),
	(1,4),
	(1,6),
	(2,1),
	(2,3),
	(2,5),
	(2,7),
	(3,0),
	(3,2),
	(3,4),
	(3,6),
	(4,1),
	(4,3),
	(4,5),
	(4,7),
	(5,0),
	(5,2),
	(5,4),
	(5,6),
	(6,1),
	(6,3),
	(6,5),
	(6,7),
	(7,0),
	(7,2),
	(7,4),
	(7,6)
]


class Piece:
	
	def __init__(self, player,coordonates,name):
		self.player = player
		self.coordonates = coordonates
		self.name = name

	def flip_piece(self):
		return self.color = 'x' if self.color == 'o' else self.color == 'o'
			
	def __repr__(self):
		return f'{self.name}'

class Game:
	
	def __init__(self, allowed_list):
		self.allowed_list = allowed_list
		self.p1 = Player('x')
		self.p2 = Player('o')
		self.pieces = []
		self.board = {key: None for key in allowed_list}
		for player in [self.p1, self.p2]:
			if self.pieces:
				coo_list = allowed_list[::-1]
			else:
				coo_list = allowed_list
			for i,coo in zip(range(1,13), coo_list):
				piece = Piece(player,coo,player.color+str(i))
				self.pieces.append(piece)
				self.board[coo] = piece
		
		#print(self.pieces)		
		print(self.board)





class Player:
	
	def __init__(self, color):
		self.color = color

	def move(self,from_pos, to_pos):
		to_pos_int = eval(to_pos)
		from_pos_int = eval(from_pos)

		if to_pos_int not in coordonates_allowed:
			print("you entered wrong coordonates!")
			exit()		
		for key,value in board_game.items():
			if key == to_pos_int:
				if value == 0:
					board_game[key] = 1
					board_game[from_pos] = 0
				else:
					# from_pos is like (0,3) and to_pos is like (1,4)
					if from_pos_int[1]<to_pos_int[1]:
						if board_game[to_pos_int[0]+1][to_pos_int[1]+1] == 0:
							board_game[to_pos_int[0]+1][to_pos_int[1]+1] = 1
							board_game[from_pos_int] = 0
							board_game[to_pos_int] = 0
					# from_pos is like (0,3) and to_pos is like (1,2)
					else:
						if board_game[to_pos_int[0]+1][to_pos_int[1]-1] == 0:
							board_game[to_pos_int[0]+1][to_pos_int[1]-1] = 1
							board_game[from_pos_int] = 0
							board_game[to_pos_int] = 0
								



if __name__ == '__main__':
	#main()
	board = Game(allowed_list)


	from_pos = '(0,3)'
	to_pos = '(1,4)'
	p1 = Player('x')
	print(board)
	p1.move(from_pos,to_pos)
	print(board)
