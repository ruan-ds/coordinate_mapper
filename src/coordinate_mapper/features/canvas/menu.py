from PySide6.QtWidgets import QMenu


class CanvasMenuMixin:


    def show_point_context_menu(self, event):

        item = self.itemAt(
            event.position().toPoint()
        )

        if not item:
            return

        point = item.data(0)

        if not point:
            return


        menu = QMenu(self)

        delete_action = menu.addAction(
            "Excluir ponto"
        )

        action = menu.exec(
            self.cursor().pos()
        )


        if action == delete_action:

            self.annotation.remove(point)

            self.redraw()