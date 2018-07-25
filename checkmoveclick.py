def move(turtle):
    position = turtle.pos()
    if input("Left or Right?") == "Left":
        turtle.goto(position[0] - 80,position[1] + 80)
        
        
    