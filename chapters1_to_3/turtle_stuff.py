import turtle

wn = turtle.Screen()

wn.bgcolor('lightgreen')
wn.title('Turtle Game')

ben = turtle.Turtle()
ben.pencolor("purple")
ben.shape("turtle")
ben.color('blue')
ben.pensize(3)

ben.penup()
ben.stamp()

for i in range(12):
    ben.forward(160)
    ben.pendown()
    ben.forward(10)
    ben.penup()
    ben.forward(30)
    ben.stamp()
    ben.backward(200)
    ben.right(30)



wn.mainloop()