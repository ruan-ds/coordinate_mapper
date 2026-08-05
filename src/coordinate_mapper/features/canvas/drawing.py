from PySide6.QtGui import QColor, QPen, QPixmap


class CanvasDrawingMixin:

    def draw_point(self, point):

        radius = 4

        pen = QPen(
            QColor("red")
        )

        item = self.scene.addEllipse(
            point.x - radius,
            point.y - radius,
            radius * 2,
            radius * 2,
            pen
        )

        item.setData(
            0,
            point
        )

        item.setData(
            1,
            "point"
        )

        return item


    def draw_vertex_point(self, point):

        radius = 4

        pen = QPen(
            QColor("blue")
        )

        item = self.scene.addEllipse(
            point.x - radius,
            point.y - radius,
            radius * 2,
            radius * 2,
            pen
        )

        item.setData(
            0,
            point
        )

        item.setData(
            1,
            "vertex"
        )

        return item


    def draw_vertex(self, vertex):

        items = []

        points = [
            vertex.start_point,
            *vertex.points,
            vertex.end_point
        ]

        for point in points:

            item = self.draw_vertex_point(
                point
            )

            item.setData(
                2,
                vertex.id
            )

            items.append(
                item
            )

        return items


    def draw_image(self):

        pixmap = QPixmap(
            self.image_path
        )

        self.scene.clear()

        self.scene.addPixmap(
            pixmap
        )


    def redraw(self):
        self.draw_image()


        # pontos comuns
        for point in self.annotation.get_points():

            if point.group.startswith(
                "vertex_"
            ):
                continue

            self.draw_point(
                point
            )


        # vertices
        for vertex in self.annotation.get_vertices():

            self.draw_vertex(
                vertex
            )


        self.update_scale()