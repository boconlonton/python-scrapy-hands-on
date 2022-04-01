from scrapy import Spider

from crawler.items import Job


class XmlFeedSpiderSpider(Spider):
    name = 'xml_feed_spider'
    allowed_domains = ['appone.com']
    start_urls = ['https://www.appone.com/branding/adfeed/default.asp?servervar=Valvoline'
                  'InstantOilChange.AdFeed.appone.com&all=yes&accesscode=any']

    def parse(self, response, **kwargs):
        jobs = response.xpath('//Job')
        for job in jobs:
            job_id = job.xpath('.//JobID/text()').extract_first()
            job_title = job.xpath('.//Title/text()').extract_first()
            category = job.xpath('.//Category/text()').extract_first()
            description = job.xpath('.//Description/text()').extract_first()
            url = job.xpath('.//ApplyURL/text()').extract_first()
            yield Job(rid=job_id,
                      title=job_title,
                      category_list=[category],
                      description=description,
                      url=url)
