import turtle
def sq(some) :
        for i in range (1 , 5) :
                some.forward(100)
                some.right(120)
def art() :
        window=turtle.Screen()
        window.bgcolor("black")
        a=turtle.Turtle()
        a.shape("turtle")
        a.color("yellow")
        a.speed(0)
        for i in range (1,73) :
                sq(a)
                a.right(5)
        window.exitonclick()
art()

