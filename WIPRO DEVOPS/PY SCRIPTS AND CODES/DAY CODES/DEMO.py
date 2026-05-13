class ProductManagement:
    def __init__(self, product_id, product_name):
        self.product_id = product_id
        self.product_name = product_name

    def add_product(self):
        print("Product Added Successfully")

    def update_stock(self):
        print("Stock Updated")


# Class 2: PaymentManagement
class PaymentManagement:
    def __init__(self, payment_id, amount):
        self.payment_id = payment_id
        self.amount = amount

    def process_payment(self):
        print("Payment Processed")
    def refund_payment(self):
        print("Payment Refunded")


# Class 3: DeliveryExecutive (Hybrid Inheritance)
class DeliveryExecutive(ProductManagement, PaymentManagement):
    def __init__(self, product_id, product_name, payment_id, amount, executive_name, area):
        ProductManagement.__init__(self, product_id, product_name)
        PaymentManagement.__init__(self, payment_id, amount)
        self.executive_name = executive_name
        self.area = area

    def assign_order(self):
        print("Order Assigned")

    def deliver_order(self):
        print("Order Delivered")


# Class 4: SeniorDeliveryManager (Hierarchical + Multilevel)
class SeniorDeliveryManager(DeliveryExecutive):
    def __init__(self, product_id, product_name, payment_id, amount, executive_name, area, manager_name):
        super().__init__(product_id, product_name, payment_id, amount, executive_name, area)
        self.manager_name = manager_name

    def track_all_deliveries(self):
        print("Tracking All Deliveries")

    def generate_report(self):
        print("Monthly Report Generated")


# -------------------------------
# Main Execution
# -------------------------------
product_id = input("Enter Product ID: ")
product_name = input("Enter Product Name: ")
payment_id = input("Enter Payment ID: ")
amount = float(input("Enter Amount: "))
executive_name = input("Enter Delivery Executive Name: ")
area = input("Enter Area: ")
manager_name = input("Enter Manager Name: ")
 
manager = SeniorDeliveryManager(
    product_id,
    product_name,
    payment_id,
    amount,
    executive_name,
    area,
    manager_name
)
# Calling methods
manager.add_product()
manager.update_stock()
manager.process_payment()
manager.assign_order()
manager.deliver_order()
manager.track_all_deliveries()
manager.generate_report()