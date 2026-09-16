import time

# ==========================================
# PARADIGMA ORIENTADO A OBJETOS (POO)
# ==========================================
class Persona:
    def __init__(self, dni, nombres):
        # Encapsulamiento estricto: atributos privados
        self.__dni = dni
        self.__nombres = nombres

    # Getters
    def get_dni(self):
        return self.__dni

    def get_nombres(self):
        return self.__nombres

class Paciente(Persona):
    def __init__(self, dni, nombres, numero_sis, comunidad):
        super().__init__(dni, nombres)
        self.__numero_sis = numero_sis
        self.__comunidad = comunidad
        self.__datos_ofuscados = False

    def get_comunidad(self):
        return self.__comunidad
    
    def get_numero_sis(self):
        return self.__numero_sis

    # Método de seguridad: Tratamiento de datos personales (Ley N.° 29733)
    def ofuscar_datos(self):
        """Enmascara los datos sensibles antes de un posible guardado local."""
        if not self.__datos_ofuscados:
            dni_original = self.get_dni()
            nombres_originales = self.get_nombres()
            
            # Solo muestra los primeros 4 dígitos del DNI y las iniciales del nombre
            self._Persona__dni = dni_original[:4] + "****"
            self._Persona__nombres = nombres_originales[0] + "***"
            self.__datos_ofuscados = True
            
    def __str__(self):
        return f"Paciente SIS: {self.get_numero_sis()} | DNI: {self.get_dni()} | Nombre: {self.get_nombres()} | Comunidad: {self.__comunidad}"


# ==========================================
# PARADIGMA FUNCIONAL (PF)
# ==========================================
def generar_reporte_por_comunidad(lista_pacientes, comunidad_objetivo):
    """
    Usa funciones de orden superior (filter y map) para procesar datos 
    sin efectos secundarios (inmutabilidad).
    """
    # 1. filter: Filtra solo los pacientes de la comunidad indicada
    pacientes_filtrados = filter(lambda p: p.get_comunidad().lower() == comunidad_objetivo.lower(), lista_pacientes)
    
    # 2. map: Extrae solo los números SIS para el reporte epidemiológico
    reporte_sis = list(map(lambda p: p.get_numero_sis(), pacientes_filtrados))
    
    return reporte_sis


# ==========================================
# PARADIGMA PROCEDURAL (Flujo Principal CLI)
# ==========================================
def registrar_paciente_seguro():
    """Maneja la entrada de datos con control de excepciones y código limpio."""
    try:
        print("\n--- REGISTRO DE PACIENTE SIS ---")
        dni = input("Ingrese DNI (8 dígitos): ")
        
        # Manejo de excepciones: Validar formato de DNI
        if len(dni) != 8 or not dni.isdigit():
            raise ValueError("El DNI debe contener exactamente 8 caracteres numéricos.")
            
        nombres = input("Ingrese Nombres completos: ")
        numero_sis = input("Ingrese Código SIS: ")
        comunidad = input("Ingrese Comunidad de procedencia: ")
        
        nuevo_paciente = Paciente(dni, nombres, numero_sis, comunidad)
        
        print("\nProcesando y asegurando datos (Ley N.° 29733)...")
        time.sleep(1) # Simulando latencia de procesamiento
        
        # Aplicamos seguridad antes de consolidar en el sistema
        nuevo_paciente.ofuscar_datos()
        print("¡Registro exitoso y datos ofuscados correctamente!")
        return nuevo_paciente
        
    except ValueError as error:
        print(f"[ERROR DE VALIDACIÓN]: {error}")
        return None
    except Exception as error:
        print(f"[ERROR INESPERADO]: Ocurrió un fallo en el sistema: {error}")
        return None

# ==========================================
# EJECUCIÓN DE PRUEBA
# ==========================================
if __name__ == "__main__":
    base_datos_temporal = []
    
    # Simulamos el registro de un paciente desde la interfaz de consola
    paciente_1 = registrar_paciente_seguro()
    if paciente_1:
        base_datos_temporal.append(paciente_1)
        print(paciente_1)
        
    # Agregamos datos de prueba para el reporte
    base_datos_temporal.append(Paciente("11112222", "Juan", "SIS-002", "La Paccha"))
    base_datos_temporal.append(Paciente("33334444", "Maria", "SIS-003", "Chugur"))
    
    # Generamos el reporte funcional
    print("\n--- REPORTE EPIDEMIOLÓGICO: LA PACCHA ---")
    reporte = generar_reporte_por_comunidad(base_datos_temporal, "La Paccha")
    print(f"Códigos SIS atendidos en La Paccha: {reporte}")