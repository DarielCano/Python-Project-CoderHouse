# FUNCION PARA EL REGISTRO DE USUARIOS 
def sign_in(user,password):
    
    if user.isdigit() or users=="":
        print("\n !!El nombre de usuario no es correcto!!\n")
        return
    
    if(password=="" or len(password)<9):
        print("\nLa contraseña debe contener más de 8 caracteres\n")
        return
    
    if user in users.keys():
        print("\nERROR -- El usuario ya existe")
        return
    
    print(f"\nBienvenido {user}!!!!!!")
    users[f"{user}"]=password
    return True
      
# ------------------------------------------------------------------------------------ 

#FUNCION PARA INICIO DE SESION
def login(user,password):

    if user.isdigit() or users=="":
        print("\n ERROR -- El nombre de usuario no es correcto\n")
        return
    
    if(password=="" or len(password)<9):
        print("\n ERROR -- La contraseña debe contener más de 8 caracteres\n")
        return

    if len(users)==0:
        print("\n ERROR -- No existe registro de usuarios\n")
        return "out"
    
    else:
        if user in users.keys():
            if password in users.values():
                print(f"\n Bienvenido {user}!!!!!!")
                return True
            else:
                print("\nERROR -- Las contraseñas no coinciden\n")
                return  
        else:
            print("\nERROR -- El usuario no existe\n")
            return
#-------------------------------------------------------------------------

# FUNCION PARA MOSTRAR USUARIOS 

def show_info(users):
    print("------------------------------------------------------")
    print("          Listado de usuarios          ")
    print("------------------------------------------------------")
    print(f" Nombre de usuario        |         Contraseña       ")
   
    for users_name, users_password in users.items():
        print("------------------------------------------------------")
        print(f" {users_name}                     |        {users_password}         ")


    cont = input("\nPresione Enter para continuar")
    if cont=="":
        return
# ---------------------------------------------------------------------------------------     
    
    
#FUNCION PARA LEER O ESCRIBIR ARCHIVOS

def files(file_name, action, file_users={}):
    f = open(f"./{file_name}",action)
    users = {}
    if(action == "r"):
        content = f.read()
        print(content)
        if len(content)!=0:
            eachUser= content.split(" ")
            eachUser.pop()
            for user in eachUser:
                oneUser = user.split(":")
                users[oneUser[0]] = oneUser[1]
           
            f.close()
            return users
        else: 
            users={}
            f.close()
            return users
        
    elif(action == "w"):
  
        data = ""
        for name, surname in file_users.items():
            data = data + f"{name}:{surname}" +" "
            print(data)
         
        f.write(data)
        f.close()
        return
       

#----------------------------------------------------------------------

# SECCION PRINCIPAL 


option = ""

print("\n Bienvenido a nuestro blog!!!")
users = files("users.txt","r") #leyendo archivo con posibles 

while True:
    op = ""
    print(" Sigue las intrucciones para iniciar sesión:")
    print(" --- Para INICIAR SESION presiona 1 ---")
    print(" --- Para CREAR CUENTA presiona 2 -----")
    print(" --- Para SALIR presiona 3 ------------")
    option = input("  Escriba su opción: ")
   
    if option =="3":
        break 
    
    if(option.isdigit()==False):
        print("Debe seleccionar uno de las opciones!!!\n")
        continue
     
    if(option!="1" and option!="2"):
         print("Opciones incorrectas!!!\n")
    
    if(option == "1"):
          
        if op =="3":
            break
        
        else:
            print("----------------------")
            print("---INICIO DE SESION---")
            print("----------------------")
            
            while True:
                if op == "3":
                    break
                else:
                    user = input("Escriba el nombre de usuario: ")
                    password = input("Escriba la contraseña: ")
                    res =login(user, password)
                    if(res=="out"):
                        break
                    
                    if(res):
                        while True:
                            op = input("\nPresione 4 para mostrar información de usuarios y 3 para Cerrar Sesión: ")
                        
                            if op=="3":
                                print("\n Cerrando Sesión....\n")
                                break
                                                
                            if op =="4":
                                show_info(users)
                            
                            else:
                                print("\nOpción incorrecta!!! \n")
        
    if(option == "2"):
        
        if(op == "3"):
            break
        
        else:
            print("\n----------------------")
            print("-----CREAR CUENTA-----")
            print("----------------------")
            
            while True:
                
                if op =="3":
                    break
                
                user = input("Escriba el nombre de usuario: ")
                password = input("Escriba la contraseña: ")
            
                res = sign_in(user,password)
        
                if(res):
                      
                    while True:
                        op = input("\nPresione 4 para mostrar información de usuarios y 3 para Cerrar Sesión: ")
                        
                        if op=="3":
                            print("\n Cerrando Sesión....\n")
                            break
                                                
                        if op =="4":
                            show_info(users)
                            
                        else:
                            print("\nOpción incorrecta!!! \n")

             
end = files("users.txt","w", users)  
   
print("\n Saliendo... Gracias por visitarnos!!!\n")






