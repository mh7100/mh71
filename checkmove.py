def move(turtle):
    position = turtle.pos()
    leftright = input("Left or Right? Please capitalize")
    
    if turtle.color()[0] == "red":
        if leftright == "Left":
            turtle.goto(position[0] + 80,position[1] - 80)
        else:
            turtle.goto(position[0] - 80,position[1] - 80)
    else:
        if leftright == "Left":
            turtle.goto(position[0] - 80,position[1] + 80)
        else:
            turtle.goto(position[0] + 80,position[1] + 80)
            
    position = turtle.pos()
            

def movenoask(turtle, leftright):
    position = turtle.pos()
    
    if turtle.color()[0] == "red":
        if leftright == "Left":
            turtle.goto(position[0] + 80,position[1] - 80)
        else:
            turtle.goto(position[0] - 80,position[1] - 80)
    else:
        if leftright == "Left":
            turtle.goto(position[0] - 80,position[1] + 80)
        else:
            turtle.goto(position[0] + 80,position[1] + 80)
            
    position = turtle.pos()

            
def checkeat(turtle, pos, direction):
    if turtle.color()[0] == "red":
        turtlelist = [peice1, peice2, peice3, peice4, peice5, peice6, peice7, peice8, peice9, peice10, peice11, peice12]
    else:
        turtlelist = [peice1b, peice2b, peice3b, peice4b, peice5b, peice6b, peice7b, peice8b, peice9b, peice10b, peice11b, peice12b]
    
    turtlelist.remove(turtle)
    
    if turtle.pos() == turtlelist[0].pos():
        turtlelist[0].goto(1000,1000)
        movenoask(turtle, direction)
    elif turtle.pos() == turtlelist[1].pos():
        turtlelist[1].goto(1000,1000)
        movenoask(turtle, direction)
    elif turtle.pos() == turtlelist[2].pos():
        turtlelist[2].goto(1000,1000)
        movenoask(turtle, direction)
    elif turtle.pos() == turtlelist[3].pos():
        turtlelist[3].goto(1000,1000)
        movenoask(turtle, direction)
    elif turtle.pos() == turtlelist[4].pos():
        turtlelist[4].goto(1000,1000)
        movenoask(turtle, direction)
    elif turtle.pos() == turtlelist[5].pos():
        turtlelist[5].goto(1000,1000)
        movenoask(turtle, direction)
    elif turtle.pos() == turtlelist[6].pos(): 
        turtlelist[6].goto(1000,1000)
        movenoask(turtle, direction)
    elif turtle.pos() == turtlelist[7].pos():
        turtlelist[7].goto(1000,1000)
        movenoask(turtle, direction)
    elif turtle.pos() == turtlelist[8].pos(): 
        turtlelist[8].goto(1000,1000)
        movenoask(turtle, direction)
    elif turtle.pos() == turtlelist[9].pos():
        turtlelist[9].goto(1000,1000)
        movenoask(turtle, direction)
    elif turtle.pos() == turtlelist[10].pos():
        turtlelist[10].goto(1000,1000)
        movenoask(turtle, direction)
    
    
