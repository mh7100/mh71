def move(x1, y1, x2, y2):
    x1 = getcoor(x1, y1, x2, y2)[0]
    y1 = getcoor(x1, y1, x2, y2)[1]
    x2 = getcoor(x1, y1, x2, y2)[2]
    y2 = getcoor(x1, y1, x2, y2)[3]
    print(x1, y1, x2, y2)
    



def getcoor(x1, y1, x2, y2):
    canmove = 1
    endx1 = 0
    endy1 = 0
    endx2 = 0
    endy2 = 0
    
    if x1 == 1:         #Getting coordinates
        x1 = 40
        endx1 = 1
    elif x1 == 2 and endx1 == 0:
        x1 = 120
        endx1 = 1
    elif x1 == 3 and endx1 == 0:
        x1 == 200
        endx1 = 1
    elif x1 == 4 and endx1 == 0:
        x1 == 280
        endx1 = 1
    elif x1 > 4 and x1 <= 8 and type(x1) == int and endx1 == 0:
        x1 = (x1 - 4) * 80 - 40
    elif endx1 == 0:
        print ("Sorry, your first x-coordinate is invalid")
        canmove = 0
    
    if y1 == 1:         
        y1 = 280
        endy1 = 1
    elif y1 == 2 and endy1 == 0:
        y1 = 200
        endy1 = 1
    elif y1 == 3 and endy1 == 0:
        y1 = 120
        endy1 = 1
    elif y1 == 4 and endy1 == 0:
        y1 = 40
        endy1 = 1
    elif y1 > 4 and y1 <= 8 and type(y1) == int and endy1 == 0:
        y1 = (y1 - 4) * 80 - 40
    elif endy1 == 0:
        print ("Sorry, your first y-coordinate is invalid")
        canmove = 0
        
    if x2 == 1:         #Getting coordinates
        x2 = 40
        endx2 = 1
    elif x2 == 2 and endx2 == 0:
        x2 = 120
        endx2 = 1
    elif x2 == 3 and endx2 == 0:
        x2 == 200
        endx2 = 1
    elif x2 == 4 and endx2 == 0:
        x2 == 280
        endx2 = 1
    elif x2 > 4 and x2 <= 8 and type(x2) == int and endx2 == 0:
        x2 = (x2 - 4) * 80 - 40
    elif endx2 == 0:
        print ("Sorry, your second x-coordinate is invalid")
        canmove = 0
        
    if y2 == 1:         
        y2 = 280
        endy2 = 1
    elif y2 == 2 and endy2 == 0:
        y2 = 200
        endy2 = 1
    elif y2 == 3 and endy2 == 0:
        y2 = 120
        endy2 = 1
    elif y2 == 4 and endy2 == 0:
        y2 = 40
        endy2 = 1
    elif y2 > 4 and y2 <= 8 and type(y2) == int and endy2 == 0:
        y2 = (y2 - 4) * 80 - 40
    elif endy2 == 0:
        print ("Sorry, your second y-coordinate is invalid")
        canmove = 0
        
    movecoor = [x1, y1, x2, y2]
    return movecoor