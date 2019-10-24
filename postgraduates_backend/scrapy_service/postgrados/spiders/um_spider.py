import scrapy
import json
import os

class UmSpider(scrapy.Spider):
    name = "um"

    def start_requests(self):
        urls = [
            'https://fium.um.edu.uy/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.xpath('//a[contains(@href,"fium.um.edu.uy/propuesta-academica/")]/@href').extract()[-5:]
        for i in links:
            yield scrapy.Request(url='https:'+i, callback=self.getCareerInfo)

    def getCareerInfo(self, response):
        name = response.xpath('//li[@class="career"]/text()').get()
        career_name = name if name != None else ""
        # career_description = response.xpath('//div[@id="content-description"]/h2/text()').get()
        url = response.request.url
        career_url = url if url != None else ""
        # career_image_url = response.xpath('//div[@id="content-picture"]/img/@src').get() 
        with open('./postgraduates_backend/scrapy_service/postgrados/spiders/careers.json', mode='r+', encoding='utf-8') as json_file:
            careers = json.load(json_file)

            new_career = {
                'name': career_name,
                'description': "",
                'url': career_url,
                'image_url': "",
                'university': "um"
            }

            careers['careers'].append(new_career)

            json_file.seek(0)
            json.dump(careers, json_file, ensure_ascii=False)
            