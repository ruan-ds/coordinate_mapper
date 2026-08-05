from PySide6.QtWidgets import QDialog, QMenu

from coordinate_mapper.features.dialogs.vertex_dialog import VertexDialog


class CanvasMenuMixin:
    def show_point_context_menu(self, event):

        item = self.itemAt(event.position().toPoint())

        if not item:
            return

        point = item.data(0)

        if not point:
            return

        menu = QMenu(self)

        delete_action = menu.addAction("Excluir ponto")

        action = menu.exec(self.cursor().pos())

        if action == delete_action:
            self.annotation.remove_point(point)

            self.redraw()

    def show_vertex_context_menu(self, event):

        item = self.itemAt(
            event.position().toPoint()
        )

        if not item:
            return

        vertex_id = item.data(2)

        vertex = self.annotation.get_vertex(
            vertex_id
        )

        if not vertex:
            return

        menu = QMenu(self)

        edit_action = menu.addAction(
            "Editar vértice"
        )

        delete_action = menu.addAction(
            "Excluir vértice"
        )

        action = menu.exec(
            self.cursor().pos()
        )

        if action == edit_action:

            dialog = VertexDialog(
                parent=self
            )

            dialog.count.setValue(
                vertex.count
            )

            dialog.density.setValue(
                vertex.density
            )

            if dialog.exec() == QDialog.Accepted:
                values = dialog.get_values()

                self.tools.vertex_tool.generate_vertex(
                    self.annotation,
                    vertex.start_point,
                    vertex.end_point,
                    values["count"],
                    values["percentage"],
                    vertex=vertex
                )

                self.redraw()


        elif action == delete_action:

            self.annotation.remove_vertex(
                vertex.id
            )

            self.redraw()