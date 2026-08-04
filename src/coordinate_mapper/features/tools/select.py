from coordinate_mapper.features.tools.base import BaseTool


class SelectTool(BaseTool):

    def __init__(self):
        self.selected_point = None
        self.dragging = False


    def mouse_press(self, canvas, event):

        item = canvas.itemAt(
            event.position().toPoint()
        )

        if not item:
            return

        point = item.data(0)

        if point:
            self.selected_point = point
            self.dragging = True


    def mouse_move(self, canvas, event):

        if not self.dragging:
            return

        if not self.selected_point:
            return

        pos = canvas.mapToScene(
            event.position().toPoint()
        )

        x = int(pos.x())
        y = int(pos.y())

        if x < 0 or y < 0:
            return

        if x >= canvas.image_width:
            return

        if y >= canvas.image_height:
            return

        self.selected_point.x = x
        self.selected_point.y = y

        canvas.redraw()


    def mouse_release(self, canvas, event):

        self.dragging = False
        self.selected_point = None