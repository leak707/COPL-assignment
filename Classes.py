import datetime

class User():
    users = []

    def __init__(self, user_id, firstname, lastname, email, password):
        self.__user_id = user_id
        self._firstname = firstname
        self._lastname = lastname
        self.__email = email
        self.__password = password

    def __str__(self):
        return f"firstname={self.firstname}, lastname={self.lastname}, email={self._email}, username={self.username}, password={self.password})"
    
    def __repr__(self):
        return f"User(firstname={self.firstname}, lastname={self.lastname}, email={self._email}, username={self.username}, password={self.password})"
    
    # Getters
    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def firstname(self):
        return self._firstname
    
    @property
    def lastname(self):
        return self._lastname
    
    @property
    def email(self):
        return self.__email
    
    # Setters
    @firstname.setter
    def name(self, new_name):
        if len(new_name) > 0:
            self._firstname = new_name
        else:
            raise ValueError("Name cannot be empty!")
        
    @lastname.setter
    def name(self, new_name):
        if len(new_name) > 0:
            self._lastname = new_name
        else:
            raise ValueError("Name cannot be empty!")
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self.__email = new_email
        else:
            raise ValueError("Invalid email address!")

    def verify_password(self, password):
        return self.__password == password
    
    def change_password(self, old_password, new_password):
        if self.verify_password(old_password):
            self.__password = new_password
            return "Password updated successfully!"
        return "Incorrect old password!"

    @classmethod
    def register(cls, name, email, password):
        user_id = len(cls.users) + 1  # Simple auto-incremented user_id
        new_user = cls(user_id, name, email, password)
        cls.users.append(new_user)
        return new_user

    @classmethod
    def login(cls, email, password):
        for user in cls.users:
            if user.email == email and user.verify_password(password):
                return f"Login successful! Welcome, {user.name}."
        return "Invalid email or password!"

class Review():
    def __init__(self, user, rating, comment):
        self.user = user
        self.rating = max(1, min(5, rating))  # Ensures rating is between 1-5
        self.comment = comment

    def __str__(self):
        return f"{self.user.firstname} rated {self.rating}/5 - {self.comment}"

class Product():
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__reviews = []

    def __str__(self):
        return f"Product id: {self.id}, Product price: {self.price}, Product quantity: {self.quantity}"
    
    def __repr__(self):
        return f"Product id: {self.id}, Product price: {self.price}, Product quantity: {self.quantity}"

    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @property
    def stock(self):
        return self.__stock
    
    @property
    def reviews(self):
        return self.__reviews
     
    @name.setter
    def name(self, new_name):
        if new_name.strip():
            self.__name = new_name
        else:
            raise ValueError("Product name cannot be empty!")

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            raise ValueError("Price must be greater than 0!")

    @stock.setter
    def stock(self, new_stock):
        if new_stock >= 0:
            self.__stock = new_stock
        else:
            raise ValueError("Stock cannot be negative!")

    def add_review(self, user, rating, comment=""):
        review = Review(user, rating, comment)
        self.__reviews.append(review)

    @property
    def num_reviews(self):
        return len(self.__reviews)

    @property
    def average_rating(self):
        if not self.__reviews:
            return 0
        total_rating = sum(review.rating for review in self.__reviews)
        return round(total_rating / self.num_reviews, 2)

    def update_stock(self, quantity):
        if self.__stock >= quantity:
            self.__stock -= quantity
            return True
        return False

    @staticmethod
    def in_stock(stock):
        return stock > 0 

class Electronics(Product):
    electronics_counter = 0

    def __init__(self, product_id, name, price, stock, brand, warranty_years):
        super().__init__(product_id, name, price, stock)
        self.__brand = brand
        self.__warranty_years = warranty_years  # Warranty period in years
        Electronics.electronics_counter += 1

    # Getters
    @property
    def brand(self):
        return self.__brand

    @property
    def warranty_years(self):
        return self.__warranty_years

    # Setters
    @brand.setter
    def brand(self, new_brand):
        if new_brand.strip():
            self.__brand = new_brand
        else:
            raise ValueError("Brand name cannot be empty!")

    @warranty_years.setter
    def warranty_years(self, years):
        if years >= 0:
            self.__warranty_years = years
        else:
            raise ValueError("Warranty years cannot be negative!")

    def __str__(self):
        return f"{super().__str__()} | Brand: {self.__brand}, Warranty: {self.__warranty_years} years"


class Furniture(Product):
    furniture_counter = 0

    def __init__(self, product_id, name, price, stock, material, dimensions):
        super().__init__(product_id, name, price, stock)
        self.__material = material
        self.__dimensions = dimensions  # Tuple (length, width, height)
        Furniture.furniture_counter += 1

    @property
    def material(self):
        return self.__material

    @property
    def dimensions(self):
        return self.__dimensions

    @material.setter
    def material(self, new_material):
        if new_material.strip():
            self.__material = new_material
        else:
            raise ValueError("Material cannot be empty!")

    @dimensions.setter
    def dimensions(self, new_dimensions):
        if isinstance(new_dimensions, tuple) and len(new_dimensions) == 3:
            self.__dimensions = new_dimensions
        else:
            raise ValueError("Dimensions must be a tuple (length, width, height)!")

    def __str__(self):
        return f"{super().__str__()} | Material: {self.__material}, Dimensions: {self.__dimensions}"


