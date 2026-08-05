from coordinate_mapper.features.annotation.models import Point


class AnnotationManager:

    def __init__(self):

        self.points = []
        self.vertices = []

        self.current_group = "default"

        self.next_id = 1
        self.next_vertex_id = 1



    def add_point(
        self,
        x: int,
        y: int,
        group=None
    ):

        if group is None:
            group = self.current_group


        point = Point(
            id=self.next_id,
            x=x,
            y=y,
            group=group
        )

        self.points.append(point)

        self.next_id += 1

        return point



    def add_vertex(self, vertex):

        self.vertices.append(
            vertex
        )

        self.next_vertex_id += 1



    def get_vertices(self):

        return self.vertices



    def get_vertex(self, vertex_id):

        for vertex in self.vertices:

            if vertex.id == vertex_id:
                return vertex

        return None

    def get_next_vertex_id(self):

        return self.next_vertex_id

    def remove_vertex(self, vertex_id):

        vertex = self.get_vertex(
            vertex_id
        )

        if not vertex:
            return


        points = [
            vertex.start_point,
            *vertex.points,
            vertex.end_point
        ]


        for point in points:

            self.remove_point(
                point
            )


        self.vertices.remove(
            vertex
        )



    def remove_point(self, point):

        if point in self.points:

            self.points.remove(
                point
            )

    def remove_last(self):
        if not self.points:
            return None

        point = self.points.pop()

        return point

    def clear_vertex_points(self, vertex):

        for point in vertex.points:

            self.remove_point(
                point
            )

        vertex.points.clear()

    def get_points(self):

        return self.points



    def clear(self):

        self.points.clear()

        self.vertices.clear()

        self.next_id = 1

        self.next_vertex_id = 1