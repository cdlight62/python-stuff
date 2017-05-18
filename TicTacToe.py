def game_board(board):
    for y in range(len(board)):
        print(" ---" * len(board))
        for x in range(len(board)):
            print("| " + (board[y][x] if board[y][x] else " ") + " ", end="")
        print("|")
    print(" ---" * len(board))

def check_winner(board):
    for x in range(len(board)):
        if len(set(board[x])) == 1:
            return board[x][0]
        if len(set([board[0][x], board[1][x], board[2][x]])) == 1:
            return board[0][x]
    if len(set([board[0][0], board[1][1], board[2][2]])) == 1:
        return board[1][1]
    if len(set([board[0][2], board[1][1], board[2][0]])) == 1:
        return board[1][1]

if __name__ == "__main__":
    # size = int(input("Enter size of game board:"))
    game = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]]
    player_turn = 1
    moves = 0
    winner = ""
    while moves < 9:
        game_board(game)
        winner = check_winner(game)
        if winner:
            break
        move = [int(x) for x in input("Player " + str(player_turn) + "'s move (row,col): ").split(",")]
        while game[move[0]][move[1]]:
            move = [int(x) for x in input("That move is taken. Enter a different move (row,col): ").split(",")]
        game[move[0]][move[1]] = "x" if player_turn == 1 else "o"
        player_turn = 2 if player_turn == 1 else 1
        moves += 1

    print("Player " + str(winner) + " wins!" if winner else "Draw")