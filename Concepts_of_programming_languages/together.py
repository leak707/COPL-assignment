"""
Checklist 1:
 --- 9 classes
 --- 15 methods
 --- 9 encapsulated attributes (getters and setters)
 --- 9 private, protected, public attributes (3 each)
 --- 3 __str__ methods

Checklist 2:
9 Static / class methods, class attributes (3 each)
9 operator overloading
3 derived classes, 6 overridden methods
"""

class User():
    user_counter = 0
    def __init__(self, firstname, lastname, email, username, password):
        self._firstname = firstname
        self._lastname = lastname
        self.__email = email
        self.__username = username
        self.__password = password
        User.user_counter += 1

    def __str__(self):
        return f"Username: {self.username}, Password: {self.password}"
    
    def __repr__(self):
        return f"firstname={self.firstname}, lastname={self.lastname}, email={self._email}, username={self.username}, password={self.password})"
    
    @classmethod
    def register(cls):
        firstname = input("First name: ").strip()
        lastname = input("Last name: ").strip()
        email = input("Email: ").strip()
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        return cls(firstname, lastname, email, username, password)

    @classmethod
    def login(cls):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        return cls(username, password)
    
    @property
    def email(self):
        return self.__email
    
    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @email.setter
    def email(self, is_valid_email):
        if not is_valid_email:
           raise ValueError("Email is not valid") 
        self.__email = is_valid_email
    
    @username.setter
    def username(self, is_valid_username):
        if not is_valid_username:
           raise ValueError("Username is not valid") 
        self.__username = is_valid_username

    @password.setter
    def password(self, is_valid_password):
        if not is_valid_password:
           raise ValueError("Password is not valid") 
        self.__password = is_valid_password

    def add_review(self, product, rating, comment):
        product.reviews.append(Review(self, rating, comment))

class Review():
    def __init__(self, username, rating, comment):
        self.username = username
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"User: {self.user}, Rating: {self.rating}, Comment: {self.comment}"

class Product():
    def __init__(self, id, price, quantity):
        self.id = id
        self._price = price
        self.quantity = quantity
        self.reviews = []

    def __str__(self):
        return f"Product id: {self.id}, Product price: {self.price}, Product quantity: {self.quantity}"
    
    def __repr__(self):
        return f"Product id: {self.id}, Product price: {self.price}, Product quantity: {self.quantity}"

    @property
    def price(self):
        return self._price
    
    @property
    def number_of_reviews(self):
        return len(self.reviews)
    
    @property
    def average_rating(self):
        if not self.reviews:
            return 0
        return sum(review.rating for review in self.reviews) / len(self.reviews)
     
    @price.setter
    def price(self, new_price:float):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.price = new_price

    @staticmethod
    def in_stock(product):
        if product.quantity == 0:
            return f"Product is sold out."
        else:
            return f"Item is in stock."
    
    def add_to_cart(self):
        Cart.add_item(self)

class Electronics(Product):
    def __init__(self, id, name, price, quantity, brand, model):
        super().__init__(id, name, price, quantity)
        self.brand = brand
        self.model = model

    @property
    def brand(self):
        return self.brand
    
    @property
    def model(self):
        return self.model
    
    @brand.setter
    def brand(self, new_brand):
        if new_brand == "":
            raise ValueError("Brand cannot be empty")
        self.brand = new_brand

    @model.setter
    def model(self, new_model):
        if new_model == "":
            raise ValueError("Model cannot be empty")
        self.model = new_model
    
    def __str__(self):
        return f"Product brand: {self.brand}, Product model: {self.model}"
    
    def __repr__(self):
        return f"Product brand: {self.brand}, Product model: {self.model}"
    
class Furniture(Product):
    def __init__(self, id, name, price, quantity, dimensions):
        super().__init__(id, name, price, quantity)
        self.dimensions = dimensions

    @property
    def dimensions(self):
        return self.dimensions
    
    @dimensions.setter
    def dimensions(self, new_dimensions):
        if new_dimensions == "":
            raise ValueError("Dimensions cannot be empty")
        self.dimensions = new_dimensions
    
    def __str__(self):
        return f"Product dimensions: {self.dimensions}"
    
    def __repr__(self):
        return f"Product dimensions: {self.dimensions}"
    
class Clothing(Product):
    def __init__(self, id, name, price, quantity, size):
        super().__init__(id, name, price, quantity)
        self.size = size

    @property
    def size(self):
        return self.size
    
    @size.setter
    def size(self, new_size):
        if new_size == "":
            raise ValueError("Size cannot be empty")
        self.size = new_size

    def __str__(self):
        return f"Product size: {self.size}"
    
    def __repr__(self):
        return f"Product size: {self.size}"

class CartItem(Product):
    def __init__(self, id, name, price, quantity):
        super().__init__(id, name, price, 0)
        self.quantity = quantity

    def __str__(self):
        return f"Product id: {self.id}, Product name: {self.name}, Product price: {self.price}, Product quantity: {self.quantity}"
    
    def __repr__(self):
        return f"Product id: {self.id}, Product name: {self.name}, Product price: {self.price}, Product quantity: {self.quantity}"
    
    @property
    def quantity(self):
        return self.quantity
    
    @quantity.setter
    def quantity(self, new_quantity:int):
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = new_quantity

    def add_quantity(self):
        self.quantity += 1

    def subtract_quantity(self):
        self.quantity -= 1

    def remove_from_cart(self):
        Cart.remove_items(self)

class Cart:
    def __init__(self, items:list):
        self._items = []

    def __str__(self):
        return f"Items: {self._items}, Total: {self.total}"
    
    def __repr__(self):
        return f"Items: {self._items}, Total: {self.total}"
    
    @property
    def items(self):
        return self._items
    
    @property
    def total(self):
        return sum(item.price * item.quantity for item in self._items)
    
    @total.setter
    def total(self, new_total):
        if new_total < 0:
            raise ValueError("Total cannot be negative")
        self.total = new_total
    
    def checkout(self):
        print("Thank you for your purchase!")

    def add_item(self, item):
        self._items.append(item)

class CreditCard():
    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.__cvv = cvv

    @property
    def card_number(self):
        return self._card_number
    
    @card_number.setter
    def card_number(self, new_card_number):
        if new_card_number.length != 16:
            raise ValueError("Card number can only be 16 digits")
        self._card_number = new_card_number
    
    @property
    def cvv(self):
        return self.__cvv
    
    @cvv.setter
    def cvv(self, new_cvv):
        if new_cvv.length != 3:
            raise ValueError("CVV can only be 3 digits")
        self.__cvv = new_cvv

    def __str__(self):
        return f"Card number: {self.card_number}, Expiration date: {self.expiration_date}, CVV: {self.cvv}"

    def __repr__(self):
        return f"Card number: {self.card_number}, Expiration date: {self.expiration_date}, CVV: {self.cvv}"

class Order():
    shipping_method = "Standard Shipping"
    def __init__(self, id, products, total, status):
        self.id = id
        self.products = products
        self.total = total
        self.status = status

    def __str__(self):
        return f"Products: {self.products}, Total: {self.total}, Status: {self.status}, Shipping method: {self.shipping_method}"
    
    def __repr__(self):
        return f"Products: {self.products}, Total: {self.total}, Status: {self.status}, Shipping method: {self.shipping_method}"


user_cart = Cart([])
new_product = Product(1, 15, 1)
print(new_product)
user_cart.add_item(new_product)
print(user_cart)