from crawler.page_crawler import PageCrawler
from utils.resource_pool import ResourcePool


def crawl_website(base_url, start_url):
    crawler = PageCrawler(base_url)
    pool = ResourcePool(num_workers=100)

    def crawl_url(url):
        crawler.crawl(url)

    pool.spawn_worker(crawl_url, start_url)
    pool.wait_for_free_worker()

    links = crawler.all_links

    results = []
    for link in links:
        results.append(f"{base_url} -> {link}")

    return results


if __name__ == '__main__':
    base_url = 'bbc.co.uk'
    start_url = 'https://www.bbc.co.uk'

    results = crawl_website(base_url, start_url)

    # Print the results in the specified format
    for result in results:
        print(result)

    print(f"Total links found: {len(results)}")
    print(f"Total unique links found: {len(set(results))}")
    print(f"Total duplicate links found: {len(results) - len(set(results))}")
