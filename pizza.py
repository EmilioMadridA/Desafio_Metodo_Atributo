# Variables externas
from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipos_de_masa

# Definicion clase de Pizza
class Pizza():
    precio = 10000
    tamaño = "Familiar"
    
    def __init__(self):
        """Metodo que crea una nueva pizza con atributos para almacenar el ingrediente proteico,
        los ingredientes vegetales, el tipo de masa y si la pizza es válida según los ingredientes seleccionados.
        """
        self.ingrediente_proteico = ''
        self.ingredientes_vegetales = []
        self.tipo_de_masa = ''
        self.es_valida = False

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        """Metodo que verifica si el elemento dado se encuentra dentro de una lista de valores posibles.

            Args:
            elemento (str): El valor a validar entre ingredientes o tipo de masa.
            valores_posibles (list): Lista que contiene los elementos validos, a evaluar según "elemento".

         Returns:
            elemento (str): Retorna el elemento ingresado
         """
        while elemento not in valores_posibles:
            print(f"Opción no válida, ingrese una de las opciones válidas: {', '.join(valores_posibles)} \n")
            elemento = input('Ingresa una Opción: \n').lower()
        return elemento

    def realizar_pedido(self):
        """Solicita al usuario ingresar los ingredientes para su pizza y el tipo de masa,
        validando cada entrada contra los valores posibles definidos.
        """
        proteico = input("Ingrese el ingrediente proteico (pollo, vacuno, carne vegetal): \n")
        proteina = Pizza.validar_elemento(proteico, ingredientes_proteicos)
        vegetal1 = input("Ingrese el primer ingrediente vegetal (tomate, aceitunas, champiñones): \n")
        vegetal_1 = Pizza.validar_elemento(vegetal1, ingredientes_vegetales)
        vegetal2 = input("Ingrese el segundo ingrediente vegetal (tomate, aceitunas, champiñones): \n")
        vegetal_2 = Pizza.validar_elemento(vegetal2, ingredientes_vegetales)
        masa = input("Ingrese el tipo de masa (tradicional, delgada): \n")
        masa_final = Pizza.validar_elemento(masa, tipos_de_masa)

        # Validación de los ingredientes vegetales distintos
        if vegetal_1 != vegetal_2:
            self.ingrediente_proteico = proteina
            self.ingredientes_vegetales = [vegetal_1, vegetal_2]
            self.tipo_de_masa = masa
            self.es_valida = True
        else:
            print("Pedido inválido. Asegúrese de que los ingredientes y el tipo de masa son correctos y que los ingredientes vegetales no sean iguales.")