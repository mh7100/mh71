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


def checksetuppt2():
    import turtle
    maxy = turtle.Turtle()
    maxy.shape("circle")            #Black checker setup
    maxy.shapesize(3,3)
    maxy.up()
    maxy.speed(1000)
    maxy.goto(-280, -280)
    
                                    
    for i in range(3):              
        maxy.stamp()
        maxy.forward(160)                   #Lines of black checkers
    maxy.stamp()
    maxy.forward(80)
    maxy.left(90)
    maxy.forward(80)
    maxy.left(90)
    
    for i in range(3):              
        maxy.stamp()
        maxy.forward(160)                   
    maxy.stamp()
    maxy.forward(80)
    maxy.right(90)
    maxy.forward(80)
    maxy.right(90)
    
    for i in range(3):              
        maxy.stamp()
        maxy.forward(160)
    maxy.stamp()
    
    
    maxy.color("red")               #Red checker setup
    maxy.goto(-280,280)
    
    for i in range(3):              
        maxy.stamp()
        maxy.forward(160)
    maxy.stamp()
    maxy.forward(80)
    maxy.right(90)
    maxy.forward(80)
    maxy.right(90)
    
    for i in range(3):              
        maxy.stamp()
        maxy.forward(160)
    maxy.stamp()
    maxy.forward(80)
    maxy.left(90)
    maxy.forward(80)
    maxy.left(90)
    
    for i in range(3):              
        maxy.stamp()
        maxy.forward(160)
    maxy.color("white")    
    maxy.goto(1000,1000)
    
        
        
        
        
    
    
    
    
    

