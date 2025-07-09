from dataclasses import dataclass

from greenhouse.models.genome import Genome
from greenhouse.models.plant_parts.plant_part import PlantPart
from greenhouse.models.plant_parts.seed import Seed


@dataclass
class Flower(PlantPart):

    def is_complete(self, energy_target: float) -> bool:
        return self.energy >= energy_target

    def get_seed(self, genome: Genome) -> Seed:
        return Seed(x=self.x, y=self.y, energy=self.energy, genome=genome)
