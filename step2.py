import turtle as trtl
import random as rand

spot_color = "black"
spot_shape = "circle"
font_setup = ("Arial", 20, "normal")
score = 0
timer = 30
timer_up = False
colors = ["red", "blue", "green", "yellow", "purple"]
sizes = [2, 1.5, 1, 0.5]

spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(sizes[0])
spot.fillcolor(spot_color)
spot.penup()

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-200, 200)
score_writer.hideturtle()

counter = trtl.Turtle()
counter.penup()
counter.goto(200, 200)
counter.hideturtle()

wn = trtl.Screen()
wn.bgcolor("white")

def spot_clicked(x, y):
    global timer_up
    if not timer_up:
        add_stamp()
        change_size()
        update_score()
        change_position()
    else:
        spot.hideturtle()

def add_stamp():
    color_choice = rand.choice(colors)
    spot.fillcolor(color_choice)
    spot.stamp()
    spot.fillcolor(spot_color)

def change_size():
    new_size = rand.choice(sizes)
    spot.shapesize(new_size)

def change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.goto(new_xpos, new_ypos)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write(f"Timer: {timer}", font=font_setup)
        timer -= 1
        wn.ontimer(countdown, 1000)

def start_game():
    wn.ontimer(countdown, 1000)
    spot.onclick(spot_clicked)
    wn.mainloop()

start_game()
