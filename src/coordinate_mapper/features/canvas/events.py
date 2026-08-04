class CanvasEventsMixin:

    def mousePressEvent(self, event):
        self.tools.mouse_press(
            self,
            event
        )