import random
def display_board(board):
    print("\n")
    print("      |      |")
    print(''+  board[7]    + "      |" + board[8] + '      |' + board[9])
    print("      |      |")
    print("  -----------------")
    print("      |      |")
    print(''+ board[4]+ "      |" + board[5] + '      |' + board[6])
    print("      |      |")
    print("  ------------------")
    print("      |      |")
    print(''+ board[1]+ "      |" + board[2] + '      |' + board[3])
    print("      |      |")


def player_input(a,b):
    n=""
    if n!="X" or n!="O":
        while n!="X" and n!="O":
            n=input(a +" choose the marker X or O ").upper()
    if n=="X":
        return "X","O"
    else:
        return "O","X"


def placemarker(board,marker,position):
    if board[position]=="":
        board[position]=marker
    else:
        print()
        print("oops!! Place Occupied You Lost Your Chance  ")



def wincheck(b,m):
    if (b[1]==m and b[2]==m and b[3]==m) or (b[4]==m and b[5]==m and b[6]==m) or (b[7]==m and b[8]==m and b[9]==m) or (b[4]==m and b[7]==m and b[1]==m)or (b[9]==m and b[6]==m and b[3]==m) or (b[5]==m and b[8]==m and b[2]==m) or (b[7]==m and b[5]==m and b[3]==m) or (b[9]==m and b[5]==m and b[1]==m):
        return True
    else:
        return False



def spacecheck(b,pos):
    return b[pos]==""


def fullboardcheck(b):
    for i in range(1,10):
        if  spacecheck(b,i):
            return False
    return True



def playerchoice(b):
    pos=0
    print()
    while pos not in [1,2,3,4,5,6,7,8,9] and spacecheck(b,pos):
        pos=int(input("enter the position from 1-9 "))
    return pos


def choosefirst(a,b):
    flip=random.randint(0,1)
    if flip==0:
        return a
    else:
        return b

    
def replay():
    c=input("want to play again? yes or no")
    return c=="yes"


print("WELCOME TO TIC TAC TOE")
print()
a=input("PLAYER ONE ENTER YOUR NAME :  ")
print()
b=input("PLAYER TWO ENTER YOUR NAME :  ")
print()
while True:
    boards=[""]*10
    player1_marker,player2_marker=player_input(a,b)
    turn=choosefirst(a,b)
    print()
    print(turn+" will start the game ")
    print()
    play_game=input("Ready to Play? Y or N ")
    if play_game=="Y":
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn== a:
            display_board(boards)
            pos=playerchoice(boards)
            placemarker(boards,player1_marker,pos)
            if wincheck(boards,player1_marker):
                display_board(boards)
                print(a.upper()+" IS THE WINNER")
                print()
                game_on=False
            else:
                if fullboardcheck(boards):
                    display_board(boards)
                    print("TIE MATCH")
                    print()
                    game_on=False
                else:
                    turn=b
        else:
            display_board(boards)
            pos=playerchoice(boards)
            placemarker(boards,player2_marker,pos)
            if wincheck(boards,player2_marker):
                display_board(boards)
                print()
                print(b.upper()+" IS THE WINNER")
                print()
                game_on=False
            else:
                if fullboardcheck(boards):
                    display_board(boards)
                    print()
                    print("TIE MATCH")
                    print()
                    game_on=False
                else:
                    turn=a
    if not replay():
        break
