# loot_simulator/defeat_simulator.py

from collections import defaultdict


class DefeatSimulator:
    def __init__(self, loot_simulator):
        self.loot_simulator = loot_simulator

    def simulate_defeats(self, num_defeats):
        total_loot = []
        rarity_summary = defaultdict(int)

        for _ in range(num_defeats):
            loot = self.loot_simulator.simulate_boss_loot()
            total_loot.extend(loot)
            for item in loot:
                rarity_summary[item.rarity] += 1

        return total_loot, rarity_summary
