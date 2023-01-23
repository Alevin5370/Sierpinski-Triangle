import turtle,random,math

#x1-x3 and y1-y3 are the vertices of the triangle
#lastx and lasty start as a spot I picked within the triangle 
#25 is an abritrary number I picked
#as long as the coordinates are within the triangle this will work 
x1 = 0
y1 = 0
x2 = 100
y2 = 0
x3 = 50
y3 = 86.6025
lastx = 25
lasty = 25

#General setup of the pen such as speed and color
#setup also draws the outline of the triangle 
def setup():
    turtle.color("black")
    turtle.speed(0)
    turtle.setpos(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    turtle.goto(x3,y3)
    turtle.goto(x1,y1)
    turtle.penup()

#draws the first point in the triangle
def pick_rand_spot():
    turtle.goto(lastx,lasty)
    turtle.pendown()
    turtle.forward(.5)
    turtle.penup()

#helper function to give the distance from the last point to the vertex 
def calc_dist(x,y):
    return math.sqrt(((lastx-x)**2+(lasty-y)**2))

#this function does most of the work
#it starts by turning the turtle towards the random vertex
#it then grabs the distance from the helper function and moves forward half of that distance
#then it draws the dot and updates the cordinates of the last drawn point
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

#this function contains the loop to draw 10,000 dots
#within the loop it starts by choosing a random vertex
#it then calls the draw_new_point function
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