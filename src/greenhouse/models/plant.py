from dataclasses import dataclass

from greenhouse import config
from greenhouse.models.plant_parts import Flower, Root, Leaf, Branch, Seed
from greenhouse.models.genome import Genome
from greenhouse.models.plant_parts.plant_part import PlantPart


@dataclass
class Plant:

    age: float = 0

    genome: Genome

    roots: list[Root]
    branches: list[Branch]
    leafs: list[Leaf]
    flowers: list[Flower]

    def update(self, dt: float):

        age += dt

        self._update_roots(dt)
        self._update_branches(dt)
        self._update_leafs(dt)
        self._update_flowers(dt)

    def _update_roots(self, dt: float):
        self._update_water_absorption(dt)

    def _update_branches(self, dt: float):
        pass

    def _update_leafs(self, dt: float):
        self._update_photosynthesis(dt)

    def _update_flowers(self, dt: float):
        pass

    ## ROOTS ##
    def _update_water_absorption(self, dt: float):
        water_list = self._compute_root_water_gain(dt)
        for water, root in zip(water_list, self.roots):
            root.water = min(root.water + water, root.water_cap)

    def _compute_root_water_gain(self, dt: float) -> list[float]:
        return [config.ROOT_WATER_GAIN_FACTOR * dt for _ in self.roots]

    # def _determine_actions(self):

    ## LEAVES ##
    def _update_photosynthesis(self, dt: float):
        energy_list = self._compute_leaf_energy_gain(dt)
        for energy, leaf in zip(energy_list, self.leafs):
            leaf.energy = min(leaf.energy + energy, leaf.energy_cap)

    def _compute_leaf_energy_gain(self, dt: float) -> list[float]:
        return [config.ROOT_WATER_GAIN_FACTOR * dt for _ in self.roots]

    ## GENERAL ##
    def _share_resources_with_parents(self):
        for part in self.roots + self.branches + self.leafs:
            parent = self._get_part_parent(part)
            self._share_resources_with_parent(self, part, parent)

    def _get_part_parent(self, part: PlantPart):

        # Check for special case of seed
        if part.parent_id == -1:
            if isinstance(part, Root):
                return self.branches[0]
            return self.roots[0]

        if isinstance(part, Root):
            return self.roots[part.parent_id]
        return self.branches[part.parent_id]

    def _share_resources_with_parent(self, part: PlantPart, parent: PlantPart):
        energy_diff = part.energy - parent.energy
        # TODO share based on capacity
        energy_transfer = max(min(energy_diff / 2, config.MAX_SHARE_RATE), -config.MAX_SHARE_RATE)
