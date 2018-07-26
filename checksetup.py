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
                                            #black p
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
        
                                        #red p
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
    











       
        
        



