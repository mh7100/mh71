if 1 == 1:
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
            elif direction == "Right":
                turtle.goto(position[0] + 80,position[1] + 80)
            elif direction == "Backleft":
                turtle.goto(position[0] - 80,position[1] - 80)
            elif direction == "Backright":
                turtle.goto(position[0] + 80,position[1] - 80)
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
            turtlelist = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]
        else:
            turtlelist = [p1b, p2b, p3b, p4b, p5b, p6b, p7b, p8b, p9b, p10b, p11b, p12b]
        
        if turtle.pos() == turtlelist[0].pos():
            turtlelist[0].goto(500,500)
            movenoask(turtle, turtlename, direction)
        elif turtle.pos() == turtlelist[1].pos():
            turtlelist[1].goto(500,500)
            movenoask(turtle, turtlename, direction)
        elif turtle.pos() == turtlelist[2].pos():
            turtlelist[2].goto(500,500)
            movenoask(turtle, turtlename, direction)
        elif turtle.pos() == turtlelist[3].pos():
            turtlelist[3].goto(500,500)
            movenoask(turtle, turtlename, direction)
        elif turtle.pos() == turtlelist[4].pos():
            turtlelist[4].goto(500,500)
            movenoask(turtle, turtlename, direction)
        elif turtle.pos() == turtlelist[5].pos():
            turtlelist[5].goto(500,500)
            movenoask(turtle, turtlename, direction)
        elif turtle.pos() == turtlelist[6].pos(): 
            turtlelist[6].goto(500,500)
            movenoask(turtle, turtlename, direction)
        elif turtle.pos() == turtlelist[7].pos():
            turtlelist[7].goto(500,500)
            movenoask(turtle, turtlename, direction)
        elif turtle.pos() == turtlelist[8].pos(): 
            turtlelist[8].goto(500,500)
            movenoask(turtle, turtlename, direction)
        elif turtle.pos() == turtlelist[9].pos():
            turtlelist[9].goto(500,500)
            movenoask(turtle, turtlename, direction)
        elif turtle.pos() == turtlelist[10].pos():
            turtlelist[10].goto(500,500)
            movenoask(turtle, turtlename, direction)
        elif turtle.pos() == turtlelist[11].pos():
            turtlelist[11].goto(500,500)
            movenoask(turtle, turtlename, direction)
    
    
    def checksetup():
        import turtle
        wn = turtle.Screen()
        turtle.setup(640, 640)
        
        maxy = turtle.Turtle()          #Creates the horizontal lines of the checkers board
        maxy.speed(1000)
        maxy.up()
        maxy.goto(-320, -320)
        maxy.down()
        for i in range(4):
            maxy.left(90)
            maxy.forward(640)
            maxy.right(90)
            maxy.forward(80)
            maxy.right(90)
            maxy.forward(640)
            maxy.left(90)
            maxy.forward(80)
        
        maxy.up()                       #Creates the vertical lines of the checkers board
        maxy.goto(-320, 240)
        maxy.right(90)
        maxy.down()
        for i in range(4):
            maxy.left(90)
            maxy.forward(640)
            maxy.right(90)
            maxy.forward(80)
            maxy.right(90)
            maxy.forward(640)
            maxy.left(90)
            maxy.forward(80)
    

    def createpieces():
        import turtle
                                                #black ps
        p1.shape("circle")
        p1.shapesize(3,3)
        p1.up()
        p1.goto(-280,-280)
        name(p1, p1n)
        
        p2.shape("circle")
        p2.shapesize(3,3)
        p2.up()
        p2.goto(-120,-280)
        name(p2, p2n)
        
        p3.shape("circle")
        p3.shapesize(3,3)
        p3.up()
        p3.goto(40,-280)
        name(p3, p3n)
        
        p4.shape("circle")
        p4.shapesize(3,3)
        p4.up()
        p4.goto(200,-280)
        name(p4, p4n)
        
        p5.shape("circle")
        p5.shapesize(3,3)
        p5.up()
        p5.goto(-200,-200)
        name(p5, p5n)
        
        p6.shape("circle")
        p6.shapesize(3,3)
        p6.up()
        p6.goto(-40,-200)
        name(p6, p6n)
        
        p7.shape("circle")
        p7.shapesize(3,3)
        p7.up()
        p7.goto(120,-200)
        name(p7, p7n)
        
        p8.shape("circle")
        p8.shapesize(3,3)
        p8.up()
        p8.goto(280,-200)
        name(p8, p8n)
        
        p9.shape("circle")
        p9.shapesize(3,3)
        p9.up()
        p9.goto(-280,-120)
        name(p9, p9n)
    
        p10.shape("circle")
        p10.shapesize(3,3)
        p10.up()
        p10.goto(-120,-120)
        name(p10, p10n)
        
        p11.shape("circle")
        p11.shapesize(3,3)
        p11.up()
        p11.goto(40,-120)
        name(p11, p11n)
        
        p12.shape("circle")
        p12.shapesize(3,3)
        p12.up()
        p12.goto(200,-120)
        name(p12, p12n)
            
                                            #red ps
        p1b.shape("circle")
        p1b.shapesize(3,3)
        p1b.color("red")
        p1b.up()
        p1b.goto(280,280)
        name(p1b, p1bn)
        
        p2b.shape("circle")
        p2b.shapesize(3,3)
        p2b.color("red")
        p2b.up()
        p2b.goto(120,280)
        name(p2b, p2n)
        
        p3b.shape("circle")
        p3b.shapesize(3,3)
        p3b.color("red")
        p3b.up()
        p3b.goto(-40,280)
        name(p3b, p3n)
        
        p4b.shape("circle")
        p4b.shapesize(3,3)
        p4b.color("red")
        p4b.up()
        p4b.goto(-200,280)
        name(p4b, p4n)
        
        p5b.shape("circle")
        p5b.shapesize(3,3)
        p5b.color("red")
        p5b.up()
        p5b.goto(200,200)
        name(p5b, p5n)
        
        p6b.shape("circle")
        p6b.shapesize(3,3)
        p6b.color("red")
        p6b.up()
        p6b.goto(40,200)
        name(p6b, p6n)
        
        p7b.shape("circle")
        p7b.shapesize(3,3)
        p7b.color("red")
        p7b.up()
        p7b.goto(-120,200)
        name(p7b, p7n)
        
        p8b.shape("circle")
        p8b.shapesize(3,3)
        p8b.color("red")
        p8b.up()
        p8b.goto(-280,200)
        name(p8b, p8n)
        
        p9b.shape("circle")
        p9b.shapesize(3,3)
        p9b.color("red")
        p9b.up()
        p9b.goto(280,120)
        name(p9b, p9n)
    
        p10b.shape("circle")
        p10b.shapesize(3,3)
        p10b.color("red")
        p10b.up()
        p10b.goto(120,120)
        name(p10b, p10n)
        
        p11b.shape("circle")
        p11b.shapesize(3,3)
        p11b.color("red")
        p11b.up()
        p11b.goto(-40,120)
        name(p11b, p11n)
    
        p12b.shape("circle")
        p12b.shapesize(3,3)
        p12b.color("red")
        p12b.up()
        p12b.goto(-200,120)
        name(p12b, p12bn)


    def name(turtle, turtlenm):
        turtle.pencolor("white")
        turtle.write(turtlenm)
    
    
    checksetup()
    
    if 1 == 1:
        import turtle
        p1 = turtle.Turtle()
        p2 = turtle.Turtle()
        p3 = turtle.Turtle()
        p4 = turtle.Turtle()
        p5 = turtle.Turtle()
        p6 = turtle.Turtle()
        p7 = turtle.Turtle()
        p8 = turtle.Turtle()
        p9 = turtle.Turtle()
        p10 = turtle.Turtle()
        p11 = turtle.Turtle()
        p12 = turtle.Turtle()
            
        p1b = turtle.Turtle()
        p2b = turtle.Turtle()
        p3b = turtle.Turtle()
        p4b = turtle.Turtle()
        p5b = turtle.Turtle()
        p6b = turtle.Turtle()
        p7b = turtle.Turtle()
        p8b = turtle.Turtle()
        p9b = turtle.Turtle()
        p10b = turtle.Turtle()
        p11b = turtle.Turtle()
        p12b = turtle.Turtle()
        
        p1n = 1
        p2n = 2
        p3n = 3
        p4n = 4
        p5n = 5
        p6n = 6
        p7n = 7
        p8n = 8
        p9n = 9
        p10n = 10
        p11n = 11
        p12n = 12
        
        p1bn = 1
        p2bn = 2
        p3bn = 3
        p4bn = 4
        p5bn = 5
        p6bn = 6
        p7bn = 7
        p8bn = 8
        p9bn = 9
        p10bn = 10
        p11bn = 11
        p12bn = 12
        
    createpieces()
    
    print('''This is a 2-player game of checkers. Use move(peice, "peicenumber") to move a peice. Use moveking(peice, "peicenumber") to move a king.
    For example, to move black peice number 3, type "move(p3, "3"). To move RED peice number 3, type "move(p3b, "3"). To move a king, just add "king" after the move commmand like this: "moveking(p3b, "3")" 
    Remember the basic rules of checkers: you can move your pieces diagonally forward on your turn. You can jump your opponent's checkers if one is next to one of your checkers and there is a open space beyond your opponent's checker. Remember, if you can jump a checker on your turn, you must jump it.''')

