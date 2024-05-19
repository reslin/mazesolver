from graphics import Line, Point

class Cell:
    def __init__(self, x1, x2, y1, y2, win,
                  has_left = True, has_right = True,
                  has_top = True, has_bottom = True):
        self.has_left_wall = has_left
        self.has_right_wall = has_right
        self.has_top_wall = has_top
        self.has_bottom_wall = has_bottom
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw_cell(self):
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))