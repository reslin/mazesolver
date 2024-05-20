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
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._animate_delay = 0.01  # quick construction
        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._animate_delay = 0.05  # slower "mazing"
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._animate_delay = 0.075 # nice and slow solving

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j]._visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            ni = direction[0] + i
            nj = direction[1] + j
            if ni < 0 or ni >= self._num_cols or nj < 0 or nj >= self._num_rows:
                continue
            if ni > i and self._cells[i][j].has_right_wall: # also checking neighbor cell is redundant
                continue
            if ni < i and self._cells[i][j].has_left_wall:
                continue
            if nj > j and self._cells[i][j].has_bottom_wall:
                continue
            if nj < j and self._cells[i][j].has_top_wall:
                continue
            if self._cells[ni][nj]._visited:
                continue
            self._cells[i][j].draw_move(self._cells[ni][nj])
            result = self._solve_r(ni, nj)
            if result:
                return True
            self._cells[i][j].draw_move(self._cells[ni][nj], True)
        return False


    def _create_cells(self):
        for col in range(self._num_cols):
            row_cells = []
            for row in range(self._num_rows):
                cell = Cell(self._win)
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
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        x = self._num_cols - 1
        y = self._num_rows - 1
        self._cells[x][y].has_bottom_wall = False
        self._draw_cell(x, y)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            to_visit_indices = self._list_unvisited_neighbors(i, j)
            if len(to_visit_indices) == 0:
                self._draw_cell(i, j)
                return
            rnd_idx = random.randrange(len(to_visit_indices))
            ni = to_visit_indices[rnd_idx][0]
            nj = to_visit_indices[rnd_idx][1]
            if ni > i:
                self._cells[i][j].has_right_wall = False
                self._cells[ni][j].has_left_wall = False
            elif ni < i:
                self._cells[i][j].has_left_wall = False
                self._cells[ni][j].has_right_wall = False
            elif nj > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][nj].has_top_wall = False
            else:
                self._cells[i][j].has_top_wall = False
                self._cells[i][nj].has_bottom_wall = False
            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row]._visited = False

    def _list_unvisited_neighbors(self, i, j):
        to_visit_indices = []
        delta_indices = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for idx in delta_indices:
            ni = idx[0] + i
            nj = idx[1] + j
            if ni < 0 or ni >= self._num_cols or nj < 0 or nj >= self._num_rows:
                continue
            if not self._cells[ni][nj]._visited:
                to_visit_indices.append((ni, nj))
        return to_visit_indices

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(self._animate_delay)