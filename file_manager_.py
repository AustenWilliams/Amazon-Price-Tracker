#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 00:07:32 2019

@author: austenwilliams
"""

import os
import shelve

#Class for management of shelve module files.

class File_Manager:
    
    
    
#this function is used to find specific files within the local directory given a "name" parameter
#See --> "update_phrase" function in 'updater' module
    
    def find_specific(self, name):
        title = name.replace(' ','')
        for file in os.listdir():
            if file.startswith(title):
                new_file = file[:-3]
                return(new_file)
                
                
   
#This functionis used to open a database .db file and return the dictionary of that item
#See --> 'find_files' below
                 
    def open_file(self, file):
        with shelve.open(file) as database:
            item = database['key']
        return(item)
        
            
    
#Used to update the shelve .db file with the new data of that specific product
#See --> "update_phrase" function in 'updater' module

    def update_file(self,title, n):
        file = self.find_specific(title)
        with shelve.open(file, 'w') as database:
            database['key'] ={
                    'name': n['name'],
                    'price': n['price'],
                    'old_price': n['old_price'],
                    'website': n['website']}
            
            
    
#Used to find all .db files in the local directory
#See --> "update" function in 'product_finder' module
    
    def find_files(self):
        items = list()
        for file in os.listdir():
            if file.endswith("1.db"):
                new_file = file[:-3]
                item_list = self.open_file(new_file)
                items.append(item_list)
        return items
    
    
    
#Used to delete file passed in from name parameter from the local directory
#See --> "delete" function in 'product_finder' module
            
    def delete_file(self,name):
        title = name.replace(' ','')
        for file in os.listdir():
            if file.startswith(title):
                os.remove(file)
                
                
       
#Used to create new .db database file for new product 
#Passes in parameters created when user selects submit
#See --> "submit" function in 'product_finder' module
                
    def create_new(self, name, price, old_price, site):
        title = name.replace(' ','') + '1'
        with shelve.open(title) as database:
            database['key'] ={
                        'name': str(name),
                        'price': float(price),
                        'old_price': old_price,
                        'website': str(site)}
            
            
    
#Used to return the website of a specific product passed in by a name parameter
#It locates the file in the local directory and returns the website
#See --> "site_visit" function in 'product_finder' module
            
    def site_return(self,name):
        title = name.replace(' ','')
        for file in os.listdir():
            if file.startswith(title):
                new_file = file[:-3]
                with shelve.open(new_file) as database:
                    item = database['key']
                    site = item['website']
                return(site)