import scrapy
from config.utils.CSVService import CSVService
import pandas as pd
import config.utils.constants as constants
from config.utils.utils import name_formatting


class DSESpider(scrapy.Spider):
    """
    Scrapy spider class for scraping data and processing for analysis.
    """

    name = "dse"
    news_csv = CSVService(constants.NEWS_ARCHIVE_FILE_PATH, constants.NEWS_COLUMN)
    company_csv = CSVService(constants.COMPANY_LISTING_FILE_PATH, constants.COMPANY_INFO_COLUMN)
    allowed_domains = ['dse.com.bd']
    start_urls = ['%s%s' % (constants.BASE_URL, constants.NEWS_ARCHIVE_ENDPOINT)]

    def __init__(self, *args, **kwargs):
        super(DSESpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        yield scrapy.Request('%s%s' % (constants.BASE_URL, constants.COMPANY_LISTING_ENDPOINT),
                             callback=self.company_parse)

        for item in response.xpath(constants.SELECT_XPATH).getall()[1:constants.CRAWLING_LIMIT+1]:
            yield scrapy.Request('%s%s' % (constants.BASE_URL, constants.NEWS_LISTING_ENDPOINT.format(sel=item)),
                                 callback=self.news_parse, meta={"csvFile": self.news_csv})

    def close(self, spider, reason):
        self.news_csv.close()
        self.company_csv.close()
        self.merged_two_csv_file()
        closed = getattr(spider, 'closed', None)
        if callable(closed):
            return closed(reason)

    def news_parse(self, response):
        mycsv = response.meta['csvFile']
        for item in response.xpath(constants.TABLE_NEWS_XPATH):
            news_extract = item.xpath(constants.TABLE_TD_XPATH).extract()
            if len(news_extract) >= 4:
                mycsv.write({
                    constants.NEWS_COLUMN[0]: news_extract[0],
                    constants.NEWS_COLUMN[1]: news_extract[1],
                    constants.NEWS_COLUMN[2]: news_extract[2],
                    constants.NEWS_COLUMN[3]: news_extract[3],
                })

    def company_parse(self, response):
        companyInfoList = []
        for sel in response.xpath(constants.COMPANY_LIST_XPATH):
            trading_code = sel.xpath(constants.HREF_TAG_XPATH).extract()
            company_name = sel.xpath(constants.SPAN_XPATH).extract()
            if 'More...' in trading_code:
                trading_code.remove('More...')

            for idx, i in enumerate(trading_code):
                companyInfoList.append({
                    constants.COMPANY_INFO_COLUMN[0]: i,
                    constants.COMPANY_INFO_COLUMN[1]: name_formatting(company_name[idx])
                })

        for item in companyInfoList[0:constants.CRAWLING_LIMIT]:
            self.company_csv.write(item)

    @staticmethod
    def merged_two_csv_file():
        df1 = pd.read_csv(constants.COMPANY_LISTING_FILE_PATH)
        df2 = pd.read_csv(constants.NEWS_ARCHIVE_FILE_PATH)
        result = pd.merge(df1, df2, on=constants.COMPANY_INFO_COLUMN[0], how='left')
        result.to_csv(constants.COMBINE_DATA_FILE_PATH, header=True)
