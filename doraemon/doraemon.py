from turtle import*
import turtle
wn = turtle.Screen()
wn.setup(width=1000, height=800)
def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()

def nose():
    my_goto(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()
    
def beard():
    my_goto(-32, 135)
    seth(165)
    fd(60)

    my_goto(-32, 125)
    seth(180)
    fd(60)

    my_goto(-32, 115)
    seth(193)
    fd(60)

    my_goto(37, 135)
    seth(15)
    fd(60)

    my_goto(37, 125)
    seth(0)
    fd(60)

    my_goto(37, 115)
    seth(-13)
    fd(60)

def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()

if __name__ == '__main__':
    head()
    beard()
    nose()
    my_goto(100, -300)
    write('Vo Ngoc Minh Tri', font=("Bradley Hand ITC", 30, "bold"))
        mainloop()