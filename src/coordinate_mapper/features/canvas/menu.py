from PySide6.QtWidgets import QMenu


class CanvasMenuMixin:

    def show_point_menu(self, point):

        menu = QMenu(self)

        delete_action = menu.addAction("Excluir ponto")

        action = menu.exec(self.cursor().pos())

        if action == delete_action:
            self.annotation.remove(point)
            self.redraw()