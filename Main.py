from ClassVenta import Venta

venta = Venta()

venta.set_id_venta(1)
venta.set_fecha("15/10/2014")
venta.set_cliente("Victor")

venta.agregar_producto("Producto A", 2, 50.25)  # 2 unidades de Producto A a 50.25 cada uno
venta.agregar_producto("Producto B", 1, 30.00)  # 1 unidad de Producto B a 30.00
venta.agregar_producto("Producto C", 3, 20.00)  # 3 unidades de Producto C a 20.00 cada uno

'''venta.set_productos(["Producto1", "Producto2", "Producto#"])
venta.set_total(150.75)'''

venta.agregar_producto("Producto D", 1, 40.00)

venta.mostrar_detalle()


