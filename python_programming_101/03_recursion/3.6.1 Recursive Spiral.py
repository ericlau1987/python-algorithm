import turtle 

def drawSpiral(t, length, color, colorBase):

    if length == 0:
        return 
    
    base = int(colorBase[1:],16)

    if newcolor < base:
        newcolor = (newcolor + base) % (2**24)

    newcolor = hex(newcolor)[2:]

    newcolor = "#" + ("0"*(6-len(newcolor))) + newcolor 

    t.color(newcolor)
    t.forward(length)
    t.left(90)
    drawSpiral(t, length-1, newcolor, colorBase)

def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(100)
    t.penup()
    t.goto(-100, -100)
    t.pendown()

    drawSpiral(t, 200, "#000000", "#ff00ff")

    screen.exitonclick()

if __name__ == "__main__":
    main()