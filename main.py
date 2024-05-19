from graphics import *

def main():
    win = Window(800, 600)
    p1 = Point(100, 100)
    p2 = Point(700, 500)
    line = Line(p1, p2)
    win.draw_line(line, "black")
    p1 = Point(700, 100)
    p2 = Point(100, 500)
    line = Line(p1, p2)
    win.draw_line(line, "blue")
    win.wait_for_close()


main()