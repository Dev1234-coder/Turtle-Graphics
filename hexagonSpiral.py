import turtle
colors = ["blue", "lime", "yellow" ,"orange", "brown", "purple"]
hexagon = turtle.Pen()
turtle.bgcolor("black")
for i in range(360):
    hexagon.pencolor(colors[i%6])
    hexagon.width(i/100+1)
    hexagon.forward(i)
    hexagon.left(59)