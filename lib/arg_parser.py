import argparse


class EcoArgParser:

    @staticmethod
    def parse_the_args():
        parser = argparse.ArgumentParser(description='Show Crafting Materials')
        parser.add_argument('-i', '--item', help='Name of the item you want to craft')
        parser.add_argument('-m', '--module', help='Level of the Upgrade you are using 1-5')
        parser.add_argument('-q', '--quantity', help='Number of items being crafted')
        parser.add_argument('--list-crafting-material', help='List crafting Material for the item', action='store_true')
        return parser.parse_args()
