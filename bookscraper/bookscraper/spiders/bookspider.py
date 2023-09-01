import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        books = response.css('article.product_pod')
        
        # look only on product catalogue
        # for book in books:
        #     yield{
        #         'name' : book.css('h3 a::text').get(),
        #         'price' : book.css('.product_price p.price_color::text').get(),
        #         'url' : book.css('h3 a').attrib['href'],
        #     }
        
        # visiting and scraping all product pages
        for book in books:
            # click on the next page link to load the next page   
            relative_url = response.css('h3 a::attr(href)').get()
            if 'catalogue/' in next_page:
                next_page_url = 'http://books.toscrape.com/' + relative_url
            else:
                next_page_url = 'http://books.toscrape.com/catalogue/' + relative_url
            # load the next page and re-run the parse method
            yield response.follow(next_page_url, callback = self.parse_book_page)
                    
        
        # a. Repeat until the end of pages
        # b. There is some issues with part of the URL "sometimes catalogue/ is missing" 
        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'http://books.toscrape.com/' + next_page
            else:
                next_page_url = 'http://books.toscrape.com/catalogue/' + next_page
            # load the next page and re-run the parse method
            yield response.follow(next_page_url, callback = self.parse)
    
    
    
    def parse_book_page(self, response):
        pass
