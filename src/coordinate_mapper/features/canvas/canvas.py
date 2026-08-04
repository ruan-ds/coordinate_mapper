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
from coordinate_mapper.features.canvas.events import CanvasEventsMixin
from coordinate_mapper.features.canvas.commands import CanvasCommandsMixin
from coordinate_mapper.features.canvas.image import CanvasImageMixin
from coordinate_mapper.features.canvas.menu import CanvasMenuMixin
from coordinate_mapper.features.canvas.project import CanvasProjectMixin
from coordinate_mapper.features.canvas.viewport import CanvasViewportMixin
from coordinate_mapper.features.project.storage import save_project
from coordinate_mapper.features.tools.base import ToolManager
from coordinate_mapper.features.tools.point import PointTool


class Canvas(
    CanvasDrawingMixin,
    CanvasEventsMixin,
    CanvasCommandsMixin,
    CanvasImageMixin,
    CanvasMenuMixin,
    CanvasProjectMixin,
    CanvasViewportMixin,
    QGraphicsView
    ):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.annotation = AnnotationManager()
        self.tools = ToolManager(
            PointTool()
        )

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