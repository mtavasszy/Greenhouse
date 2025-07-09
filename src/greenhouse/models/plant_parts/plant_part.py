from dataclasses import dataclass


@dataclass
class PlantPart:
    x: float
    y: float
    age: int
    water: float
    energy: float

    @property
    def water_cap(self) -> float:
        raise NotImplementedError()

    @property
    def energy_cap(self) -> float:
        raise NotImplementedError()

    parent_id: int
