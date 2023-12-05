from typing import List

class Client:
    def __init__(self,name:str, surname:str, age:int, email:str, cart:List[str] = [], wishList:List[str] = []):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.cart = cart
        self.wishList = wishList
        
        
    def __str__(self):
        return f"Datos del cliente:\n - Nombre y apellidos: {self.name} {self.surname}\n - Email: {self.email}\n - Carrito: {self.cart}\n -Lista de deseos: {self.wishList}"
    
     
    def udpdateEmail(self,newEmail):
        self.email=newEmail
    
    def getCart(self):
        return self.cart
    
    
    def getWishList(self):
        return self.wishList
    
    def addItemCart(self, prod):
        self.cart.append(prod)
        
        
    def addItemWishList(self, prod):
        self.wishList.append(prod)
        
    def getCantCart(self):
        return len(self.cart)
        
    




