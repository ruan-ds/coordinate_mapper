from dataclasses import asdict, dataclass


@dataclass
class Point:
    id: int
    x: int
    y: int
    group: str = "default"

    def to_dict(self) -> dict:
        return asdict(self)
