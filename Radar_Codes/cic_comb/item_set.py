class ItemSet:
   def  __init__(self,id,word,freq): ### __init__ is a constructor of class
       self.id = int(id) #int
       self.word = word #string --> array of characters
       self.freq = len(freq) #int