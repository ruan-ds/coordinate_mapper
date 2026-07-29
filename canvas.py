from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QKeySequence, QPen, QPixmap
from PySide6.QtWidgets import (
    QFileDialog,
    QGraphicsScene,
    QGraphicsView,
)

from PySide6.QtGui import (
    QColor,
    QKeySequence,
    QPen,
    QPixmap,
    QShortcut,
)

from models import Point
from storage import save_project


class Canvas(QGraphicsView):

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.points = []

        self.image_path = None
        self.image_width = 0
        self.image_height = 0

        self.current_group = "default"
        self.next_id = 1

        self.setRenderHints(self.renderHints())
        self.setMouseTracking(True)

        QShortcut(QKeySequence("Ctrl+S"), self, self.save_project)


    def load_image(self, path: str):

        pixmap = QPixmap(path)

        self.scene.clear()

        self.scene.addPixmap(pixmap)

        self.image_path = path
        self.image_width = pixmap.width()
        self.image_height = pixmap.height()

        self.points.clear()
        self.next_id = 1

        self.setSceneRect(pixmap.rect())
        self.resize(
            self.image_width + 2,
            self.image_height + 2
        )


    def mousePressEvent(self, event):

        pos = self.mapToScene(event.position().toPoint())

        x = int(pos.x())
        y = int(pos.y())

        if event.button() == Qt.LeftButton:

            point = Point(
                id=self.next_id,
                x=x,
                y=y,
                group=self.current_group
            )

            self.points.append(point)
            self.next_id += 1

            self.draw_point(point)

        elif event.button() == Qt.RightButton:

            if self.points:
                self.points.pop()
                self.redraw()

        super().mousePressEvent(event)


    def draw_point(self, point: Point):

        radius = 4

        pen = QPen(QColor("red"))

        self.scene.addEllipse(
            point.x - radius,
            point.y - radius,
            radius * 2,
            radius * 2,
            pen
        )


    def redraw(self):

        pixmap = QPixmap(self.image_path)

        self.scene.clear()
        self.scene.addPixmap(pixmap)

        for point in self.points:
            self.draw_point(point)


    def save_project(self):

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar projeto",
            "points.json",
            "JSON (*.json)"
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
                for point in self.points
            ]
        }

        save_project(project, filename)