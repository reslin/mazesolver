from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win_width = 1000
    win_height = 800
    margin = 50
    rows = 14
    cols = 18
    cell_size_x = (win_width - 2 * margin) // cols
    cell_size_y = (win_height - 2 * margin) // rows

    win = Window(win_width, win_height)

    m = Maze(margin, margin, rows, cols, cell_size_x, cell_size_y, win)
    m.solve()

    win.wait_for_close()


main()
