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
    

    def createpeices():
        import turtle
                                                #black peices
        peice1.shape("circle")
        peice1.shapesize(3,3)
        peice1.up()
        peice1.goto(-280,-280)
        name(peice1, peice1n)
        
        peice2.shape("circle")
        peice2.shapesize(3,3)
        peice2.up()
        peice2.goto(-120,-280)
        name(peice2, peice2n)
        
        peice3.shape("circle")
        peice3.shapesize(3,3)
        peice3.up()
        peice3.goto(40,-280)
        name(peice3, peice3n)
        
        peice4.shape("circle")
        peice4.shapesize(3,3)
        peice4.up()
        peice4.goto(200,-280)
        name(peice4, peice4n)
        
        peice5.shape("circle")
        peice5.shapesize(3,3)
        peice5.up()
        peice5.goto(-200,-200)
        name(peice5, peice5n)
        
        peice6.shape("circle")
        peice6.shapesize(3,3)
        peice6.up()
        peice6.goto(-40,-200)
        name(peice6, peice6n)
        
        peice7.shape("circle")
        peice7.shapesize(3,3)
        peice7.up()
        peice7.goto(120,-200)
        name(peice7, peice7n)
        
        peice8.shape("circle")
        peice8.shapesize(3,3)
        peice8.up()
        peice8.goto(280,-200)
        name(peice8, peice8n)
        
        peice9.shape("circle")
        peice9.shapesize(3,3)
        peice9.up()
        peice9.goto(-280,-120)
        name(peice9, peice9n)
    
        peice10.shape("circle")
        peice10.shapesize(3,3)
        peice10.up()
        peice10.goto(-120,-120)
        name(peice10, peice10n)
        
        peice11.shape("circle")
        peice11.shapesize(3,3)
        peice11.up()
        peice11.goto(40,-120)
        name(peice11, peice11n)
        
        peice12.shape("circle")
        peice12.shapesize(3,3)
        peice12.up()
        peice12.goto(200,-120)
        name(peice12, peice12n)
            
                                            #red peices
        peice1b.shape("circle")
        peice1b.shapesize(3,3)
        peice1b.color("red")
        peice1b.up()
        peice1b.goto(280,280)
        name(peice1b, peice1bn)
        
        peice2b.shape("circle")
        peice2b.shapesize(3,3)
        peice2b.color("red")
        peice2b.up()
        peice2b.goto(120,280)
        name(peice2b, peice2n)
        
        peice3b.shape("circle")
        peice3b.shapesize(3,3)
        peice3b.color("red")
        peice3b.up()
        peice3b.goto(-40,280)
        name(peice3b, peice3n)
        
        peice4b.shape("circle")
        peice4b.shapesize(3,3)
        peice4b.color("red")
        peice4b.up()
        peice4b.goto(-200,280)
        name(peice4b, peice4n)
        
        peice5b.shape("circle")
        peice5b.shapesize(3,3)
        peice5b.color("red")
        peice5b.up()
        peice5b.goto(200,200)
        name(peice5b, peice5n)
        
        peice6b.shape("circle")
        peice6b.shapesize(3,3)
        peice6b.color("red")
        peice6b.up()
        peice6b.goto(40,200)
        name(peice6b, peice6n)
        
        peice7b.shape("circle")
        peice7b.shapesize(3,3)
        peice7b.color("red")
        peice7b.up()
        peice7b.goto(-120,200)
        name(peice7b, peice7n)
        
        peice8b.shape("circle")
        peice8b.shapesize(3,3)
        peice8b.color("red")
        peice8b.up()
        peice8b.goto(-280,200)
        name(peice8b, peice8n)
        
        peice9b.shape("circle")
        peice9b.shapesize(3,3)
        peice9b.color("red")
        peice9b.up()
        peice9b.goto(280,120)
        name(peice9b, peice9n)
    
        peice10b.shape("circle")
        peice10b.shapesize(3,3)
        peice10b.color("red")
        peice10b.up()
        peice10b.goto(120,120)
        name(peice10b, peice10n)
        
        peice11b.shape("circle")
        peice11b.shapesize(3,3)
        peice11b.color("red")
        peice11b.up()
        peice11b.goto(-40,120)
        name(peice11b, peice11n)
    
        peice12b.shape("circle")
        peice12b.shapesize(3,3)
        peice12b.color("red")
        peice12b.up()
        peice12b.goto(-200,120)
        name(peice12b, peice12bn)
    


    def name(turtle, turtlenm):
        turtle.pencolor("white")
        turtle.write(turtlenm)
    
    
    checksetup()
    if 1 == 1:
        import turtle
        peice1 = turtle.Turtle()
        peice2 = turtle.Turtle()
        peice3 = turtle.Turtle()
        peice4 = turtle.Turtle()
        peice5 = turtle.Turtle()
        peice6 = turtle.Turtle()
        peice7 = turtle.Turtle()
        peice8 = turtle.Turtle()
        peice9 = turtle.Turtle()
        peice10 = turtle.Turtle()
        peice11 = turtle.Turtle()
        peice12 = turtle.Turtle()
            
        peice1b = turtle.Turtle()
        peice2b = turtle.Turtle()
        peice3b = turtle.Turtle()
        peice4b = turtle.Turtle()
        peice5b = turtle.Turtle()
        peice6b = turtle.Turtle()
        peice7b = turtle.Turtle()
        peice8b = turtle.Turtle()
        peice9b = turtle.Turtle()
        peice10b = turtle.Turtle()
        peice11b = turtle.Turtle()
        peice12b = turtle.Turtle()
        
        peice1n = 1
        peice2n = 2
        peice3n = 3
        peice4n = 4
        peice5n = 5
        peice6n = 6
        peice7n = 7
        peice8n = 8
        peice9n = 9
        peice10n = 10
        peice11n = 11
        peice12n = 12
        
        peice1bn = 1
        peice2bn = 2
        peice3bn = 3
        peice4bn = 4
        peice5bn = 5
        peice6bn = 6
        peice7bn = 7
        peice8bn = 8
        peice9bn = 9
        peice10bn = 10
        peice11bn = 11
        peice12bn = 12
        
    createpeices()
