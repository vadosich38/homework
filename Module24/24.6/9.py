board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def print_board():
    print(" {} | {} | {}".format(board[0][0], board[0][1], board[0][2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[1][0], board[1][1], board[1][2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[2][0], board[2][1], board[2][2]))


class Player:

    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


player1 = Player("Vlad", "x")
player2 = Player("Olya", "o")

print("Введите поле для хода. Например, строка 2, столбец 3: 23\n")


def step(player):
    pl_step = input("\nВаш ход: ")
    hor = int(pl_step[0]) - 1
    ver = int(pl_step[1]) - 1
    board[hor][ver] = player.sign


while True:
    print("Игрок {}, ваш ход. Вы ходите {}".format(player1.name, player1.sign))
    print_board()
    step(player1)
    if board[0][0] == board[0][1] == board[0][2] == "x" or board[1][0] == board[1][1] == board[1][2] == "x"\
            or board[2][0] == board[2][1] == board[2][2] == "x" or board[0][0] == board[1][0] == board[2][0] == "x" \
            or board[0][1] == board[1][1] == board[2][1] == "x" or board[0][2] == board[1][2] == board[2][2] == "x" \
            or board[0][0] == board[1][1] == board[2][2] == "x" or board[0][2] == board[1][1] == board[2][0] == "x":
        print("Игра окончена! Победил игрок {}".format(player1.name))
        print_board()
        break
    elif all(y != " " for i_x in board for y in i_x):
        print("Игра окончена ничьей!")
        print_board()
        break
    print("Игрок {}, ваш ход. Вы ходите {}".format(player2.name, player2.sign))
    print_board()
    step(player2)
    if board[0][0] == board[0][1] == board[0][2] == "o" or board[1][0] == board[1][1] == board[1][2] == "o" \
            or board[2][0] == board[2][1] == board[2][2] == "o" or board[0][0] == board[1][0] == board[2][0] == "o" \
            or board[0][1] == board[1][1] == board[2][1] == "o" or board[0][2] == board[1][2] == board[2][2] == "o" \
            or board[0][0] == board[1][1] == board[2][2] == "o" or board[0][2] == board[1][1] == board[2][0] == "o":
        print("Игра окончена! Победил игрок {}".format(player2.name))
        print_board()
        break
    elif all(y != " " for i_x in board for y in i_x):
        print("Игра окончена ничьей!")
        break

