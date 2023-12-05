from packages.cliente import Client

cliente = Client("Dari","Cano", 31, "dariel@dariel.com",["audifonos"," laptop Acer"], ["Iphone15","Mancuernas gym"])

#LLAMADA AL METODO __str__
print(cliente)

print("------------------------------------------------------")

##EDITAR EMAIL
#cliente.udpdateEmail("darielitocano@gmail.com")
#print(cliente)

##PRODUCTOS DEL CARRITO
#cartProd = cliente. getCart()
#print(cartProd)

##PRODUCTOS DE LA LISTA DE DESEOS
#wishProd = cliente.getWishList()
#print(wishProd)

##AGREGAR PRODUCTOS AL CARRITO DEL CLIENTE
#cliente.addItemCart("jean skinny")
#cartProd = cliente. getCart()
#print(cartProd)


##AGREGAR PRODUCTO A LA LISTA DE DESEOS
#cliente.addItemWishList("Bocina")
#wishProd = cliente.getWishList()
#print(wishProd)

##CANTIDAD TOTAL DE PRODUCTOS DEL CARRITO DEL CLIENTE
#cantProd = cliente.getCantCart()
#print(cantProd)