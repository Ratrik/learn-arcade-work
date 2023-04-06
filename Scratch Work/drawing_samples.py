"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.

Multi-line comments are surrounded by three double-quote marks.
Single-line comments start with a hash/pound sign. #
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.ALICE_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.OLIVE)

# Tree trunk
# Center of 100, 320
# Width of 20
# Height of 60
arcade.draw_rectangle_filled(100, 320, 15, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_rectangle_outline(100, 320, 15, 60, arcade.csscolor.BLACK, 1)

# Tree top
arcade.draw_circle_filled(90, 340, 15, arcade.csscolor.DARK_OLIVE_GREEN)
arcade.draw_circle_filled(87, 360, 20, arcade.csscolor.DARK_OLIVE_GREEN)
arcade.draw_circle_filled(110, 340, 15, arcade.csscolor.DARK_OLIVE_GREEN)
arcade.draw_circle_filled(113, 360, 20, arcade.csscolor.DARK_OLIVE_GREEN)
arcade.draw_circle_filled(100, 380, 20, arcade.csscolor.DARK_OLIVE_GREEN)

# Another tree, with a trunk and ellipse for top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_rectangle_outline(200, 320, 20, 60, arcade.csscolor.BLACK, 1)
arcade.draw_ellipse_filled(200, 350, 50, 80, arcade.csscolor.DARK_OLIVE_GREEN)
arcade.draw_ellipse_filled(200, 370, 45, 80, arcade.csscolor.DARK_OLIVE_GREEN)
arcade.draw_ellipse_filled(200, 390, 35, 80, arcade.csscolor.DARK_OLIVE_GREEN)

# Another tree, with a trunk and arc for top
# Arc is centered at (300, 340) with a width of 60 and height of 100.
# The starting angle is 0, and ending angle is 180.
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_rectangle_outline(300, 320, 20, 60, arcade.csscolor.BLACK, 1)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_OLIVE_GREEN, 0, 180)
arcade.draw_arc_filled(270, 340, 30, 50, arcade.csscolor.DARK_OLIVE_GREEN, 0, 180)
arcade.draw_arc_filled(330, 340, 30, 50, arcade.csscolor.DARK_OLIVE_GREEN, 0, 180)

# Another tree, with a trunk and triangle for top
# Triangle is made of these three points:
# (400, 400), (370, 320), (430, 320)
arcade.draw_rectangle_filled(400, 330, 15, 80, arcade.csscolor.SADDLE_BROWN)
arcade.draw_rectangle_outline(400, 330, 15, 80, arcade.csscolor.BLACK, 1)
arcade.draw_triangle_filled(400, 420, 370, 320, 430, 320, arcade.csscolor.DARK_OLIVE_GREEN)
arcade.draw_triangle_filled(400, 430, 375, 350, 425, 350, arcade.csscolor.DARK_OLIVE_GREEN)
arcade.draw_triangle_filled(400, 440, 380, 380, 420, 380, arcade.csscolor.DARK_OLIVE_GREEN)

# Draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SADDLE_BROWN)
arcade.draw_rectangle_outline(500, 320, 20, 60, arcade.csscolor.BLACK, 1)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_OLIVE_GREEN)

# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.CORNSILK)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.CORNSILK, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.CORNSILK, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.CORNSILK, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.CORNSILK, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.CORNSILK, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.CORNSILK, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.CORNSILK, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.CORNSILK, 3)

# Draw text at (150, 230) with a font size of 24 pts.
arcade.draw_text("Arbor Day - Plant a Tree!",
                 130, 230,
                 arcade.color.BLACK, 24)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
