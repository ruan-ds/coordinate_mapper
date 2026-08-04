from coordinate_mapper.features.annotation.models import Point


class AnnotationManager:
    def __init__(self):
        self.points = []
        self.current_group = "default"
        self.next_id = 1

    def add_point(self, x: int, y: int) -> Point:

        point = Point(id=self.next_id, x=x, y=y, group=self.current_group)

        self.points.append(point)

        self.next_id += 1

        return point

    def remove_last(self):

        if not self.points:
            return None

        return self.points.pop()

    def get_points(self):

        return self.points

    def remove(self, point):

        if point in self.points:
            self.points.remove(point)

    def clear(self):

        self.points.clear()
        self.next_id = 1
