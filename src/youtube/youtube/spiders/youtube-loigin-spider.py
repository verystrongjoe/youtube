import scrapy

from scrapy.http import Request, FormRequest
from scrapy.selector import HtmlXPathSelector


class LoginSpider(scrapy.Spider):
    name = 'youtube'
    start_urls = ['https://accounts.google.com/ServiceLoginAuth']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'Email': 'xxx', 'Passwd': '~xxx'},
            callback=self.after_login
        )

    def after_login(self, response):

        print "---------------------------------------------------------------------------"
        # print response.xpath('//div[contains(@class, "yt-alert-message")]').extract()[1]
        print response.headers["x-frame-options"]
        print "---------------------------------------------------------------------------"

        # check login succeed before going on
        if "error-msg" in response.body:
            self.logger.error("Login failed")
            print "---------------------------------------------------------------------------"
            print "Login failed............"
            print "---------------------------------------------------------------------------"
            return

         # We've successfully authenticated, let's have some fun!
        else:
            print "---------------------------------------------------------------------------"
            print "Login succed............"
            print "---------------------------------------------------------------------------"
            return Request(url="https://www.youtube.com/playlist?list=xxxx",
               callback=self.parse_tastypage)

    def parse_tastypage(self, response):

        hxs = HtmlXPathSelector(response)

        print "---------------------------------------------------------------------------"
        print "what are you doing?"
        #print response.xpath("//tbody[@id='pl-load-more-destination']//tr[@data-title]").extract()
        # print hxs.xpath('//tr[contains(@class, "pl-video")]').extract()
        # print response.css('img').xpath('@src').extract()
        hxs = HtmlXPathSelector(response)
        images = hxs.select('//img')
        # .. do something with them
        links = hxs.select('//a/@href')

        # Yield a new request for each link we found
        for link in links:
            yield Request(url=link, callback=self.parse_page)



        print "---------------------------------------------------------------------------"

        # etc.