class Clothing(Product):
    clothing_counter = 0

    def __init__(self, product_id, name, price, stock, size, fabric):
        super().__init__(product_id, name, price, stock)
        self.__size = size
        self.__fabric = fabric
        Clothing.clothing_counter += 1

    @property
    def size(self):
        return self.__size

    @property
    def fabric(self):
        return self.__fabric

    @size.setter
    def size(self, new_size):
        if new_size.strip():
            self.__size = new_size
        else:
            raise ValueError("Size cannot be empty!")

    @fabric.setter
    def fabric(self, new_fabric):
        if new_fabric.strip():
            self.__fabric = new_fabric
        else:
            raise ValueError("Fabric cannot be empty!")

    def __str__(self):
        return f"{super().__str__()} | Size: {self.__size}, Fabric: {self.__fabric}"

class Cart:
    def __init__(self, user):
        self.user = user
        self.items = {}  # Dictionary to store products and their quantities

    def add_product(self, product, quantity=1):
        if product.stock >= quantity:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
        else:
            raise ValueError(f"Not enough stock for {product.name}!")

    def remove_product(self, product, quantity=1):
        if product in self.items:
            if self.items[product] > quantity:
                self.items[product] -= quantity
            else:
                del self.items[product]  # Remove product if quantity is 0
        else:
            raise ValueError("Product not in cart!")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def checkout(self):
        if not self.items:
            raise ValueError("Cart is empty. Add items before checkout!")

        new_order = Order(self.user, self.items, self.calculate_total()) # Create an order

        # Reduce stock for each product
        for product, quantity in self.items.items():
            product.update_stock(quantity)

        self.items.clear() # Clear the cart

        return new_order

    def __str__(self):
        cart_items = "\n".join([f"{product.name} x{quantity}" for product, quantity in self.items.items()])
        return f"Cart for {self.user.name}:\n{cart_items}\nTotal: ${self.calculate_total():.2f}"

class Order:
    order_count = 1

    def __init__(self, user, items, total_price):
        self.order_id = Order.order_count
        self.user = user
        self.items = items  # Stores products with quantities
        self.total_price = total_price
        self.order_date = datetime.datetime.now()
        self.status = "Pending"
        Order.order_count += 1

    def update_status(self, new_status):
        valid_statuses = ["Pending", "Shipped", "Delivered", "Cancelled"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError("Invalid order status!")

    def __str__(self):
        item_list = "\n".join([f"{product.name} x{quantity}" for product, quantity in self.items.items()])
        return (f"Order #{self.order_id} for {self.user.name}:\n"
                f"{item_list}\nTotal: ${self.total_price:.2f}\n"
                f"Status: {self.status} | Date: {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}")


# Example Usage
user1 = User.register("Alice", "alice@example.com", "secure123")
user2 = User.register("Bob", "bob@example.com", "mypassword")

# Login Attempts
print(User.login("alice@example.com", "secure123"))  # Output: Login successful! Welcome, Alice.
print(User.login("bob@example.com", "wrongpass"))   # Output: Invalid email or password!

product1 = Product(101, "Laptop", 1200, 10)

# Adding Reviews
product1.add_review(user1, 5, "Amazing product!")
product1.add_review(user2, 4, "Great performance, but a bit expensive.")

# Displaying Product Info
print(product1)  # Laptop - $1200, Stock: 10, Rating: 4.5/5 (2 reviews)

# Stock Management
print(Product.in_stock(product1.stock))  # True
product1.update_stock(3)
print(product1.stock)  # 7

# Example Usage
laptop = Electronics(201, "Gaming Laptop", 1500, 5, "Asus", 2)
sofa = Furniture(301, "Leather Sofa", 700, 3, "Leather", (80, 35, 40))
tshirt = Clothing(401, "Graphic T-Shirt", 25, 20, "M", "Cotton")

# Adding Reviews
laptop.add_review(user1, 5, "Super fast and great for gaming!")
sofa.add_review(user2, 4, "Comfortable, but a bit expensive.")

# Displaying Product Info
print(laptop)  # Gaming Laptop - $1500, Stock: 5, Rating: 5.0/5 (1 reviews) | Brand: Asus, Warranty: 2 years
print(sofa)    # Leather Sofa - $700, Stock: 3, Rating: 4.0/5 (1 reviews) | Material: Leather, Dimensions: (80, 35, 40)
print(tshirt)  # Graphic T-Shirt - $25, Stock: 20, Rating: 0/5 (0 reviews) | Size: M, Fabric: Cotton

# Example Usage
cart = Cart(user1)
cart.add_product(laptop, 1)
cart.add_product(tshirt, 2)

print(cart)  # Shows items in cart with total price

order = cart.checkout()  # Creates an order and clears the cart
print(order)  # Displays order details
