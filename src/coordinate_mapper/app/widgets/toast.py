from PySide6.QtCore import (
    QPropertyAnimation,
    Qt,
    QTimer,
)
from PySide6.QtWidgets import (
    QGraphicsOpacityEffect,
    QLabel,
)


class Toast(QLabel):
    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowFlags(Qt.ToolTip)

        self.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0;
                color: #202020;
                border: 1px solid gray;
                border-radius: 10px;
                padding: 8px 14px;
                font-weight: bold;
            }
        """)

        self.effect = QGraphicsOpacityEffect(self)

        self.setGraphicsEffect(self.effect)

        self.animation = None

    def show_message(self, text, duration=2000):

        self.setText(text)
        self.adjustSize()

        self.effect.setOpacity(1)

        parent = self.parent()

        x = (parent.width() - self.width()) // 2

        y = 40

        self.move(x, y)

        self.show()

        QTimer.singleShot(duration, self.fade_out)

    def fade_out(self):

        self.animation = QPropertyAnimation(self.effect, b"opacity")

        self.animation.setDuration(500)

        self.animation.setStartValue(1)
        self.animation.setEndValue(0)

        self.animation.finished.connect(self.hide)

        self.animation.start()
