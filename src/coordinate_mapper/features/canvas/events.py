from PySide6.QtCore import Qt


class CanvasEventsMixin:

    def mousePressEvent(self, event):

        if not self.image_path:
            return

        pos = self.mapToScene(event.position().toPoint())

        x = int(pos.x())
        y = int(pos.y())

        if x < 0 or y < 0 or x >= self.image_width or y >= self.image_height:
            return

        if event.button() == Qt.LeftButton:

            point = self.annotation.add_point(x, y)

            self.draw_point(point)

        elif event.button() == Qt.RightButton:

            item = self.itemAt(event.position().toPoint())

            if item:

                point = item.data(0)

                if point:
                    self.show_point_menu(point)