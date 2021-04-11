from lib import web_scrapper
from lib import html_parser
from lib import receipe_filter
from lib import arg_parser


def get_html():
    print('Downloading HTML from https://wiki.play.eco/en/Crafting')
    scraper = web_scrapper.WebScraper()
    return scraper.scrape()


def parse_html():
    parser = html_parser.HTMLParser(get_html())
    print('Parsing information from Crafting Page')
    parser.parse_receipes()
    return parser.receipes


def list_receipes(receipe_list: list):
    show_receipes = receipe_filter.ReceipeFilter(receipe_list)
    show_receipes.print_item_list()


def list_crafting_stations(receipe_list: list):
    show_receipes = receipe_filter.ReceipeFilter(receipe_list)
    show_receipes.print_crafting_stations()


def list_crafting_materials(receipe_list: list, item_to_craft: str, qty: int = 1):
    show_receipes = receipe_filter.ReceipeFilter(receipe_list)
    show_receipes.print_crafting_materials(item_to_craft, qty)


def parse_the_args():
    eco_args_parser = arg_parser.EcoArgParser().parse_the_args()
    if eco_args_parser.list_crafting_material:
        parsed_data = parse_html()
        list_crafting_materials(parsed_data, eco_args_parser.item, int(eco_args_parser.quantity))


if __name__ == '__main__':
    print()
    parse_the_args()
