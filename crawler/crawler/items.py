import scrapy


class Job(scrapy.Item):
    rid = scrapy.Field()
    uuid = scrapy.Field()
    url = scrapy.Field()
    location = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    postal_code = scrapy.Field()
    country = scrapy.Field()
    street_address = scrapy.Field()
    category_list = scrapy.Field()
    summary = scrapy.Field()
    description = scrapy.Field()
    title = scrapy.Field()
    apply_link = scrapy.Field()
    job_type = scrapy.Field()
    job_code = scrapy.Field()
    job_status = scrapy.Field()
    department = scrapy.Field()
    salary_info = scrapy.Field()
    email = scrapy.Field()
    record_name = scrapy.Field()
    is_internal = scrapy.Field()
    users = scrapy.Field()
    brand = scrapy.Field()
    date_posted = scrapy.Field()
    questionnaire_id = scrapy.Field()
    custom_fields = scrapy.Field()
    recruiter_name = scrapy.Field()
    paradox_location = scrapy.Field()