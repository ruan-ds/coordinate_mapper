from PySide6.QtCore import Qt

from coordinate_mapper.features.tools.base import BaseTool


class PointTool(BaseTool):
    def mouse_press(self, canvas, event):

        if event.button() != Qt.LeftButton:
            return

        pos = canvas.mapToScene(event.position().toPoint())

        x = int(pos.x())
        y = int(pos.y())

        if x < 0 or y < 0:
            return

        if x >= canvas.image_width:
            return

        if y >= canvas.image_height:
            return

        point = canvas.annotation.add_point(x, y)

        canvas.draw_point(point)
