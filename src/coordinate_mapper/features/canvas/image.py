from PySide6.QtGui import QPixmap


class CanvasImageMixin:

    def load_image(self, path):

        self.pixmap = QPixmap(path)

        self.image_path = path
        self.image_width = self.pixmap.width()
        self.image_height = self.pixmap.height()

        self.annotation.clear()

        self.setSceneRect(self.pixmap.rect())

        self.draw_image()

        self.update_scale()