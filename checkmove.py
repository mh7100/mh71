def move(turtle):
    position = turtle.pos()
    if turtle.color()[0] == "red":
        if input("Left or Right? Please capitalize.") == "Left":
            turtle.goto(position[0] + 80,position[1] - 80)
        else:
            turtle.goto(position[0] - 80,position[1] - 80)
    else:
        if input("Left or Right? Please capitalize.") == "Left":
            turtle.goto(position[0] - 80,position[1] + 80)
        else:
            turtle.goto(position[0] + 80,position[1] + 80)
            
    position = turtle.pos()
            
            
            
            
def checkeat(turtle, pos):
    if turtle.color()[0] == "red":
        turtlelist = [peice1, peice2, peice3, peice4, peice5, peice6, peice7, peice8, peice9, peice10, peice11, peice12]
    else:
        turtlelist = [peice1b, peice2b, peice3b, peice4b, peice5b, peice6b, peice7b, peice8b, peice9b, peice10b, peice11b, peice12b]
    
    turtlelist.remove(turtle)
    
    if turtle.pos() == turtlelist[0].pos() or turtle.pos() == turtlelist[1].pos() or turtle.pos() == turtlelist[2].pos() or turtle.pos() == turtlelist[3].pos() or turtle.pos() == turtlelist[4].pos() or turtle.pos() == turtlelist[5].pos() or turtle.pos() == turtlelist[6].pos() or turtle.pos() == turtlelist[7].pos() or turtle.pos() == turtlelist[8].pos() or turtle.pos() == turtlelist[9].pos() or turtle.pos() == turtlelist[10].pos():
        print("hi")
        
        
    
    
