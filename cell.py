from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self._visited = False
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        line = Line(Point(x1, y1), Point(x1, y2))
        self.draw_wall(line, self.has_left_wall)
        line = Line(Point(x1, y1), Point(x2, y1))
        self.draw_wall(line, self.has_top_wall)
        line = Line(Point(x2, y1), Point(x2, y2))
        self.draw_wall(line, self.has_right_wall)
        line = Line(Point(x1, y2), Point(x2, y2))
        self.draw_wall(line, self.has_bottom_wall)

    def draw_wall(self, line, has_wall):
        if has_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        x_center = (self._x1 + self._x2) // 2
        y_center = (self._y1 + self._y2) // 2

        x_center2 = (to_cell._x1 + to_cell._x2) // 2
        y_center2 = (to_cell._y1 + to_cell._y2) // 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)
