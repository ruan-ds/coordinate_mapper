from PySide6.QtCore import Qt


class CanvasEventsMixin:

    def mousePressEvent(self, event):

        if event.button() == Qt.RightButton:

            self.show_point_context_menu(event)
            return


        self.tools.mouse_press(
            self,
            event
        )


    def mouseMoveEvent(self, event):

        self.tools.mouse_move(
            self,
            event
        )


    def mouseReleaseEvent(self, event):

        self.tools.mouse_release(
            self,
            event
        )