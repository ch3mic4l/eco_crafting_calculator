class ReceipeFilter:

    def __init__(self, receipe_list: list):
        self.receipe_list = receipe_list

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

    def print_crafting_materials(self, item_to_craft: str, qty: int = 1):
        item_found = False
        print("\nSearching for {}".format(item_to_craft))
        for receipe in self.receipe_list:
            for item in receipe.item:
                if item.lower() == item_to_craft.lower():
                    item_found = True
                    print("Found {}".format(item_to_craft))
                    print("Showing materials required to craft {} {}s".format(qty, item_to_craft))
                    print("\tCrafted at {}".format(receipe.crafting_station))
                    print("\tQuantity Produced {}".format(receipe.item[item]['quantity'] * qty))
                    print("\tCrafting Time (Mins): {}".format(receipe.crafting_time * qty))
                    print("\tLabor Cost: {}".format(receipe.labor_cost * qty))
                    print("\tXP Gained".format(receipe.xp_gained * qty))
                    for skill in receipe.level_needed:
                        print("\tRequired Skill: {} Level {}".format(skill, receipe.level_needed[skill]['level']))
                    print("\tMaterials Used:")
                    for material in receipe.materials:
                        print("\t\t{} x {}".format((receipe.materials[material]['quantity'] * qty), material))
        if not item_found:
            print("\nUnable to find: {}\n\nPlease check your spelling".format(item_to_craft))
