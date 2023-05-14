import contextlib
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


class PageCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()
        self.all_links = set()

    def crawl(self, url):
        if url not in self.visited_urls:
            self.visited_urls.add(url)
            response = self._fetch_page(url)
            if response is not None:
                self._parse_links(response.text, url)

    def _fetch_page(self, url):
        with contextlib.suppress(requests.exceptions.RequestException):
            response = requests.get(url)
            if response.status_code == 200:
                return response

    def _parse_links(self, content, url):
        soup = BeautifulSoup(content, 'html.parser')
        for anchor in soup.find_all('a'):
            if href := anchor.get('href'):
                absolute_url = urljoin(url, href)
                parsed_url = urlparse(absolute_url)
                if parsed_url.netloc.replace('www.', '') == self.base_url:
                    self.all_links.add(absolute_url)

    def start_crawling(self, url):
        self.crawl(url)
        self.visited_urls.add(url)  # Add the initial URL to the visited_urls set
        new_links = self.all_links.copy()

        while new_links:
            for link in new_links.copy():
                self.crawl(link)
                new_links.remove(link)

            new_links.update(self.all_links - self.visited_urls)
            self.visited_urls.update(new_links)  # Update the visited_urls set

        return self.all_links
