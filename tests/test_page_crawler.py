import unittest
from crawler.page_crawler import PageCrawler


class PageCrawlerTests(unittest.TestCase):
    def test_crawl_single_page(self):
        # Create a PageCrawler instance
        base_url = 'example.com'
        crawler = PageCrawler(base_url)

        # Crawl a single page
        url = 'https://www.example.com/page1'
        crawler.start_crawling(url)

        # Assert the number of links found
        self.assertEqual(len(crawler.all_links), 0)

    def test_crawl_multiple_pages(self):
        # Create a PageCrawler instance
        base_url = 'example.com'
        crawler = PageCrawler(base_url)

        # Crawl multiple pages
        urls = [
            'https://www.example.com/page1',
            'https://www.example.com/page2',
            'https://www.example.com/page3',
        ]
        for url in urls:
            crawler.start_crawling(url)

        # Assert the number of links found
        self.assertEqual(len(crawler.all_links), 0)


if __name__ == '__main__':
    unittest.main()
