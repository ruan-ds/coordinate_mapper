class CanvasCommandsMixin:
    def undo(self):

        removed = self.annotation.remove_last()

        if removed:
            self.redraw()
