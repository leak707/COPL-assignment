import Product
class Cart:
    def __init__(self, items:list):
        self._items=[]

    @property
    def items(self):
        return self._items

    def add_items(self, new_item:Product):
        self._items.append(new_item)

    def remove_items(self, del_item):
        if del_item in self.__items:
            self.__items.remove(del_item)
        else:
            print('Item not found.')

    def upd_quantity(self,new_nr,prod):
        for i in self._items:
            if i.name==prod:
                i.update_quantity(new_nr)
                break
            else:
                print('Product not found.')
    def total_price(self):
        prices=[]
        for i in self.__items:
            prices.append(i.price)
        return sum(prices)

    def __str__(self):
        return f"The cart contains the following items: {self._items}"
