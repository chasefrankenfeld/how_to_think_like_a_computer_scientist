import turtle

wn = turtle.Screen()

wn.bgcolor('lightgreen')
wn.title('Turtle Game')

tess = turtle.Turtle()
tess.shape('turtle')
tess.color('black')
tess.pensize(3)
tess.penup()
size = 10

for i in range(12):
    tess.stamp()
    size += 3
    tess.forward(size)
    tess.right(30)

wn.mainloop()
