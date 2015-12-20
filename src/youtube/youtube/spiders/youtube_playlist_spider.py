import scrapy

class DmozSpider(scrapy.Spider):
    name = "youtube2"
    allowed_domains = ["youtube.com","google.com"]
    start_urls = [
        "https://www.youtube.com/playlist?list=PLXSUArFjDMwQlO21VhYEXPRfBjIM6v1SU"
    ]
    login_user = "myuname" # Email
    login_pass = "mypass"  # Passwd

    # https://accounts.google.com/ServiceLogin
    # https://www.youtube.com/playlist?list=PLXSUArFjDMwQlO21VhYEXPRfBjIM6v1SU

    http_user = "verykindjoe"
    http_pass = "gusgmlqkforl77"

    def parse(self, response):
        print "---------------------------------------------------------------------------"
        print response.xpath('//div[contains(@class, "yt-alert-message")]').extract()[1]
        print "---------------------------------------------------------------------------"
        # for sel in response.xpath('//pl-video-table'):
        #     title = sel.xpath('a/text()').extract()
        #     link = sel.xpath('a/@href').extract()
        #     desc = sel.xpath('text()').extract()
        #     print "test"
        #     print title, link, desc