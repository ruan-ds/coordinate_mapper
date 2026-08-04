from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsView,
    QMenu,
    QFileDialog,
)

from PySide6.QtGui import (
    QKeySequence,
    QPixmap,
    QShortcut,
    QTransform,
)

from coordinate_mapper.features.annotation.manager import AnnotationManager
from coordinate_mapper.features.canvas.drawing import CanvasDrawingMixin
from coordinate_mapper.features.canvas.viewport import CanvasViewportMixin
from coordinate_mapper.features.project.storage import save_project


class Canvas(
    CanvasDrawingMixin,
    CanvasViewportMixin,
    QGraphicsView,
    ):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.annotation = AnnotationManager()

        self.image_path = None
        self.image_width = 0
        self.image_height = 0
        self.pixmap = None

        self.setMouseTracking(True)
        self.setAlignment(Qt.AlignCenter)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setTransformationAnchor(QGraphicsView.AnchorViewCenter)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        QShortcut(QKeySequence("Ctrl+S"), self, self.save_project)
        QShortcut(QKeySequence("Ctrl+Z"), self, self.undo)

    def load_image(self, path):

        self.pixmap = QPixmap(path)

        self.image_path = path
        self.image_width = self.pixmap.width()
        self.image_height = self.pixmap.height()

        self.annotation.clear()

        self.setSceneRect(self.pixmap.rect())

        self.draw_image()
        self.update_scale()

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

    def save_project(self):

        if not self.image_path:
            return

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar projeto",
            "points.json",
            "JSON (*.json)",
        )

        if not filename:
            return

        project = {
            "image": {
                "path": self.image_path,
                "width": self.image_width,
                "height": self.image_height,
            },
            "points": [
                point.to_dict()
                for point in self.annotation.get_points()
            ],
        }

        save_project(project, filename)

    def show_point_menu(self, point):

        menu = QMenu(self)

        delete_action = menu.addAction("Excluir ponto")

        action = menu.exec(self.cursor().pos())

        if action == delete_action:

            self.annotation.remove(point)

            self.redraw()

    def undo(self):

        removed = self.annotation.remove_last()

        if removed:
            self.redraw()