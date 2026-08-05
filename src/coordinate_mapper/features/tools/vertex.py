from PySide6.QtWidgets import QDialog

from coordinate_mapper.features.tools.base import BaseTool
from coordinate_mapper.features.geometry.interpolation import interpolate_points
from coordinate_mapper.features.dialogs.vertex_dialog import VertexDialog
from coordinate_mapper.features.annotation.models import Vertex


class VertexTool(BaseTool):

    def __init__(self):
        self.start_point = None
        self.end_point = None
        self.current_vertex_id = None
        self.creating = False


    def mouse_press(self, canvas, event):

        if event.button().name != "LeftButton":
            return


        pos = canvas.mapToScene(
            event.position().toPoint()
        )

        x = int(pos.x())
        y = int(pos.y())


        if x < 0 or y < 0:
            return

        if x >= canvas.image_width:
            return

        if y >= canvas.image_height:
            return



        # primeiro ponto do vertex

        if self.start_point is None:
            self.creating = True

            vertex_id = canvas.annotation.get_next_vertex_id()

            self.start_point = canvas.annotation.add_point(
                x,
                y,
                group=f"vertex_{vertex_id}"
            )

            self.current_vertex_id = vertex_id

            canvas.draw_vertex_point(
                self.start_point
            )

            return



        # segundo ponto do vertex

        self.end_point = canvas.annotation.add_point(
            x,
            y,
            group=f"vertex_{self.current_vertex_id}"
        )

        canvas.draw_vertex_point(
            self.end_point
        )



        dialog = VertexDialog(
            parent=canvas
        )


        if dialog.exec() != QDialog.Accepted:

            canvas.annotation.remove_point(
                self.start_point
            )

            canvas.annotation.remove_point(
                self.end_point
            )

            canvas.redraw()

            self.start_point = None
            self.end_point = None
            self.current_vertex_id = None
            self.creating = False

            return



        values = dialog.get_values()

        count = values["count"]
        percentage = values["percentage"]



        vertex = self.generate_vertex(
            canvas.annotation,
            self.start_point,
            self.end_point,
            count,
            percentage
        )

        canvas.draw_vertex(
            vertex
        )

        self.start_point = None
        self.end_point = None
        self.current_vertex_id = None

    def generate_vertex(
        self,
        annotation,
        start_point,
        end_point,
        count,
        percentage,
        vertex=None,
        vertex_id=None
    ):
        if vertex is not None:
            vertex_id = vertex.id

        elif vertex_id is None:
            vertex_id = self.current_vertex_id


        if vertex is not None:
            annotation.clear_vertex_points(
                vertex
            )


        coordinates = interpolate_points(
            start_point,
            end_point,
            count=count
        )


        coordinates = self.apply_density(
            coordinates,
            percentage
        )


        vertex_points = []

        for x, y in coordinates:
            point = annotation.add_point(
                x,
                y,
                group=f"vertex_{vertex_id}"
            )

            vertex_points.append(
                point
            )

        if vertex is None:

            vertex = Vertex(
                id=vertex_id,
                start_point=start_point,
                end_point=end_point,
                points=vertex_points,
                count=count,
                density=percentage
            )


            annotation.add_vertex(
                vertex
            )


        else:

            vertex.points = vertex_points
            vertex.count = count
            vertex.density = percentage

        return vertex

    def apply_density(
        self,
        points,
        percentage
    ):

        if not points:
            return []


        factor = percentage / 100


        center_x = (
            points[0][0]
            +
            points[-1][0]
        ) / 2


        center_y = (
            points[0][1]
            +
            points[-1][1]
        ) / 2


        result = []


        for x, y in points:

            new_x = (
                center_x
                +
                (x - center_x) * factor
            )


            new_y = (
                center_y
                +
                (y - center_y) * factor
            )


            result.append(
                (
                    int(new_x),
                    int(new_y)
                )
            )


        return result



    def reset(self, canvas):

        if self.creating:

            if self.start_point:
                canvas.annotation.remove_point(
                    self.start_point
                )

            if self.end_point:
                canvas.annotation.remove_point(
                    self.end_point
                )

            canvas.redraw()


        self.start_point = None
        self.end_point = None
        self.current_vertex_id = None
        self.creating = False