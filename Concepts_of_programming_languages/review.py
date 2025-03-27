from Product import Product

class Review:
    def __init__(self):
        self.products = {}  # Dictionary to store products by name

    def add_product(self, product: Product): #this adds a product to the review system
        self.products[product.name] = product

    def add_review(self, product_name: str, rating: int, comment: str): #this will add a review to a product if the product exists
        if product_name in self.products:
            self.products[product_name].add_review(rating, comment)
        else:
            print(f"Product '{product_name}' not found.")

    def remove_review(self, product_name: str): # this removes every signle review from a product if the product exists
        if product_name in self.products:
            self.products[product_name].remove_reviews()
        else:
            print(f"Product '{product_name}' not found.")

    def review_average(self, product_name: str): # this will calculate the average review rating for a product (again, if the products exists)
        if product_name in self.products:
            return self.products[product_name].review_average()
        else:
            print(f"Product '{product_name}' not found.")
            return 0

