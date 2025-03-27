import Discount
import Cart
class Payment:
    def __init__(self,payment_method:str):
        self.payment_method=payment_method
        self.amount=self.total()
        
    def total_order_amount(self):
        Discount.apply_discount()
        Discount.calculate_discount()
        
        
    def prc_pay(self):
        if self.payment_method.lower()=="credit card":
            print('Ongoing payment with credit card.')
        elif self.payment_method.lower()=="cash":
            print('Ongoing payment by cash.')
        elif self.payment_method.lower()=="debit card":
            print('Ongoing payment with debit card.')
        else:
            print("Invalid payment method.")
                