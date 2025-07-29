from livelocrawler import LiveloCrawler

crawler = LiveloCrawler()

print('# getting partners...')
partners = crawler.get_partners_data()
print('# partners got succesfully')
print(partners)

print('# saving partners to file partners.json...')
crawler.save_partners_to_json()