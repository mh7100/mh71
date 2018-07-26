def move(turtle):
    position = turtle.pos()
    if input("Left or Right? Please capitalize.") == "Left":
        turtle.goto(position[0] - 80,position[1] + 80)
    else:
        turtle.goto(position[0] + 80,position[1] + 80)
        
        
    