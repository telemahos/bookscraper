import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

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
            relative_url = book.css('h3 a::attr(href)').get()
            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url
            # load the next page and re-run the parse method
            yield response.follow(book_url, callback = self.parse_book_page)
                    
        next_page = response.css('li.next a ::attr(href)').get()
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
        table_rows = response.css('table tr')
        
        yield {
            'url': response.url,
            'title': response.css('.product_main h1::text').get(),
            'product_type': table_rows[1].css('td ::text').get(),
            'price_excl_tax': table_rows[2].css('td ::text').get(),
            'price_incl_tax': table_rows[3].css('td ::text').get(),
            'tax': table_rows[4].css('td ::text').get(),
            'availability': table_rows[5].css('td ::text').get(),
            'num_reviews': table_rows[6].css('td ::text').get(),
            'stars': response.css('p.star-rating').attrib['class'],
            'category': response.xpath('//*[@id="default"]/div[1]/div/ul/li[3]/a/text()').get(),
            'description': response.xpath('//*[@id="content_inner"]/article/p/text()').get(),
            'price': response.css('p.price_color ::text').get(),
        }
