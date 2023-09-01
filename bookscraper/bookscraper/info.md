### Scrapy Project
- pip install scrapy
- pip3 install "urllib3 <=1.26.15"
- scrapy startproject bookscraper
- Create a Spider: cd spiders -> scrapy genspider bookspider books.tos
crape.com
- to run the spider -> scrapy crawl bookspider
- in spiders folder -> pip install ipythom
- open scrapy.cfg and add -> shell = ipython
- run -> scrapy shell
- connect to website -> fetch('books.toscrape.com')
- save all books to a variable -> books = response.css('classname')
- collect the 'title' of a book ->
    book = books[0]
    book.css('.titleClassname') as Sample ->
      book.css('h3 a::text').get() 
- collect the 'price' of the boo ->
    book.css('.product_price p.price_color::text').get()
- collect the 'href' link ->
    book.css('h3 a').attrib['href']
- Exit the shell 'exit', and crawl the webpage with 'bookspider.py' and then give the command on the shell "scrapy crawl bookspider"
- to get the 'next page' link -> response.css('.next a::attr(href)').get()
- to get the attribute of a class -> response.css('p.star-rating').attrib['class']
- extracting data from a table ->  table_rows = response.css('table tr')
  - table_rows[2].get()
  - table_rows[2].css('td::text').get()
- extracting text from a link with Xpath -> 
    response.xpath('//*[@id="default"]/div[1]/div/ul/li[3]/a/text()').get()
- extracting data and save them to a csv or json file ->
  - scrapy crawl bookspider -O bookdata.csv
  - scrapy crawl bookspider -O bookdata.json
