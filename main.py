from livelocrawler.crawler import LiveloCrawler

crawler = LiveloCrawler()

partners = crawler.get_partners_data()

print(f'{partners=}')