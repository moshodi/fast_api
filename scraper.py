from requests_html import HTMLSession


class Scraper():
    def scrapedata(self, tag):
        # tag = input('What Tag Bruh \n')
        # url = f'https://quotes.toscrape.com/tag/{tag}'
        
        url = f'https://google.com/search?q={tag}'

        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)
        qlist = []
        quotes = r.html.find('div.yuRUbf')

        for q in quotes:
            item = {
                'Title': q.find('h3', first=True).text.strip(),
                'Link': q.find('a', first=True).text.strip(),
            }
            print(item)
            qlist.append(item)

        return qlist

quotes = Scraper()

# quotes.scrapedata('life')

