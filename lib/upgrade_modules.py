from sys import exit


class UpgradeModules:

    def __init__(self):
        self.one = {
            'resource_cost': 10,
            'craft_time': 10
        }
        self.two = {
            'resource_cost': 25,
            'craft_time': 25
        }
        self.three = {
            'resource_cost': 40,
            'craft_time': 40
        }
        self.four = {
            'resource_cost': 45,
            'craft_time': 45
        }
        self.five = {
            'resource_cost': 50,
            'craft_time': 50
        }
        self.lookup_table = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5
        }

    def calculate_material_with_upgrades(self, level: int, quantity: (int, float)):
        if level == 0:
            return quantity
        upgrade_module = self.find_upgrade_module(level)
        resource_cost = self.__getattribute__(upgrade_module)['resource_cost']
        return quantity - ((quantity / 100) * resource_cost)

    def calculate_crafting_time_with_upgrades(self, level: int, crafting_time: (int, float)):
        if level == 0:
            return crafting_time
        upgrade_module = self.find_upgrade_module(level)
        resource_cost = self.__getattribute__(upgrade_module)['craft_time']
        return crafting_time - ((crafting_time / 100) * resource_cost)

    def find_upgrade_module(self, level: int):
        upgrade_level = ''
        for module_level in self.lookup_table:
            if self.lookup_table[module_level] == level:
                upgrade_level = module_level
                break
        if upgrade_level == '':
            print("Module {} not found".format(level))
            exit(102)
        return upgrade_level
