import turtle
import time
import random

s = turtle.Screen()

#adjust screen color, name and size
s.title("Snake Tom")
s.setup(500,500)
s.delay(0.5) #to make the animation smoother

#adjust game field
field = turtle.Turtle()
field.ht()
field.fillcolor("aquamarine")
field.pu()
field.goto(-155,155)
field.pd()
field.begin_fill()
for i in range(4):
    field.fd(310)
    field.right(90)
field.end_fill()
field.pu()
field.goto(-160,160)
field.write("to turn RIGHT: press KEY RIGHT \nto turn LEFT: press KEY LEFT")

score = 0 #initiate score counter
#make score turtle
score_count = turtle.Turtle()
score_count.ht()
score_count.pu()
score_count.goto(40, 160)
score_count.write("Score: " + str(score))

#make snake turtle
t = turtle.Turtle()
t.shape("square") #shape of the snake
t.fillcolor("darkGreen") #color of the snake
t.pu() # pen up, not to draw anything when moving
t.ht()

#make food turtle
food = turtle.Turtle()
food.ht()
food.shape("square")
food.fillcolor("red")
food.pu()

#round the position of the snake head
def round_pos(t):
    heading = float(round(t.heading()))
    t.setheading(heading)
    x = float(round(t.xcor()))
    y = float(round(t.ycor()))
    t.goto(x, y)

#move the turtle
def move_turtle(t):
    t.forward(20)
    t.speed(0)
    round_pos(t)

#define the turns
def l():
    t.left(90)
    t.speed(0)
def r():
    t.right(90)
    t.speed(0)

s.onkey(l, "Left") #set the movement to pressing the left key
s.onkey(r, "Right") # set the movement to pressing the right key
s.listen() #make sensitive to the keys

stamps_id = [] #initiate the list of stamps IDs, for moving purposes
stamps_pos = [] #initiate the list of stamps positions, for later checking if the snake hit itself

#getting ready for the game and count down
start_commands = ["GET READY", "3...", "2...", "1...", "GO!"]
for i in start_commands:
    t.write(i)
    time.sleep(1)
    t.clear()

t.goto(-100,0)
t.st()

#make first snake of lenght of 4 squares
for i in range(3):
    stamps_id.append(t.stamp())
    stamps_pos.append(t.pos())
    move_turtle(t)

#loop for constant moving of the snake
while True:
    stamps_id.append(t.stamp()) #add stamp id to the list
    stamps_pos.append(t.pos()) #add stamp position to the list
    move_turtle(t)

    #increasing the speed if the higher score reached, by decreasing the sleep time
    if score < 3:
        time.sleep(0.3)
    elif score < 7:
        time.sleep(0.2)
    elif score < 11:
        time.sleep(0.1)
    else:
        time.sleep(0.05)

    #generation of food in a random position, if there is no food on the screen yet
    if food.isvisible() == False:
        food_x = random.randrange(-140,140,20)
        food_y = random.randrange(-140,140,20)
        food.setpos(food_x,food_y)
        food.st()

    #take the coordinates of snake(t)
    t_x = t.xcor()
    t_y = t.ycor()

    #check if the snake eat the food, and if yes, hide the food and increase the score
    if t_x == food_x and t_y == food_y:
        food.ht()
        score += 1
        score_count.clear()
        score_count.write("Score: " + str(score))
    else:
        t.clearstamp(stamps_id[0]) #delete the last stamp
        del stamps_id[0] #delete id of the last stamp from the list
        del stamps_pos[0] #delete the position of the last stamp from the list

    #check if the snake bit itself, if yes: end the game, break the loop
    if (t.pos() in stamps_pos[:-1]):
        score_count.write("You bit yourself! \nGAME OVER \nScore: " + str(score))
        break

    #check if the snake hit the wall, if yes end the game, break the loop
    if t_x <= -150 or t_x >= 150 or t_y <= -150 or t_y >= 150:
        score_count.write("You went through the wall! \nGAME OVER \nScore: " + str(score))
        break

s.mainloop()
