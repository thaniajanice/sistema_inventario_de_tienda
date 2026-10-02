import mysql.connector

conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="inventario_tienda"
)

def create():
    while True:
        try:

            print("-------Agregar -------")
            print("Ingrese los siguientes datos")
            name_p=input("Nombre del producto: ")
            print("--------------------------")
            lista=["Technology (Tecnologia) ","Food (Alimentos)","Clothing (Ropa)"]
            for listas in lista:
                print(listas)
            category_p=input("Categoria del producto: ")
            print("--------------------------")
            stock_p= int(input("Cantidad disponnible: "))
            print("--------------------------")
            price_p= float(input("Precio: Q"))
            print("--------------------------")
            supplier_p=input("Proveedor/a: ")
            break
        except ValueError:
            print("--- ERROR ---")

    if conexion.is_connected():
        cursor=conexion.cursor()
        query="INSERT INTO inventario (productName,category,stock,price,supplier) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(query,(name_p,category_p,stock_p,price_p,supplier_p))
        conexion.commit()
        print("Se guardó exitosamente")

        print(f"El nùmero de ID: {cursor.lastrowid}")


def read():
    print("-------Revisar registros -------")
    if conexion.is_connected():
        cursor=conexion.cursor()
        query="SELECT * FROM inventario"
        cursor.execute(query,)
        datos=cursor.fetchall()
        for filas in datos:
            print(filas)

def update():
    print("-----------ACTUALIZAR ----------")
    id=int(input("Ingrese el número de ID: "))
    if conexion.is_connected():
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM inventario WHERE idinventario = %s",(id,))
        inv=cursor.fetchall()
        for listas in inv:
            print(listas)

        if inv:
            print("PRODUCTO ENCONTRADO")
            print("--------Ingrese los nuevos datos---------")
            new_name=input("Nombre del producto: ")
            print("----------------------")
            a=["Technology (tecnologia)","Food (alimento)","Closthing (Ropa)"]
            for b in a:
                print(b)
            new_cate=input("Categoría: ")
            print("----------------------")
            new_stock=int(input("Numero de existencia: "))
            print("----------------------")
            new_price=float(input("Precio: "))
            print("----------------------")
            new_supplier=input("Proveedor/a: ")


        else:
            print("Dato no encontrado")

        query="""
            UPDATE inventario
            SET productName = %s,
                category = %s,
                stock = %s,
                price = %s,
                supplier = %s

            WHERE idinventario=%s


"""
        cursor.execute(query,(new_name,new_cate,new_stock,new_price,new_supplier,id))
        conexion.commit()
        print("SE GUARDO CORRECTAMENTE")


def delete():
    print("--------ELIMINAR---------")
    id=int(input("Ingrese el número de ID: "))
    if conexion.is_connected():
        cursor=conexion.cursor()
        query="DELETE FROM inventario WHERE idinventario = %s "
        cursor.execute(query,(id,))
        conexion.commit()
        print("Se eliminó correctamente")


        

def menu():
    print("--- BIENVENIDO ---")
    while True:
        try:
          
          lista=["1. Registrar producto","2. Consultar inventario","3. Actualizar dato","4. Eliminar registros"]
          for listas in lista:
              print(listas)

          desi=int(input("Ingrese el número de opción: "))
          break
        except ValueError:
            print("----ERROR----")

    if desi == 1:
        create()
    elif desi == 2:
        read()
    elif desi ==3:
        update()
    elif desi == 4:
        delete()
    else:
        print("Esta no es una opcion")


menu()