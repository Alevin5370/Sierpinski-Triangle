import turtle,random,math

x1 = 0
y1 = 0
x2 = 100
y2 = 0
x3 = 50
y3 = 86.6025
lastx = 25
lasty = 25

def setup():
    turtle.color("black")
    turtle.speed(0)
    turtle.setpos(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    turtle.goto(x3,y3)
    turtle.goto(x1,y1)
    turtle.penup()

def pick_rand_spot():
    turtle.goto(lastx,lasty)
    turtle.pendown()
    turtle.forward(.5)
    turtle.penup()

def calc_dist(x,y):
    return math.sqrt(((lastx-x)**2+(lasty-y)**2))

def draw_new_point(x,y):
    global lastx,lasty
    ang=turtle.towards(x,y)
    turtle.setheading(ang)
    dist = calc_dist(x,y)
    turtle.forward(dist/2)
    turtle.pendown()
    turtle.forward(.5)
    turtle.penup()
    lastx=turtle.xcor()
    lasty=turtle.ycor()

def recurring():
    i=0
    while(i<10000):
        vertex = random.randint(1,3)
        if (vertex==1):
            draw_new_point(x1,y1)
        elif (vertex==2):
            draw_new_point(x2,y2)
        elif (vertex==3):
            draw_new_point(x3,y3)
        i+=1
        
def main():
    turtle.hideturtle()
    setup()
    pick_rand_spot()
    recurring()
    input("Press Enter...")

if __name__ == "__main__":
    main()