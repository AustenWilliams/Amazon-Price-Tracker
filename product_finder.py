#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 02:16:32 2019

@author: austenwilliams
"""
from tkinter import Frame, Button, Label, Tk, Scrollbar, Entry, Listbox
from updater import Web_Service
from file_manager_ import File_Manager
from tkinter import messagebox


LARGE_FONT= ("Verdana", 12)

class Windows:
    
    
    def __init__(self):
    
        self.item_class = Web_Service()
        self.file_manager = File_Manager()
        
    #Initialize Main Window
    
        self.master = Tk()
        self.master.grid()
        self.master.title("Price Finder")
        
        
    #Build grid for Main window to allow for sub-window placement
    
        for r in range(6):
            self.master.rowconfigure(r, weight=1)    
        for c in range(6):
            self.master.columnconfigure(c, weight=1)
        
        
    #Top Left Window grid
    
        self.frame = Frame(self.master, bg= 'white')
        self.frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 3, sticky = 'WENS')
        
    
    #Top left window content
    
        self.question = Label(self.frame, bg='white', text= 'Would you like to check again', font=LARGE_FONT)
        self.question.pack(side='top')
        self.lower = Frame(self.frame)
        self.lower.pack(side='top')
        self.yes = Button(self.lower, text='Yes', command= self.update)
        self.no = Button(self.lower, text= 'No', command = self.close_window)
        self.yes.pack(side='left')
        self.no.pack(side='left')
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack( side = 'right', fill = 'y') 
        self.mylist = Listbox(self.frame, yscrollcommand = self.scrollbar.set ) 
        self.mylist.pack(fill='both') 
        self.scrollbar.config( command = self.mylist.yview ) 
        
        
    #Top right window grid
    
        self.frame2 = Frame(self.master, bg='white')
        self.frame2.grid(row = 0, column = 3, rowspan = 2, columnspan = 3, sticky = 'WENS')
        
    #Top right window content
    
        self.statement = Label(self.frame2, bg='white', text= 'Item List:', font=LARGE_FONT)
        self.statement.pack(side='top')
        self.lower = Frame(self.frame2)
        self.lower.pack(side='top')
        self.website = Button(self.lower, text= 'Visit Site', command= self.site_visit)
        self.website.pack(side= 'left')
        self.delete = Button(self.lower, text= 'Delete', command= self.delete)
        self.delete.pack(side='left')
        self.scrollbar = Scrollbar(self.frame2)
        self.scrollbar.pack( side = 'right', fill = 'y' ) 
        self.mylist2 = Listbox(self.frame2, yscrollcommand = self.scrollbar.set ) 
        self.mylist2.pack(fill='both') 
        self.scrollbar.config(command = self.mylist.yview ) 
        
        
    #Bottom Window grid
    
        self.frame3 = Frame(self.master, bg= 'white')
        self.frame3.grid(row = 2, column = 0, rowspan = 4, columnspan = 6, sticky = 'WENS')
        
        
    #Bottom window content
    
        self.product_name = Label(self.frame3, text='What is the name of the product:', anchor= 'e', justify= 'left') 
        self.product_site = Label(self.frame3, text='Please enter the website where you found this item:', anchor= 'e', justify= 'left')
        self.product_price = Label(self.frame3, text='What is the price of the item: ', anchor= 'e', justify= 'right') 
        self.product_name.grid(row=0, column=0, rowspan = 1,columnspan = 2) 
        self.product_site.grid(row=1, column=0, rowspan = 1,columnspan = 2)
        self.product_price.grid(row=2, column=0,rowspan = 1,columnspan = 2)
        self.product_name1 = Entry(self.frame3) 
        self.product_site1 = Entry(self.frame3)
        self.product_price1 = Entry(self.frame3)
        self.product_name1.grid(row=0, column=2, rowspan = 1 ,columnspan = 2) 
        self.product_site1.grid(row=1, column=2, rowspan = 1 ,columnspan = 2) 
        self.product_price1.grid(row=2, column=2,rowspan = 1 ,columnspan = 2)
        self.submit = Button(self.frame3, text= 'Submit', command= self.submit)
        self.submit.grid(row=2, column=6)


       
    
    # Initialize all windows
    
        self.master.geometry("800x350")
        self.master.mainloop()
    
    
    
    #Define the methods of the class here
#-----------------------------------------------------------------------------#
    
    
    
#Used for Top left window 'Yes' button command to fetch data and present in listview
    
    def update(self):
        self.mylist.delete(0,'end')
        self.mylist2.delete(0,'end')
        lists = self.file_manager.find_files()
        item_number = 0
        while item_number < len(lists):
            values = self.item_class.update_phrase(lists[item_number])
            self.mylist.insert('end', values['phrase'])
            self.mylist.pack(fill='both')
            self.mylist2.insert('end', values['name'])
            self.mylist2.pack(fill='both')
            item_number += 1
        


#Used for Top Right window 'delete' command  to delete file and selection from listview
        
    def delete(self):
        selection = self.mylist2.curselection()
        name = self.mylist2.get(selection)
        self.file_manager.delete_file(name)
        self.mylist.delete(selection)
        self.mylist2.delete(selection)
        self.mylist.pack(fill='both')
        self.mylist2.pack(fill='both')

#Used for Bottom Window submit button to get contents of the window and make a file
                
    def submit(self):
        name = self.product_name1.get()
        price = self.product_price1.get()
        site = self.product_site1.get()
        old_price = [float(price)]
        self.file_manager.create_new(name, price, old_price, site)
        self.product_name1.delete(first=0, last=100)
        self.product_price1.delete(first=0, last = 'end')
        self.product_site1.delete(first= 0, last= 'end')
        self.update()
        
#Used for 'Visit Site' button to get selection and bring up site related to selection     
    
    def site_visit(self):
        selection = self.mylist2.curselection()
        name = self.mylist2.get(selection)
        site = self.file_manager.site_return(name)
        self.item_class.site_pull_up(site)
    

    def close_window(self):
            if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
                self.frame3.destroy()
                self.frame2.destroy()
                self.frame.destroy()
                message = Label(self.master, text = 'Please close window by pressing "X" on the top left.')
                message.pack(side='top')
    
        
if __name__ == '__main__':
    Windows()
