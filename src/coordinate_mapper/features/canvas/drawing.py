from PySide6.QtGui import QColor, QPen, QPixmap


class CanvasDrawingMixin:
    def draw_point(self, point):

        radius = 4

        pen = QPen(QColor("red"))

        item = self.scene.addEllipse(
            point.x - radius, point.y - radius, radius * 2, radius * 2, pen
        )

        item.setData(0, point)

        return item

    def draw_image(self):

        pixmap = QPixmap(self.image_path)

        self.scene.clear()

        self.scene.addPixmap(pixmap)

    def redraw(self):

        self.draw_image()

        for point in self.annotation.get_points():
            self.draw_point(point)

        self.update_scale()
