class Book:
   def  __init__(self,book_id,name,author,num_pages,price):
       self.book_id = book_id
       self.book_name = name
       self.author_name = author
       self.num_pages = num_pages
       self.price = price
       
       
   def print_book_details(self):
       print("::::::::::::::::::::BOOK DETAILS::::::::::::::::: ")
       print("BOOK ID: ", self.book_id)
       print("BOOK NAME: ", self.book_name)
       print("AUTHOR NAME: ", self.author_name)
       print("NUMBER OF PAGES: ", self.num_pages)
       print("PRICE: ", self.price)
      
      
       