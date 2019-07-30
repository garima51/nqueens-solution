#to check if value of i is possible or not
def valid_move(chess, col, row):
#     print("Validating with {} col = {} size = {}".format(chess,col,row)

    c = 1
    for i in range(col-1, -1, -1):
        if chess[i] == row:
        #Rooks move to check previous column
            return False
        #above Knights move to check previous columns upper diagnol values
        if chess[i] == row - c:
            return False
            #below Knights move to check previous columns lower diagnol values

        if chess[i] == row + c:
            return False
        c += 1
    return True


def solve(chess, col, size):
    #print("Starting with {} col = {} size = {}".format(chess,col,size)
    #exit condition
    if col == size:
        return True
    for i in range(size):
        if valid_move(chess, col, i):
        #try values from 0 to size
            chess[col] = i
        #recursive call for next column
            if solve(chess, col+1, size):
                return True
           #If No solution
    chess[col] = None
    return False

def solve_nqueen(size):
    chess=[None]*size
    if solve(chess, 0, size):
            #printing format
        print("solved")
        print(chess)
        a=[["." for i in range (size)] for j in range(size)]
        for i in range(size):
            a[chess[i]][i] = 'Q'
        for i in range(size):
            print(a[i])
        return True
    else:
        print("no solution")
    return False

if __name__=='__main__':
    #assert solve_nqueen(3) == False
    #assert solve_nqueen(4) == True

    #chess = [None]*4
    #solve(chess, 0, 4)
    #assert chess == [1,3,0,2]
    size=int(input("please input size of chess"))
    solve_nqueen(size)
