from dataclasses import dataclass

from greenhouse.models.plant_parts.directional_plant_part import DirectionalPlantPart


@dataclass
class Leaf(DirectionalPlantPart):
    pass
