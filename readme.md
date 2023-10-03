API REST CON DJANGO

Es una aplicacion de inventario para una tienda o distribuidor de auto partes

Se tienen 4 tablas:
Categoria,
Producto,
Orden,
OrdenProducto

Una Categoria puede tener varios Productos
Un Producto puede tener varios OrdenesProductos
Una Orden puede tener varias OrdenesProdcuts.

Como ejemplo de Categoria se tendran los siguientes registros: autos, motos, camiones y tractores.

Como ejemplo de Producto se tendran el siguiente registro: llanta, R20, 1000 Bs, disponible si (en categoria camiones)
