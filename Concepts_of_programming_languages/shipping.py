from Order import Order

class Shipping:
    def __init__(self, tracking_id, status, estimated_time, courier_code):
        self.tracking_id = tracking_id
        self.status = status
        self.estimated_time = estimated_time
        self._courier_code = courier_code
    
    def shipping_status(self):
        
    
    @classmethod
    def shipping_type(cls, order: Order):
        
    
    @property
    def courier_information(self):
        