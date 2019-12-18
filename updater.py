#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:29:45 2019

@author: austenwilliams
"""
import os
from file_manager_ import File_Manager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class Web_Service:
        
        def __init__(self):    
            
            self.file_manager = File_Manager()
            
        
        
#Used to locate the chromedriver path    
            
        def chrome_finder(self):
            dir_path = os.path.dirname(os.path.realpath(__file__))
            chrome = dir_path + '/chromedriver'
            return chrome
        
        

#Used to find a price for an item by webscraping the price element and returning it.
            
        def webscraper(self,site):
            service = Options()
            service.add_argument("--headless")
            service.add_argument("--window-size=1920x1080")
            driver = webdriver.Chrome(options=service,executable_path=self.chrome_finder())
            driver.get(site)
            price_element = driver.find_element_by_id("priceblock_ourprice").text
            driver.quit()
            new_price = float(price_element.strip('$'))
            return(new_price)
            
        
  
#Used to provide the text of the listboxes. It takes in an item parameter and returns the phrase to be added to the listbox          
            
        def update_phrase(self, item):
            name = self.file_manager.find_specific(item['name'])
            newest_price = self.webscraper(item['website'])
            old_pop = item['old_price'].copy().pop()
            if old_pop != newest_price :
                item['old_price'].append(item['price'])
                old_pop = item['old_price'].copy().pop()
                item['price'] = newest_price
            self.file_manager.update_file(name, item)
            if (item['price'] > old_pop) or (item['price'] < old_pop):
                return({'name':item['name'], 'phrase':f'The price of the {item["name"]} is ${newest_price}. ' + '\n'})

            else:
                return({'name': item['name'], 'phrase':f'The price of {item["name"]} is still {item["price"]}' + '\n'})



#Used to go to site directly without closing the browser.

        def site_pull_up(self,site):
            service = Service(self.chrome_finder())
            service.start()
            driver = webdriver.Remote(service.service_url)
            driver.get(site)
            
                    