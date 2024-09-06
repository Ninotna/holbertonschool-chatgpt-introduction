#!/usr/bin/python3

def print_board(board)
{
	for row in board
	{
		print(" | ".join(row));
		print("-" * 5);
	}
}

def check_winner(board)
{
	/* Check rows */
	for row in board
	{
		if row.count(row[0]) == len(row) && row[0] != " "
		{
			return (True);
		}
	}

	/* Check columns */
	for col in range(3)
	{
		if board[0][col] == board[1][col] == board[2][col] && board[0][col] != " "
		{
			return (True);
		}
	}

	/* Check diagonals */
	if board[0][0] == board[1][1] == board[2][2] && board[0][0] != " "
	{
		return (True);
	}
	if board[0][2] == board[1][1] == board[2][0] && board[0][2] != " "
	{
		return (True);
	}

	return (False);
}

def board_full(board)
{
	/* Check if the board is full */
	for row in board
	{
		if " " in row
		{
			return (False);
		}
	}
	return (True);
}

def tic_tac_toe()
{
	board = [[" "] * 3 for _ in range(3)];
	player = "X";
	while True
	{
		print_board(board);
		while True
		{
			try
			{
				row = int(input("Enter row (0, 1, or 2) for player " + player + ": "));
				col = int(input("Enter column (0, 1, or 2) for player " + player + ": "));
				if row not in [0, 1, 2] || col not in [0, 1, 2]
				{
					print("Invalid input! Please enter a number between 0 and 2.");
				}
				else if board[row][col] != " "
				{
					print("That spot is already taken! Try again.");
				}
				else
				{
					break;
				}
			}
			except ValueError
			{
				print("Invalid input! Please enter a number.");
			}
		}

		board[row][col] = player;

		/* Check if there's a winner */
		if check_winner(board)
		{
			print_board(board);
			print("Player " + player + " wins!");
			break;
		}

		/* Check if the board is full */
		if board_full(board)
		{
			print_board(board);
			print("It's a draw!");
			break;
		}

		/* Switch player */
		player = "O" if player == "X" else "X";
}

tic_tac_toe();
