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
    
    peice2.shape("circle")
    peice2.shapesize(3,3)
    peice2.up()
    peice2.goto(-120,-280)
    
    peice3.shape("circle")
    peice3.shapesize(3,3)
    peice3.up()
    peice3.goto(40,-280)
    
    peice4.shape("circle")
    peice4.shapesize(3,3)
    peice4.up()
    peice4.goto(200,-280)
    
    peice5.shape("circle")
    peice5.shapesize(3,3)
    peice5.up()
    peice5.goto(-200,-200)
    
    peice6.shape("circle")
    peice6.shapesize(3,3)
    peice6.up()
    peice6.goto(-40,-200)
    
    peice7.shape("circle")
    peice7.shapesize(3,3)
    peice7.up()
    peice7.goto(120,-200)
    
    peice8.shape("circle")
    peice8.shapesize(3,3)
    peice8.up()
    peice8.goto(280,-200)
    
    peice9.shape("circle")
    peice9.shapesize(3,3)
    peice9.up()
    peice9.goto(-280,-120)

    peice10.shape("circle")
    peice10.shapesize(3,3)
    peice10.up()
    peice10.goto(-120,-120)
    
    peice11.shape("circle")
    peice11.shapesize(3,3)
    peice11.up()
    peice11.goto(40,-120)
    
    peice12.shape("circle")
    peice12.shapesize(3,3)
    peice12.up()
    peice12.goto(200,-120)
        
                                        #red peices
    peice1b.shape("circle")
    peice1b.shapesize(3,3)
    peice1b.color("red")
    peice1b.up()
    peice1b.goto(280,280)
    
    peice2b.shape("circle")
    peice2b.shapesize(3,3)
    peice2b.color("red")
    peice2b.up()
    peice2b.goto(120,280)
    
    peice3b.shape("circle")
    peice3b.shapesize(3,3)
    peice3b.color("red")
    peice3b.up()
    peice3b.goto(-40,280)
    
    peice4b.shape("circle")
    peice4b.shapesize(3,3)
    peice4b.color("red")
    peice4b.up()
    peice4b.goto(-200,280)
    
    peice5b.shape("circle")
    peice5b.shapesize(3,3)
    peice5b.color("red")
    peice5b.up()
    peice5b.goto(200,200)
    
    peice6b.shape("circle")
    peice6b.shapesize(3,3)
    peice6b.color("red")
    peice6b.up()
    peice6b.goto(40,200)
    
    peice7b.shape("circle")
    peice7b.shapesize(3,3)
    peice7b.color("red")
    peice7b.up()
    peice7b.goto(-120,200)
    
    peice8b.shape("circle")
    peice8b.shapesize(3,3)
    peice8b.color("red")
    peice8b.up()
    peice8b.goto(-280,200)
    
    peice9b.shape("circle")
    peice9b.shapesize(3,3)
    peice9b.color("red")
    peice9b.up()
    peice9b.goto(280,120)

    peice10b.shape("circle")
    peice10b.shapesize(3,3)
    peice10b.color("red")
    peice10b.up()
    peice10b.goto(120,120)
    
    peice11b.shape("circle")
    peice11b.shapesize(3,3)
    peice11b.color("red")
    peice11b.up()
    peice11b.goto(-40,120)

    peice12b.shape("circle")
    peice12b.shapesize(3,3)
    peice12b.color("red")
    peice12b.up()
    peice12b.goto(-200,120)
    










if 1 == 1:
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
        
        
        



