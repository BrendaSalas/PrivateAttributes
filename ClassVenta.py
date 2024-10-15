class Venta:

    __id_venta = None
    __fecha = None
    __cliente = None
    __productos = None  # Lista de productos vendidos
    __total = None

    # Getters para acceder a los atributos privados

    def __init__(self):
        self.__productos = {}
        self.__total = 0.0

    def get_id_venta(self):
        return self.__id_venta

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total


    # Setters para modificar los atributos privados

    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_productos(self, productos):
        self.__productos = productos

    def set_total(self, total):
        self.__total = total

    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_cliente(self, cliente):
        self.__cliente = cliente

    # Método para mostrar los detalles de la venta

    def agregar_producto(self, producto, cantidad, precio_unitario):
        if len(self.__productos) < 3 and producto not in self.__productos:
            self.__productos[producto] = {
                'cantidad': cantidad,
                'precio_unitario': precio_unitario
            }
            self.calcular_total()
        else:
            print("Solo puedes agregar hasta 3 productos o el producto ya fue agregado.")

    # Método para calcular el total de la venta
    def calcular_total(self):
        self.__total = sum(
            prod['cantidad'] * prod['precio_unitario'] for prod in self.__productos.values()
        )

    def mostrar_detalle(self):
        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print(f"Productos: {', '.join(self.__productos)}")
        for producto, detalles in self.__productos.items():
            print(f"  - {producto}: {detalles['cantidad']} unidades a ${detalles['precio_unitario']:.2f} cada una")
        print(f"Total: ${self.__total:.2f}")