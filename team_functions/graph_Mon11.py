"""
Mon-11 Team Function: Create a graphical representation of the flights on a day
"""

from individual_functions.layover import layover
from individual_functions.oversold import  oversold
from individual_functions.daily_data import daily_data
from fleet_data import fleet_data
from team_functions.passenger_data import passenger_data
from individual_functions.overweight import overweight
import turtle

def graph_mon_11(oversold, overweight, layover):
    """
    Accepts 2-D lists oversold, overweight, layover and time delay. Displays flight and passenger
    information organized by flight model.
    """
    # Initialize turtle
    turtle.setup(1000, 450)
    t = turtle.Turtle()
    screen = turtle.Screen()
    # instant render
    screen.tracer(0)
    # starting offset for pattern
    x = -450
    t.pu()

    # Since all data lists have the [0] item as the model
    # Use the first item list (oversold business) to index the models
    for oversold_business in oversold[0]:
        # For each model draw a box
        t.goto(x,60)
        t.color("lightpink")
        t.begin_fill()
        t.pd()

        # Draw background square
        for i in range (4):
            t.forward(120)
            t.right(90)
        t.end_fill()

        # DRAW HEADER RECTANGLE
        t.color("lightblue")
        t.pu()
        t.goto(x, 60)
        t.begin_fill()
        # 121 instead of 120 to combat pixel errors (turtle problem)
        t.forward(121)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward(121)
        t.right(90)
        t.forward(25)
        t.right(90)
        t.end_fill()
        # Rectangle DONE

        # Start printing data into box
        t.color("black")
        t.goto(x+60,40)
        # Writes flight model in header
        t.write(oversold_business[0], align = 'center')


        t.goto(x+60,20)
        # oversold business seats
        t.write(f"Oversold business:{oversold_business[1]}", align = 'center')

        # Start adding the rest of the data
        # Add oversold eco
        current_model = oversold_business[0]
        for oversold_economy in oversold[1]:
            # Find the data corresponding to the current model
            if oversold_economy[0] == oversold_business[0]:
                # write the data into the box
                t.goto(x+60,0)
                t.write(f"Oversold economy:{oversold_economy[1]}", align = 'center') # oversold economy seats

        # Find the overweight data for the current plane
        for overweight_list in overweight[0]: # plane overweight list
            # Find current model
            if overweight_list[0] == current_model:
                # write the data into the box
                t.goto(x+60,-20)
                t.write(f"Overweight bags:{overweight_list[1]}", align = 'center') 
        # Find the layover data for the current plane
        for layover_list in layover[1]: # plane layover list
            if layover_list[0] == current_model:
                # write the data into the box
                t.goto(x+60,-40)
                t.write(f"Late Layover:{layover_list[1]}", align = 'center') # amount of passengers that have late layover
        # Increase the accumulator to draw next rectangle moved to the right
        x += 130

    t.hideturtle()
    # Render the drawing
    screen.update()
    screen.exitonclick()
    turtle.done()

if __name__ == "__main__":
    dd = daily_data(passenger_data())
    oversold = oversold(fleet_data(), dd)
    overweight_d = overweight(fleet_data(), passenger_data())
    layover_d = layover(fleet_data(), passenger_data())
    graph_mon_11(oversold, overweight_d, layover_d)