from lib import web_scrapper
from lib import html_parser
from lib import receipes


def get_html():
    print('Downloading HTML from https://wiki.play.eco/en/Crafting')
    scraper = web_scrapper.WebScraper()
    return scraper.scrape()


def parse_html():
    print('Parsing information from Crafting Page')
    parser = html_parser.HTMLParser(get_html())
    parser.parse_receipes()
    return parser.receipes


def list_receipes(receipe_list: list):
    show_receipes = receipes.Receipes(receipe_list)
    show_receipes.print_crafting_stations()


if __name__ == '__main__':
    parsed_data = parse_html()
    list_receipes(parsed_data)
