BASE_URL = "https://www.dse.com.bd"
COMPANY_LISTING_ENDPOINT = "/company_listing.php"
NEWS_ARCHIVE_ENDPOINT = "/news_archive.php"
NEWS_LISTING_ENDPOINT = "/old_news.php?inst={sel}&criteria=3&archive=news"
CRAWLING_LIMIT = 250

NEWS_ARCHIVE_FILE_PATH = "output/news_archive.csv"
COMPANY_LISTING_FILE_PATH = "output/company_listing.csv"
COMBINE_DATA_FILE_PATH = "output/combine_data.csv"

SELECT_XPATH = "//select/option/text()"
TABLE_NEWS_XPATH = "//*[@class='table-news']"
TABLE_TD_XPATH = ".//td/text()"
COMPANY_LIST_XPATH = "//*[@class='BodyContent']"
HREF_TAG_XPATH = "a/text()"
SPAN_XPATH = "span/text()"

NEWS_COLUMN = ['Trading Code', 'News Title', 'News', 'Post Date']
COMPANY_INFO_COLUMN = ['Trading Code', 'Company Name']
