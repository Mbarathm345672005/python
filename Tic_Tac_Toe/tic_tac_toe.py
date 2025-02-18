import numpy

board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'

def place(sym):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter the row 1 2 or 3:"))
        col=int(input("Enter the column 1 2 or 3:"))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-'):
            break
        else:
            print("Enter the valid cell")
    board[row-1][col-1]=sym

def won(sym):
    if check_row(sym) or check_col(sym) or check_dia(sym):
        print(sym ,"won")
        return True
    else:
        return False

def check_row(sym):
    for i in range(3):
        count=0
        for j in range(3):
            if board[i][j]==sym:
                count+=1
        if(count==3):
            return True
    else:
        return False

def check_col(sym):
    for j in range(3):
        count=0
        for i in range(3):
            if board[i][j]==sym:
                count+=1
        if(count==3):
            return True
    else:
        return False
def check_dia(sym):
    if (board[0][0]==sym and board[1][1]==sym and board[2][2]==sym):
        return True
    if (board[0][2]==sym and board[1][1]==sym and board[2][0]==sym):
        return True
    else:
        return False
    
def play():
    for turn in range(9):
        if(turn%2==0):
            print("p1 turn")
            place(p1s)
            if won(p1s):
                break
        else:
            print("p2 turn")
            place(p2s)
            if (won(p2s)):
                print(numpy.matrix(board))
                break
    if (not won(p1s) and not won(p2s)):
        print ("draw")

play()
