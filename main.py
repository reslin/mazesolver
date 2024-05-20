from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win_width = 800
    win_height = 600
    margin = 50
    rows = 12
    cols = 15
    cell_size_x = (win_width - 2 * margin) // cols
    cell_size_y = (win_height - 2 * margin) // rows

    win = Window(win_width, win_height)

    # c1 = Cell(win)
    # c1.has_right_wall = False
    # c1.draw(50, 50, 100, 100)

    # c2 = Cell(win)
    # c2.has_left_wall = False
    # c2.has_bottom_wall = False
    # c2.draw(100, 50, 150, 100)

    # c1.draw_move(c2)

    # c3 = Cell(win)
    # c3.has_top_wall = False
    # c3.has_right_wall = False
    # c3.draw(100, 100, 150, 150)

    # c2.draw_move(c3)

    # c4 = Cell(win)
    # c4.has_left_wall = False
    # c4.draw(150, 100, 200, 150)

    # c3.draw_move(c4, True)

    m = Maze(margin, margin, rows, cols, cell_size_x, cell_size_y, win)
    m._break_entrance_and_exit()

    win.wait_for_close()


main()
