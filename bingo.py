import Needs as ne
import random
import time

# global variables
board_len = 5
game_completed = False
current_player = "player1"

num_li = [i for i in range(1, 26)]
# fills the board with random numbers btw(1-25)
board = [[num_li.pop(random.randrange(0, len(num_li))) for i in range(board_len)] for _ in range(board_len)]
num_li = [i for i in range(1, 26)]
hidden_board = [[num_li.pop(random.randrange(0, len(num_li))) for i in range(board_len)] for _ in range(board_len)]
ne.print_board(board)
num_li = [i for i in range(1, 26)]
while not game_completed:
    in_val = 0
    if current_player == "player1":
        current_player = "sys"
        print("its your turn ! !")
        in_val = int(input("enter a value :"))
        num_li.remove(in_val)
    elif current_player == "sys":
        current_player = "player1"
        print("its other players turn")
        in_val = num_li[random.randrange(0, len(num_li))]
        num_li.remove(in_val)
        time.sleep(1.2)
        print("He chosen : ", in_val)

    print(in_val, "is removed in both tables")
    ne.remove_val(in_val, board)
    ne.remove_val(in_val, hidden_board)
    time.sleep(1.5)
    ne.print_board(board)

    P1 = ne.check_win(board) >= 5
    P2 = ne.check_win(hidden_board) >= 5

    if P1 and P2:
        print("BinGoo :(")
        time.sleep(1.4)
        print("The match got draw")
        game_completed = True
    elif P1:
        print("Binggo ;) ")
        time.sleep(1.4)
        print("you won the match")
        game_completed = True
    elif P2:
        print("you lost the match ")
        time.sleep(1.2)
        print("Other player won the match")
        game_completed = True
