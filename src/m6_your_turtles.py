"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Eri Miyaoka.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red',10)
red_turtle.speed = 20

for k in range(8):
    red_turtle.draw_square(100)
    red_turtle.pen_up()
    red_turtle.draw_square(10)
    red_turtle.right(45)
    red_turtle.forward(100)
    red_turtle.left(90)
    red_turtle.pen_down()

kamejiro_turtle = rg.SimpleTurtle('square')
kamejiro_turtle.pen = rg.Pen('green',1)
kamejiro_turtle.speed = 30

for k in range(15):
    kamejiro_turtle.left(100)
    kamejiro_turtle.forward(200)

for l in range(5):
    red_turtle.right(10)
    red_turtle.forward(100)

window.close_on_mouse_click()

