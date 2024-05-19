from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    
    cells = [Cell(100, 200, 100, 200, win),
             Cell(200, 300, 200, 300, win),
             Cell(300, 400, 300, 400, win),
             Cell(400, 500, 400, 500, win)]

    for i in range(len(cells)):
        if i % 2 == 0:
            cells[i].has_bottom_wall = False
        else:
            cells[i].has_left_wall = False
        cells[i].draw_cell()

    win.wait_for_close()


main()



# p1 = Point(100, 100)
#     p2 = Point(700, 500)
#     line = Line(p1, p2)
#     win.draw_line(line, "black")