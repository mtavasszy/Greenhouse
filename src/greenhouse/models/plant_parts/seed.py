from dataclasses import dataclass

from greenhouse.models.genome import Genome


@dataclass
class Seed:
    x: float
    y: float
    energy: float
    water: float
    genome: Genome
