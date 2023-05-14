# Website Crawler

This project implements a website crawler that can crawl a given website and collect all internal links within the website. It utilizes a resource pool and concurrent execution to improve efficiency.

## Code Structure

The codebase is organized as follows:

```shell

website_crawler/
├── crawler/
│ ├── init.py
│ └── page_crawler.py
├── tests/
│ ├── init.py
│ ├── test_page_crawler.py
│ └── test_resource_pool.py
├── utils/
│ ├── init.py
│ └── resource_pool.py
└── main.py
```

- The `crawler` directory contains the implementation of the website crawler in `page_crawler.py`.
- The `utils` directory contains the resource pool implementation in `resource_pool.py`.
- The `tests` directory contains the unit tests for the website crawler and resource pool.

## Setup

To set up the project and run the crawler, follow these steps:
1. Clone the repository:

```shell
git clone https://github.com/your-username/website-crawler.git`
```

2. Install the dependencies. It is recommended to use a virtual environment:

```shell
cd website-crawler
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Usage

```shell
python main.py
```

## Testing

To run the unit tests, execute the following command:

```shell
python -m unittest discover -s tests
```

This will run all the test cases defined in the `tests` directory and provide you with the test results.

