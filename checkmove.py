def move(x1, y1, x2, y2):
    print("Not done yet!")



def getcoor(x1, y1, x2, y2):
    canmove = 1
    if x1 == 1:         #Getting coordinates
        x1 = 40
    elif x1 == 2:
        x1 = 120
    elif x1 == 3:
        x1 == 200
    elif x1 == 4:
        x1 == 280
        
    elif x1 > 4 and x1 <= 8 and type(x1) == int:
        x1 = (x1 - 4) * 80 - 40
    else:
        print ("Sorry, your first x-coordinate is invalid")
        canmove = 0
    
    
    if y1 == 1:         
        y1 = 280
    elif y1 == 2:
        y1 = 200
    elif y1 == 3:
        y1 = 120
    elif y1 == 4:
        y1 = 40
        
    elif y1 > 4 and y1 <= 8 and type(y1) == int:
        y1 = (y1 - 4) * 80 - 40
    else:
        print ("Sorry, your first y-coordinate is invalid")
        canmove = 0
        
    if x2 == 1:         #Getting coordinates
        x2 = 40
    elif x2 == 2:
        x2 = 120
    elif x2 == 3:
        x2 == 200
    elif x2 == 4:
        x2 == 280
        
    elif x2 > 4 and x2 <= 8 and type(x2) == int:
        x2 = (x2 - 4) * 80 - 40
    else:
        print ("Sorry, your second x-coordinate is invalid")
        canmove = 0
        
    if y2 == 1:         
        y2 = 280
    elif y2 == 2:
        y2 = 200
    elif y2 == 3:
        y2 = 120
    elif y2 == 4:
        y2 = 40
        
    elif y2 > 4 and y2 <= 8 and type(y2) == int:
        y2 = (y2 - 4) * 80 - 40
    else:
        print ("Sorry, your second y-coordinate is invalid")
        canmove = 0
        
    return[x1, y1, x2, y2]