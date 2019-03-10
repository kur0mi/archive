from scrapy.spiders import Spider


class FirstSpider(Spider):
    name = "first"
    start_urls = ["https://blog.csdn.net/wbsrv/article/details/77131279"]

    def parse(self, response):
        name = response.css("p.name.csdn-tracking-statistics.tracking-click a#uid::text").extract()[0].strip()
        box = response.css("div.grade-box.clearfix dd::text").extract()
        nVisit = box[2].strip()
        nGoal = box[3].strip()
        nRank = box[4].strip()
        print("name: {}\n  nVisit: {}\n  nGoal: {}\n  nRank: {}".format(name, nVisit, nGoal, nRank))
        
        for next_page in response.css("div.recommend-item-box.recommend-box-ident.type_blog.clearfix div a::attr(href)").extract():
            yield response.follow(next_page, self.parse)

