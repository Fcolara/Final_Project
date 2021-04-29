# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:22:16 2021

@author: nathan
"""

import scrapy

class Airfoil(scrapy.Spider):
    name = 'airfoil'
    start_urls = ['http://airfoiltools.com/search/airfoils']
    
    def parse(self, response):
        #cycle through all availible airfoils
        
        for page_url in response.css('a[href^="/airfoil/details?airfoil="]::attr(href)').getall():
            page_url = response.urljoin(page_url)
            yield scrapy.Request(url=page_url, callback=self.parse)
        
        #finds Airfoil name
        title = response.css('h1::text').extract()
        
        #finds Cl/Cd for different Reynolds numbers
        for tr in response.css('table[class="polar"]'):x=(tr.css('td[class]::text').extract())
        index = 0
        clcd_N9 = list()
        clcd_N5 = list()
        for val in x: 
            if index in [3,13,23,33,43]:
                clcd_N9.append(val.split(' ')[0])
            if index in [8,18,28,38,48]:
                clcd_N5.append(val.split(' ')[0])
            index = index+1
        
        #finds max thickness and max camber
        details = response.css('table[class="details"]').css('td[class]::text').extract()
        thickness = details[3].split(' ')[2]
        camber = details[4].split(' ')[2]
        
        yield {'title' : title, 
              'Cl/Cd_Re50K_N9' : clcd_N9[0],
              'Cl/Cd_Re50K_N5' : clcd_N5[0],
              'Cl/Cd_Re100K_N9' : clcd_N9[1],
              'Cl/Cd_Re100K_N5' : clcd_N5[1],
              'Cl/Cd_Re200K_N9' : clcd_N9[2],
              'Cl/Cd_Re200K_N5' : clcd_N5[2],
              'Cl/Cd_Re500K_N9' : clcd_N9[3],
              'Cl/Cd_Re500K_N5' : clcd_N5[3],
              'Cl/Cd_Re1000K_N9' : clcd_N9[4],
              'Cl/Cd_Re1000K_N5' : clcd_N5[4],
              'max_thickness' : thickness,
              'max_camber' : camber}
        


