from PySide6.QtGui import QTransform


class CanvasViewportMixin:
    def update_scale(self):

        scene = self.sceneRect()

        if scene.isEmpty():
            return

        viewport = self.viewport().rect()

        scale = min(
            viewport.width() / scene.width(),
            viewport.height() / scene.height(),
        )

        self.setTransform(QTransform())

        self.scale(scale, scale)

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_scale()
