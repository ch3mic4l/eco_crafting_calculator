import argparse


class EcoArgParser:

    @staticmethod
    def parse_the_args():
        parser = argparse.ArgumentParser(description='Show Crafting Materials', usage='python eco_crafting_calculator.py --list-crafting-material -i "Steam Truck" -q 1 -m 1')
        parser.add_argument('-i', '--item', help='Name of the item you want to craft')
        parser.add_argument('-m', '--module', help='Level of the upgrade module you are using 0-5', type=int, default=0)
        parser.add_argument('-q', '--quantity', help='Number of items being crafted', type=int, default=1)
        parser.add_argument('--list-crafting-material', help='List crafting Material for the item', action='store_true')
        return parser.parse_args()
