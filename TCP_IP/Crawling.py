from bs4 import BeautifulSoup
import urllib.request


def crawl(url: str):
    try:
        parser = 'lxml'
        resp = urllib.request.urlopen(url)
        soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
        if soup.find('title'):
            title = soup.find('title').get_text()
        else:
            title = 'No title'
        links = list()
        for link in soup.find_all('a', href=True):
            if 'http' in link['href']:
                links.append(link['href'])
            else:
                links.append(url + link['href'])
        return title, links
    except Exception as e:
        print(e)
        return None


def run():
    url = "http://vlada.cz"
    try:
        title, links = crawl(url)
        print(title)
        print(len(links))
        for link in links:
            if crawl(link):
                title, links = crawl(link)
                print(title)
                print(len(links))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
