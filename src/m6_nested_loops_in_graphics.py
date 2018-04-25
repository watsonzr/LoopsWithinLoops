"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Zack Watson.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate them. """
    run_test_draw_L()
    run_test_draw_wall_on_right()


def run_test_draw_L():
    """
    Demonstrates nested loops in a TWO-DIMENSIONAL GRAPHICS example.
    """
    width = 800
    height = 600
    title = 'Draw an L of circles.  Two tests'
    window = rg.RoseWindow(width, height, title)

    window.continue_on_mouse_click('Click to run Test 1.')

    # ------------------------------------------------------------------
    starting_point = rg.Point(50, 50)
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # First L.
    # ------------------------------------------------------------------
    radius = 10
    starting_circle = rg.Circle(starting_point, radius)
    green_circle = starting_circle.clone()
    green_circle.fill_color = 'green'

    draw_L(window, green_circle, 10, 5)
    window.continue_on_mouse_click('Click twice to run Test 2.')

    # ------------------------------------------------------------------
    # Second L.
    # ------------------------------------------------------------------
    starting_circle.move_by(250, 100)
    blue_circle = starting_circle.clone()
    blue_circle.fill_color = 'blue'

    window.continue_on_mouse_click('Click to run Test 2.')
    draw_L(window, blue_circle, 6, 15)

    window.close_on_mouse_click()


def draw_L(window, circle, r, c):
    """
    See   L.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an 'L' of circles on the given rg.RoseWindow.
      The 'column' part of the L should have r rows and 3 columns.
        (That is, it is r 'tall' and 3 'thick'.)
      The 'shared corner' part of the L should be 3 x 3.
      The 'row' part of the L should have c columns and 3 rows.
        (That is, it is c 'long' and 3 'thick'.)

      The given rg.Circle specifies:
      - The position of the upper-left circle drawn and also
      - The radius that all the circles have.
      - The fill_color that all the circles have.
    After drawing each circle, pauses briefly (0.1 second).

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type r: int
      :type c: int
    and m and n are small, positive integers.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------

    origin_color = circle.fill_color
    new_x = circle.center.x
    new_y = circle.center.y
    for i in range(r + 3):
        circle = rg.Circle(rg.Point(new_x, new_y), circle.radius)
        circle.fill_color = origin_color
        circle.attach_to(window)
        window.render(0.1)
        for j in range(2):
            new_x = new_x + 2 * circle.radius
            circle = rg.Circle(rg.Point(new_x, new_y), circle.radius)
            circle.fill_color = origin_color
            circle.attach_to(window)
            window.render(0.1)
        new_x = new_x - 4 * circle.radius
        new_y = new_y + 2 * circle.radius
    new_x = new_x + 6 * circle.radius
    new_y = new_y - 2 * circle.radius
    for i in range(c):
        circle = rg.Circle(rg.Point(new_x, new_y), circle.radius)
        circle.fill_color = origin_color
        circle.attach_to(window)
        window.render(0.1)
        for j in range(2):
            new_y = new_y - 2 * circle.radius
            circle = rg.Circle(rg.Point(new_x, new_y), circle.radius)
            circle.fill_color = origin_color
            circle.attach_to(window)
            window.render(0.1)
        new_x = new_x + 2 * circle.radius
        new_y = new_y + 4 * circle.radius


def run_test_draw_wall_on_right():
    """ Tests the    draw_wall_on_right    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Wall on the right, Tests 1 and 2')

    window.continue_on_mouse_click('Click to run Test 1.')

    rectangle1 = rg.Rectangle(rg.Point(250, 30), rg.Point(250 + 30, 30 + 20))
    draw_wall_on_right(rectangle1, 8, window)

    window.continue_on_mouse_click('Click to run Test 2.')
    rectangle2 = rg.Rectangle(rg.Point(470, 40), rg.Point(470 + 50, 40 + 50))
    draw_wall_on_right(rectangle2, 4, window)

    window.close_on_mouse_click()


def draw_wall_on_right(rectangle, n, window):
    """
    See   Walls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an n x n RIGHT-justified triangle of rectangles
    (1 rectangle in the top row, 2 in the next row, etc., until n rows)
    on the given rg.RoseWindow.  The given rg.Rectangle specifies:
      - The position of the upper-right rectangle drawn and also
      - The width and height that all the rectangles have.
    After drawing each rectangle, pauses briefly (0.1 second).

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is a small, positive integer.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------

    corner1 = rectangle.corner_1
    corner2 = rectangle.corner_2
    baseline_c1 = rectangle.corner_1.x
    baseline_c2 = rectangle.corner_2.x
    width = rectangle.get_width()
    height = rectangle.get_height()
    for i in range(n):
        rectangle = rg.Rectangle(corner1, corner2)
        rectangle.attach_to(window)
        window.render(0.1)
        for j in range(i):
            corner1.x = corner1.x - width
            corner2.x = corner2.x - width
            rectangle = rg.Rectangle(corner1, corner2)
            rectangle.attach_to(window)
            window.render(0.1)
        corner1.x = baseline_c1
        corner2.x = baseline_c2
        corner1.y = corner1.y + height
        corner2.y = corner2.y + height


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
