# Variables externas
from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipos_de_masa

# Definicion clase de Pizza
class Pizza():
    precio = 10000
    tamaño = "Familiar"
    
    def crear_pizza(self):
        """Metodo que crea una nueva pizza con atributos para almacenar el ingrediente proteico,
        los ingredientes vegetales, el tipo de masa y si la pizza es válida según los ingredientes seleccionados.
        """
        self.ingrediente_proteico = None
        self.ingredientes_vegetales = []
        self.tipo_de_masa = None
        self.es_valida = False

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        """Metodo que verifica si el elemento dado se encuentra dentro de una lista de valores posibles.

        Args:
            elemento (str): El valor a validar entre ingredientes o tipo de masa.
            valores_posibles (list): Lista que contiene los elementos validos, a evaluar según "elemento".

        Returns:
            bool: Retorna True si se encuentra el elemento en la lista de valores posible, False en caso contrario.
        """
        return elemento in valores_posibles

    def realizar_pedido(self):
        """Solicita al usuario ingresar los ingredientes para su pizza y el tipo de masa,
        validando cada entrada contra los valores posibles definidos.
        """
        proteico = input("Ingrese el ingrediente proteico (pollo, vacuno, carne vegetal): ")
        vegetal1 = input("Ingrese el primer ingrediente vegetal (tomate, aceitunas, champiñones): ")
        vegetal2 = input("Ingrese el segundo ingrediente vegetal (tomate, aceitunas, champiñones): ")
        masa = input("Ingrese el tipo de masa (tradicional, delgada): ")

        # Validación de los ingredientes y tipo de masa
        if (Pizza.validar_elemento(proteico, ingredientes_proteicos) and
                Pizza.validar_elemento(vegetal1, ingredientes_vegetales) and
                Pizza.validar_elemento(vegetal2, ingredientes_vegetales) and
                vegetal1 != vegetal2 and  # Asegurar que los ingredientes vegetales sean diferentes
                Pizza.validar_elemento(masa, tipos_de_masa)):
            self.ingrediente_proteico = proteico
            self.ingredientes_vegetales = [vegetal1, vegetal2]
            self.tipo_de_masa = masa
            self.es_valida = True
        else:
            print("Pedido inválido. Asegúrese de que los ingredientes y el tipo de masa son correctos y que los ingredientes vegetales no sean iguales.")