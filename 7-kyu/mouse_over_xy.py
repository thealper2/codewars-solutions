class MouseOver:
    def __init__(self, rectangles):
        self.rectangles = rectangles

    def find_rectangle(self, x, y):
        for rect in self.rectangles:
            rect_x, rect_y, width, height = rect
            if (rect_x <= x <= rect_x + width) and (rect_y <= y <= rect_y + height):
                return rect
        return None
