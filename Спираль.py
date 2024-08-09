import turtle
import colorsys

def draw_spiral():

    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)  
    t.width(2)

    num_colors = 36
    num_steps = 360
    
    for i in range(num_steps):

        color = colorsys.hsv_to_rgb(i / num_steps, 1.0, 1.0)
        t.pencolor(color)
        

        t.forward(i * 3 / num_steps + i)
        t.left(59)
    

    screen.exitonclick()

if __name__ == "__main__":
    draw_spiral()
