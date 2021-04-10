from urllib.request import urlopen, Request


class WebScraper:

    def __init__(self):
        self.eco_url = 'https://wiki.play.eco/en/Crafting'
        self.items = {'items': []}

    def scrape(self):
        req = Request(self.eco_url, headers={'User-Agent': 'Magic Browser'})
        response = urlopen(req)
        return response.read().decode('utf-8')
