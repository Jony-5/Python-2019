import turtle

def base(t):
	t.speed(0)
	t.penup()
	t.setpos(0,-250)
	t.color("#ffe0bd")
	t.begin_fill()
	t.pendown()
	t.forward(200)
	t.left(90)
	t.forward(350)
	t.left(90)
	t.forward(400)
	t.left(90)
	t.forward(350)
	t.left(90)
	t.forward(200)
	t.penup()
	t.end_fill()

def roof(t):
	t.speed(0)
	t.color("#FF0000")
	t.begin_fill()
	t.setpos(0,100)
	t.pendown()
	t.forward(225)
	t.left(90)
	t.circle(225,180)
	t.left(90)
	t.forward(225)
	t.end_fill()

def dots(t):
	t.speed(0)
	t.color("#FFFFFF")
	t.begin_fill()
	t.penup()
	t.forward(50)
	t.pendown()
	t.left(90)
	t.circle(25,180)
	t.end_fill()
	t.right(90)
	t.penup()
	t.forward(50)
	t.pendown()
	t.right(90)
	t.begin_fill()
	t.circle(50,180)
	t.left(90)
	t.penup()
	t.forward(300)
	t.end_fill()
	t.pendown()
	t.left(90)
	t.begin_fill()
	t.circle(30,180)
	t.end_fill()
	t.penup()
	t.right(180)
	t.forward(90)
	t.pendown()
	t.begin_fill()
	t.circle(40,360)
	t.end_fill()
	t.penup()
	t.left(90)
	t.forward(225)
	t.right(90)
	t.right(90)
	t.begin_fill()
	t.circle(25,360)
	t.end_fill()
	t.penup()
	t.right(90)
	t.forward(15)
	t.left(90)
	t.forward(85)
	t.begin_fill()
	t.circle(60,360)
	t.end_fill()


def door(t):
	t.hideturtle()
	t.speed(3)
	t.setpos(0,-250)
	t.color("#785027")
	t.begin_fill()
	t.penup()
	t.forward(125)
	t.left(90)
	t.forward(250)
	t.left(90)
	t.forward(150)
	t.left(90)
	t.forward(250)
	t.end_fill()
	t.left(90)
	t.forward(73)
	t.left(90)
	t.color("#000000")
	t.begin_fill()
	t.forward(250)
	t.right(90)
	t.forward(5)
	t.right(90)
	t.forward(250)
	t.end_fill()
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(167)
	t.color("#c4c730")
	t.begin_fill()
	t.circle(-10,360)
	t.penup()
	t.left(90)
	t.forward(25)
	t.right(90)
	t.circle(10,360)
	t.end_fill()




def main():
	t=turtle.Turtle()
	w=turtle.Screen()
	base(t)
	roof(t)
	dots(t)
	door(t)
	w.exitonclick()

if __name__ == '__main__':
	main()
