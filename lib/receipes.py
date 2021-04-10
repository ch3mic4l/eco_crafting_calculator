class Receipes:

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
