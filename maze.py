import time, random
from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for col in range(self._num_cols):
            row_cells = []
            for row in range(self._num_rows):
                cell = Cell(self._win)
                # r = random.random()
                # if r < 0.25:
                #     cell.has_left_wall = False
                # elif r < 0.5:
                #     cell.has_top_wall = False
                # elif r < 0.75:
                #     cell.has_right_wall = False
                # else:
                #     cell.has_bottom_wall = False
                row_cells.append(cell)
            self._cells.append(row_cells)
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        if self._win is None:
            return
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        x = self._num_cols - 1
        y = self._num_rows - 1
        self._cells[x][y].has_bottom_wall = False
        self._draw_cell(x, y)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)