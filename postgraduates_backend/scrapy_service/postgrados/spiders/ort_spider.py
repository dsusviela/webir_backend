import scrapy
import json

class OrtSpider(scrapy.Spider):
    name = "ort"

    def start_requests(self):
        urls = [
            'https://www.ort.edu.uy/postgrados'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.xpath('//a[contains(@href,"/fi.ort.edu.uy")]/@href').extract()[:4] 
        for i in links:
            yield scrapy.Request(url=i, callback=self.getCareerInfo)

    def getCareerInfo(self, response):
        name = response.xpath('//div[@id="content-title"]/h1/text()').get()
        career_name = name if name != None else ""
        description = response.xpath('//div[@id="content-description"]/h2/text()').get()
        career_description = description if description != None else ""
        url = response.request.url
        career_url = url if url != None else ""
        image_url = response.xpath('//div[@id="content-picture"]/img/@src').get() 
        career_image_url = image_url if image_url != None else ""
       
        with open('./postgraduates_backend/scrapy_service/postgrados/spiders/careers.json', mode='r+', encoding='utf-8') as json_file:
            careers = json.load(json_file)

            new_career = {
                'name': career_name,
                'description': career_description,
                'url': career_url,
                'image_url': career_image_url,
                'university': "ort"
            }

            careers['careers'].append(new_career)

            json_file.seek(0)
            json.dump(careers, json_file, ensure_ascii=False)
            