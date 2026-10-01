from PIL import Image, ImageDraw

def createImage():
    image = Image.new('RGB', (320, 320), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    #shape = ([6,4],[10,8],[14,4],[18,8],[22,4],[26,8],[30,4],[30,28],[6,28],[6,4])
    #xy = ((40*i)-20, (40*j)-20), ((40*i)+20, (40*j)+20)
    for i in range(8):
        for j in range(8):
            if i%2 == 1 and j%2 == 0:
                color = "black"
            elif i%2 == 0 and j%2 == 1:
                color = "black"
            else:
                color = "white"
            draw.rectangle([i*40,j*40,(i+1)*40,(j+1)*40],color)
            if board[i][j]==1:
                draw.rectangle(((40*i+10, (40*j+10)), (40*i+30), 40*j+30),fill="brown")
    image.save('queens_solution.png')

board = []
counter = 1
def create_chessBoard():
    global board
    for i in range(8):
        row = [0] * 8
        board.append(row)

def checkIt(x,y):
    for i in range(8):
        #check row
        if board[y][i] ==1:
            return False

        #check col
        if board[i][x] ==1:
            return False

    for i in range(0,8):
        for j in range(0,8):
            if i+j == x+y:
                if board[i][j]==1:
                    return False
            if i-j == y-x:
                if board[i][j]==1:
                    return False
    return True

#def place_queen(x,y,queen):
 #   global board
  #  if checkIt(x,y):
   #     board[y][x] = queen

def queen(n):
    global board,counter
    if n ==8:
        counter+=1
        createImage()
        print(board)
        print('-----------------------')
    else:
        for i in range(8):
            if checkIt(i,n):
                board[n][i] = 1
                queen(n+1)
                board[n][i] = 0


create_chessBoard()
queen(0)
