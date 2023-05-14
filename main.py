from crawler.page_crawler import PageCrawler
from utils.resource_pool import ResourcePool


if __name__ == '__main__':
    base_url = 'bbc.co.uk'
    crawler = PageCrawler(base_url)

    pool = ResourcePool(num_workers=100)

    def crawl_url(url):
        crawler.crawl(url)

    pool.spawn_worker(crawl_url, 'https://www.bbc.co.uk')

    pool.wait_for_free_worker()

    links = crawler.all_links

    print(f"Found {len(links)} links")
    for link in links:
        print(f"{base_url} -> {link}")
