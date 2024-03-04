# Clase externa
from pizza import Pizza

# a. Mostrar los valores de los atributos de clase sin crear una instancia
print(f"Precio de las pizzas: {Pizza.precio}")
print(f"El tamaño de las pizzas: {Pizza.tamaño}")

# b. Validar si "salsa de tomate" se encuentra en una lista específica sin crear una instancia
print("¿'salsa de tomate' es un ingrediente válido?:", Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c. Crear una instancia y realizar un pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d. Mostrar los detalles del pedido realizado
print(f"Ingredientes vegetales: {mi_pizza.ingredientes_vegetales}")
print(f"Ingrediente proteico: {mi_pizza.ingrediente_proteico}")
print(f"Tipo de masa: {mi_pizza.tipo_de_masa}")
print(f"¿Es la pizza válida?: {'Sí' if mi_pizza.es_valida else 'No'}")

# e. Intentar mostrar si la clase Pizza es válida sin crear una instancia (esto debería generar un error)
try:
    print(f"¿Es la clase Pizza una pizza válida?: {'Sí' if Pizza.es_valida else 'No'}")
except AttributeError:
    print("Error: La clase 'Pizza' no tiene un atributo 'es_valida' sin una instancia.")