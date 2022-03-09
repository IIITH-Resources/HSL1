import scrapy
import csv

with open("/Users/maharnavsinghal/Library/Mobile Documents/com~apple~CloudDocs/Semester 1/HSL 1/Working with newspaper articles/toi.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["url","title","date","text"])

class ToiSpider(scrapy.Spider):
    name = 'toi'
    allowed_domains = ['timesofindia.indiatimes.com']
    with open("/Users/maharnavsinghal/Library/Mobile Documents/com~apple~CloudDocs/Semester 1/HSL 1/Working with newspaper articles/urls.txt", "r") as f:
        all_urls = [url.strip() for url in f.read().split("\n")]
    start_urls = all_urls
    
    def parse(self, response):
        url = response.url
        title = response.css('h1._1Y-96 span::text').get()
        date = response.css('div.yYIu-.byline span::text').get()
        text = response.css('div._3YYSt.clearfix ::text').getall()
        
        with open("/Users/maharnavsinghal/Library/Mobile Documents/com~apple~CloudDocs/Semester 1/HSL 1/Working with newspaper articles/toi.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([url,title,date,text])
        
        print('\n\n')
        print(url,title,date)