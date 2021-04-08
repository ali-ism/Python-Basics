class Flower:
    def __init__(self,name,nbpetals,price):
        self._name = str(name)
        self._nbpetals = int(nbpetals)
        self._price = float(price)
        
    def set_name(self,name):
        self._name = name
    
    def set_nbpetals(self,nbpetals):
        self._nbpetals = int(nbpetals)
        
    def set_price(self,price):
        self._price = price
        
    def get_string(self):
        print(f"This flower is a {self._name} with {self._nbpetals} petals and it costs {self._price} dollars.")

flower1 = Flower('tulip',5,30)
flower1.get_string()
flower1.set_name('Rose')
flower1.set_nbpetals(15)
flower1.set_price(50)
flower1.get_string()