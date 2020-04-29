Class acting as the basket
class Basket:
    def __init__(self):
        self.items=dict()
        
        #Class that will be handling the individual products
class Product:
    def __init__(self,SKU,name,description,seller,price,currency):
        self.SKU=SKU
        self.name=name
        self.description=description
        self.seller=seller
        self.price=price
        self.currency=currency

    def details(self):
        print('SKU\t\t: ',self.SKU)
        print('Name\t\t: ',self.name)
        print('Description\t: ',self.description)
        print('Seller\t\t: ',self.seller)
        print('Price\t\t: ',self.price)
        print('Currency\t: ',self.currency)
       

b1=Basket()
b1.items['Item1']='item1'
print(b1.items)

p=Product(121234,'Ipad Air','Product with extra details','Ali express',123.12,'$')
p.details()
