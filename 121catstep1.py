#-----import statements-----
import turtle as trtl
import random as rand
#-----countdown variables-----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
timer_up = False

spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.penup()

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-200, 200)  
score_writer.hideturtle()
#-----countdown writer-----
counter = trtl.Turtle()
counter.penup()
counter.goto(200, 200)  
counter.hideturtle()

#-----game functions-----
def spot_clicked(x, y):
    global timer_up
    if not timer_up:
        update_score()
        change_position()
    else:
        spot.hideturtle()

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

#---------events---------
wn = trtl.Screen()
wn.ontimer(countdown, 1000)  
spot.onclick(spot_clicked)    
wn.mainloop()                 
