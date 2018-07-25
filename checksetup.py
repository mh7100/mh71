def checksetup():
    import turtle
    wn = turtle.Screen()
    turtle.setup(640, 640)
    
    maxy = turtle.Turtle()          #Creates horizontal lines
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
    
    maxy.up()                       #Creates vertical lines
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


