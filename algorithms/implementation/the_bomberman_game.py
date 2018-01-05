R, C, N = map(int, input().split())
board = [[c for c in input()] for row in range(R)]


def progress_one_detonation_cycle(current_board):
    """Calculates the configuration of the board after filling all squares with
    bombs then detonating the bombs in the initial board.
    """
    R = len(current_board)
    C = len(current_board[0])
    new_board = [["O" for column in range(C)] for row in range(R)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    # Calculate board after one detonation cycle.
    for i in range(R):
        for j in range(C):
            if current_board[i][j] == "O":
                # Fill this bomb and neighbouring squares as not bombs
                # on the new board.
                new_board[i][j] = "."
                for x, y in zip(dx, dy):
                    if 0 <= i + y < R and 0 <= j + x < C:
                        new_board[i + y][j + x] = "."
    return new_board


configuration_1 = progress_one_detonation_cycle(board)
configuration_2 = progress_one_detonation_cycle(configuration_1)

# N = 0 or 1 then initial configuration
# If N >= 2 even then all bombs
# N = 3 mod 4 then configuration 1
# N = 1 mod 4 then configuration 2
if N == 0 or N == 1:
    print("\n".join("".join(c for c in row) for row in board))
elif N % 2 == 0:
    print("\n".join("O" * C for row in range(R)))
elif N % 4 == 3:
    print("\n".join("".join(c for c in row) for row in configuration_1))
elif N % 4 == 1:
    print("\n".join("".join(c for c in row) for row in configuration_2))
