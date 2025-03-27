# Creating a class for 'Product' instaces
class Product:
    # The constructor has the following 3 attributes:
    def __init__(self, name:str, quantity:int, price:float):
        self.name=name #The product's name
        self.quantity=quantity #The product's quantity in stock
        self.__price=price #The product's price (it is private, so that only the page administrators can access it)
        self.reviews = []
      
    #Defining a getter method to access the product's price:
    @property
    def price(self):
        return self.__price
    
    #Defining a setter method to set a new price for the product:
    @price.setter
    def price(self,new_price:float):
        self.__price=new_price
    
    #Defining a method to update the quantity of the product:
    def update_quantity(self,new_quantity:int):
        self.quantity=new_quantity
        
    @staticmethod
    def is_left(product):
        if product.quantity==0:
            return f"Product is sold out."
        else:
            return f"Item is in stock."

    #the next 3 is for the review class, and thar functions are explained there (and in their names) 
    def add_review(self, rating: int, comment: str):
        self.reviews.append({'rating': rating, 'comment': comment})

    def review_average(self):
        if not self.reviews:
            return 0
        return sum(review['rating'] for review in self.reviews) / len(self.reviews)

    def remove_reviews(self):
        self.reviews = []

        
    def __str__(self):
        return f"Here are the details of the product: Product name: {self.name}, quantity: {self.quantity}, price: {self.__price}€"
    
    


class Limited(Product):
    def __init__(self, name:str, quantity:int, price:float, brand:str):
        super().__init__(name, quantity, price)
        self.brand=brand
    def update_quantity(self, new_quantity:str):
        max_quant=5
        if new_quantity>5:
            self.quantity=max_quant
            return f"Cannot buy any more of: {self.name}"
        else:
            self.quantity=new_quantity
            return f"New quantity succesfully set as {new_quantity}."
    @property
    def price(self):
        return super().price
    @price.setter
    def price(self, np):
        lim_tax=1.5
        final_np=np*lim_tax
        self.__price=final_np
    
    def __str__(self):
        f"Product name: {self.name}, Product brand: {self.brand},Product price(with limited edition tax): {self.price}, Product quantity: {self.quantity}"
        