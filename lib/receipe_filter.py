from lib import upgrade_modules


class ReceipeFilter:

    def __init__(self, receipe_list: list):
        self.receipe_list = receipe_list
        self.module_upgrade = upgrade_modules.UpgradeModules()

    def print_item_list(self):
        for receipe in self.receipe_list:
            for item in receipe.item:
                print(item)

    def print_crafting_stations(self):
        print('Searching for all Crafting Stations')
        crafting_stations = []
        for receipe in self.receipe_list:
            if receipe.crafting_station not in crafting_stations:
                crafting_stations.append(receipe.crafting_station)
        for station in crafting_stations:
            print(station)

    def print_crafting_materials(self, item_to_craft: str, qty: int = 1, module: int = 0):
        item_found = False
        print("\nSearching for {}".format(item_to_craft))
        for receipe in self.receipe_list:
            for item in receipe.item:
                if item.lower() == item_to_craft.lower():
                    item_found = True
                    purlize_item = item_to_craft
                    if qty > 1:
                        purlize_item = "{}s".format(item_to_craft)
                    mats_to_craft = "Showing materials required to craft {} {}".format(qty, purlize_item)
                    if module > 0:
                        mats_to_craft = "{} with upgrade module {}'s".format(mats_to_craft, module)
                    print("Found {}".format(item_to_craft))
                    print(mats_to_craft)
                    print("\tCrafted at {}".format(receipe.crafting_station))
                    print("\tQuantity Produced {}".format(receipe.item[item]['quantity'] * qty))
                    print("\tCrafting Time (Mins): {}".format(self.module_upgrade.calculate_crafting_time_with_upgrades(module, receipe.crafting_time * qty)))
                    print("\tLabor Cost: {}".format(receipe.labor_cost * qty))
                    print("\tXP Gained".format(receipe.xp_gained * qty))
                    for skill in receipe.level_needed:
                        print("\tRequired Skill: {} Level {}".format(skill, receipe.level_needed[skill]['level']))
                    print("\tMaterials Used:")
                    for material in receipe.materials:
                        print("\t\t{} x {}".format(self.module_upgrade.calculate_material_with_upgrades(module, receipe.materials[material]['quantity'] * qty), material))
                        self.print_sub_crafting_materials(material, 2, self.module_upgrade.calculate_material_with_upgrades(module, receipe.materials[material]['quantity'] * qty))
        if not item_found:
            print("\nUnable to find: {}\n\nPlease check your spelling".format(item_to_craft))

    def print_sub_crafting_materials(self, item_to_craft: str, print_level: int, qty: int, module: int = 0):
        item_found = False
        for receipe in self.receipe_list:
            temp_print_level = print_level + 1
            if item_found:
                break
            for item in receipe.item:
                if item == item_to_craft:
                    item_found = True
                    mat_print = ''
                    for level in range(temp_print_level):
                        mat_print += "\t"
                    for material in receipe.materials:
                        print("{}{} x {}".format(mat_print, (self.module_upgrade.calculate_material_with_upgrades(module, receipe.materials[material]['quantity'] * qty) / receipe.item[item]['quantity']), material))
                        self.print_sub_crafting_materials(material, temp_print_level + 1, self.module_upgrade.calculate_material_with_upgrades(module, (receipe.materials[material]['quantity'] * qty) / receipe.item[item]['quantity']))
