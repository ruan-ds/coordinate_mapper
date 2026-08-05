from dataclasses import (
    asdict,
    dataclass,
    field
)


@dataclass
class Point:
    id: int
    x: int
    y: int
    group: str = "default"

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Vertex:

    id: int

    start_point: Point
    end_point: Point

    points: list[Point] = field(
        default_factory=list
    )

    count: int = 0
    density: int = 100


    def group_name(self):
        return f"vertex_{self.id}"


    def get_points(self):

        return [
            self.start_point,
            *self.points,
            self.end_point
        ]


    def update_settings(
        self,
        count,
        density
    ):

        self.count = count
        self.density = density


    def contains_point(self, point):

        return point in self.get_points()