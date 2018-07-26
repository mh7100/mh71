def move(turtle, turtlename):
    position = turtle.pos()
    leftright = input("Left or Right? Please capitalize")
    
    if turtle.color()[1] == "red":
        turtle.clear()
        if leftright == "Left":
            turtle.goto(position[0] + 80,position[1] - 80)
        else:
            turtle.goto(position[0] - 80,position[1] - 80)
        name(turtle, turtlename)
    else:
        turtle.clear()
        if leftright == "Left":
            turtle.goto(position[0] - 80,position[1] + 80)
        else:
            turtle.goto(position[0] + 80,position[1] + 80)
        name(turtle, turtlename)
        
    position = turtle.pos()
    
    checkeat(turtle, turtlename, position, leftright)
    
    if turtle.color()[1] == "red":
        if turtle.pos()[1] == -280:
            turtle.shape("square")
    else:
        if turtle.pos()[1] == 280:
            turtle.shape("square")
            
    name(turtle, turtlename)
    
    
    
def moveking(turtle, turtlename):
    position = turtle.pos()
    direction = input("Left, Right, Backleft, or Backright? Please capitalize")
    
    if turtle.color()[1] == "red":
        turtle.clear()
        if direction == "Left":
            turtle.goto(position[0] + 80,position[1] - 80)
        elif direction == "Right":
            turtle.goto(position[0] - 80,position[1] - 80)
        elif direction == "Backleft":
            turtle.goto(position[0] + 80,position[1] + 80)
        elif direction == "Backright":
            turtle.goto(position[0] - 80,position[1] + 80)
        name(turtle, turtlename)
    else:
        turtle.clear()
        if direction == "Left":
            turtle.goto(position[0] - 80,position[1] + 80)
        else:
            turtle.goto(position[0] + 80,position[1] + 80)
        name(turtle, turtlename)
        
    position = turtle.pos()
    
    checkeat(turtle, turtlename, position, direction)
            

def movenoask(turtle, turtlename, leftright):
    position = turtle.pos()
    
    if turtle.color()[1] == "red":
        turtle.clear()
        if leftright == "Left":
            turtle.goto(position[0] + 80,position[1] - 80)
        elif leftright == "Right":
            turtle.goto(position[0] - 80,position[1] - 80)
        elif leftright == "Backleft":
            turtle.goto(position[0] + 80,position[1] + 80)
        elif leftright == "Backright":
            turtle.goto(position[0] - 80,position[1] + 80)
        name(turtle, turtlename)
    else:
        turtle.clear()
        if leftright == "Left":
            turtle.goto(position[0] - 80,position[1] + 80)
        elif leftright == "Right":
            turtle.goto(position[0] + 80,position[1] + 80)
        elif leftright == "Backleft":
            turtle.goto(position[0] - 80,position[1] - 80)
        elif leftright == "Backright":
            turtle.goto(position[0] + 80,position[1] - 80)
        name(turtle, turtlename)
    position = turtle.pos()
    
    
            
def checkeat(turtle, turtlename, pos, direction):
    if turtle.color()[1] == "red":
        turtlelist = [peice1, peice2, peice3, peice4, peice5, peice6, peice7, peice8, peice9, peice10, peice11, peice12]
    else:
        turtlelist = [peice1b, peice2b, peice3b, peice4b, peice5b, peice6b, peice7b, peice8b, peice9b, peice10b, peice11b, peice12b]
    
    if turtle.pos() == turtlelist[0].pos():
        turtlelist[0].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    elif turtle.pos() == turtlelist[1].pos():
        turtlelist[1].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    elif turtle.pos() == turtlelist[2].pos():
        turtlelist[2].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    elif turtle.pos() == turtlelist[3].pos():
        turtlelist[3].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    elif turtle.pos() == turtlelist[4].pos():
        turtlelist[4].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    elif turtle.pos() == turtlelist[5].pos():
        turtlelist[5].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    elif turtle.pos() == turtlelist[6].pos(): 
        turtlelist[6].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    elif turtle.pos() == turtlelist[7].pos():
        turtlelist[7].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    elif turtle.pos() == turtlelist[8].pos(): 
        turtlelist[8].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    elif turtle.pos() == turtlelist[9].pos():
        turtlelist[9].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    elif turtle.pos() == turtlelist[10].pos():
        turtlelist[10].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    elif turtle.pos() == turtlelist[11].pos():
        turtlelist[11].goto(1000,1000)
        movenoask(turtle, turtlename, direction)
    
    
