import scrapy
from w3lib.html import remove_tags


class ArticleSpider(scrapy.Spider):
    name = 'theguardian'

    #Start Fucntion
    def start_requests(self):

        yield scrapy.Request('https://www.theguardian.com/international', self.parse_article)

    #In this function we try to get all articles url and then crawl all the information by calling parse function
    def parse_article(self, response):

        #loop over all url
        for url in response.xpath("//*[@data-link-name='article']/@href").getall():
            #we used this function to avoid local urls
            article_url = response.urljoin(url)
            #parse the page of that url
            yield scrapy.Request(article_url, callback=self.parse)

    def parse(self, response):

        title = response.css('title::text').get()
        url = response.request.url
        #The articles content are all in a p tag in div with class = article-body-commercial-selector
        article_list = response.xpath("//*[contains(@class, 'article-body-commercial-selector')]/p[normalize-space()]").extract()
        #remove_tags helps getting all the text in p tag in one element,
        article_list = [remove_tags(text) for text in article_list]
        #while article_list is a list,each element is a paragraph, we gonna join them by new line
        article = "<br/>".join(article_list)
        #authors names exist in address tag
        authors = response.xpath("//address[normalize-space()]//text()").getall()
        # authors names exist in label tag with attribute dateToggle
        date = response.xpath("//label[@for='dateToggle'][normalize-space()]/text()").get()

        #there are some url contain live video, so there will be no article. so we check before yield anything
        if article != "":

            yield {
                'title': title,
                'url': url,
                'article': article,
                'authors': "".join(authors),
                'date': date
            }
