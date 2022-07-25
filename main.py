rows = [0, 0, 0]
columns = [0, 0, 0]

board_row_1b = "-----------"
board_row_2b = "-----------"
board_row_1a = ["   ", "   ", "   "]
board_row_2a = ["   ", "   ", "   "]
board_row_3a = ["   ", "   ", "   "]
board_rows = [board_row_1a, board_row_2a, board_row_3a]
winner = False
turn = 0
p1 = {"Symbol": "X",
      "Score": 1,
      }

p2 = {"Symbol": "O",
      "Score": -1}

board = ["|".join(board_row_1a), board_row_1b, "|".join(board_row_2a), board_row_2b, "|".join(board_row_3a)]

for row in board:
    print(row)


def place_marker(player):
    global board
    global rows
    global columns
    row = int(input(f"What row do you want to place your {player['Symbol']}? ")) - 1
    if row < 0 or row > 2:
        print("Invalid row")
        return place_marker(player)
    else:
        column = int(input(f"What column do you want to place your {player['Symbol']}? ")) - 1
        if column < 0 or column > 2:
            print("Invalid column")
            return place_marker(player)
        else:
            if board_rows[row][column] == "   ":
                rows[row] += player["Score"]
                columns[column] += player["Score"]
                board_rows[row][column] = f" {player['Symbol']} "
                board = ["|".join(board_rows[0]), board_row_1b, "|".join(board_rows[1]), board_row_2b, "|".join(board_rows[2])]
            else:
                print("Sorry, you cannot place it there.")
                return place_marker(player)

            for entry in board:
                print(entry)
            print("")


def check_score(player):
    global columns
    global rows
    global winner
    global turn

    for row in rows:
        if row == 3*player['Score']:
            winner = player["Symbol"]
            print(f"{winner} wins!")
            return winner
    for column in columns:
        if column == 3*player['Score']:
            winner = player["Symbol"]
            print(f"{winner} wins!")
            return winner

    if board_rows[0][0] == f" {player['Symbol']} " and board_rows[1][1] == f" {player['Symbol']} " and board_rows[2][2] == f" {player['Symbol']} ":
        winner = player["Symbol"]
        print(f"{winner} wins!")
        return winner

    if board_rows[0][2] == f" {player['Symbol']} " and board_rows[1][1] == f" {player['Symbol']} " and board_rows[2][0] == f" {player['Symbol']} ":
        winner = player["Symbol"]
        print(f"{winner} wins!")
        return winner

    turn += 1
    if turn == 9:
        winner = "Draw"
        print(winner)
        return winner


while not winner:
    place_marker(p1)
    if check_score(p1):
        break
    place_marker(p2)
    check_score(p2)

