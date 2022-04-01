from scrapy import Spider

from scrapy.http import Request

from crawler.items import Job


class DynamicWebNuvasiveSpiderSpider(Spider):
    name = 'dynamic_web_nuvasive_spider'
    allowed_domains = ['nuvasive.avature.net']
    start_urls = ['http://nuvasive.avature.net']

    def start_requests(self):
        yield Request(f'{self.start_urls[0]}/careers/SearchJobs/?jobOffset=0')

    def parse(self, response, **kwargs):
        jobs = response.xpath('//a[text()="Apply Now"]/@href').extract()
        for job in jobs:
            yield Request(job,
                          callback=self.parse_jobs)


        next_page_url = response.xpath('//a[text()="Next >>"]/@href').extract_first()
        if next_page_url:
            yield Request(response.urljoin(next_page_url),
                          callback=self.parse)

    def parse_jobs(self, response, **kwargs):
        job_url = response.url
        job_title = response.xpath('//*[@itemprop="title"]/text()').extract_first()
        job_location = response.xpath('//*[@itemprop="jobLocation"]/text()').extract_first()
        job_id = response.xpath(
            '//div[@class="jobDetail__details-column"]/p/span[text()="Ref#:"]/ancestor::p/text()').extract_first()
        yield Job(
            url=job_url,
            title=job_title,
            location=job_location,
            rid=job_id
        )
