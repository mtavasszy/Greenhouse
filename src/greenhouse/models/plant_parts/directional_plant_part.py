from dataclasses import dataclass
from functools import cached_property
import math

from greenhouse import config
from greenhouse.models.plant_parts.plant_part import PlantPart


@dataclass
class DirectionalPlantPart(PlantPart):
    length: float
    width: float
    dir: float

    @property
    def area(self) -> float:
        return self.length * self.width

    @property
    def circumference(self) -> float:
        return 2 * self.length + 2 * self.width

    @cached_property
    def dx(self) -> float:
        """Unit dx for direction"""
        return math.cos(self.dir)

    @cached_property
    def dy(self) -> float:
        """Unit dy for direction"""
        return math.sin(self.dir)

    @property
    def x2(self) -> float:
        return self.x + self.dx * self.length

    @property
    def y2(self) -> float:
        return self.y + self.dy * self.length

    @property
    def water_cap(self) -> float:
        return self.area * config.WATER_CAP_FACTOR

    @property
    def energy_cap(self) -> float:
        return self.area * config.ENERGY_CAP_FACTOR
