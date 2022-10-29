# Создайте программу для игры в ""Крестики-нолики""

def Draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def Player_input(player_symbol):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_symbol+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Вводить числа от 1 до 9.")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_symbol
                valid = True
            else:
                print("Эта клетка занята!")
        else:
            print("Вводить числа от 1 до 9.")

def Check_win(board):
    win_line = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_line:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        Draw_board(board)
        if counter % 2 == 0:
            Player_input("X")
        else:
            Player_input("O")
        counter += 1
        if counter > 4:
            tmp = Check_win(board)
            if tmp:
                print(tmp, "победил!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    Draw_board(board)

board = list(range(1, 10))
main(board)