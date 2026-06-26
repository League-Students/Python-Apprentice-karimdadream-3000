"""
# 20_Efficient_Turtle.py

In this program, use what you've learned about functions and variables to make a program that can draw a square, pentagon, and hexagon with a single function.

- Create a function that draws a polygon based on the number of sides passed to it as an argument.
- Use variables to calculate the angle needed to turn the turtle based on the number of sides.
- Call the function multiple times with different arguments to draw a square, pentagon, and hexagon.
"""

import turtle                            # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)             # Set the size of the window

tina = turtle.Turtle()                   # Create a turtle named tina

tina.shape('turtle')                     # Set the shape of the turtle to a turtle
tina.speed(2)                            # Move at a moderate speed, not too fast.

def draw_polygon(sides):
                      # Calculate angle from number of sides
    
    for i in range(3):                 # Loop through the number of sides
                                   # Move tina forward e
                                    # Turn tina left by the left turn

draw_polygon(3, 50, "red")      # Draw a red triangle
move_tina(100, 0)               # Move to a new spot
draw_polygon(4, 60, "blue")     # Draw a blue square
move_tina(225, 0)               # Move again
draw_polygon(6, 40, "green")    # Draw a green hexagon
turtle.exitonclick()                     # Close the window when we click on it