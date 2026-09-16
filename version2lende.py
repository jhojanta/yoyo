import time
from datetime import datetime

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
        # Captura automática de la fecha de registro actual
        self.__fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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
        return f"[{self.__fecha_registro}] SIS: {self.get_numero_sis()} | DNI: {self.get_dni()} | Nombre: {self.get_nombres()} | Zona: {self.__comunidad}"


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
    
    # 2. map: Extrae solo los números SIS para el reporte
    reporte_sis = list(map(lambda p: p.get_numero_sis(), pacientes_filtrados))
    
    return reporte_sis


# ==========================================
# PARADIGMA PROCEDURAL (Flujo Principal CLI)
# ==========================================
def registrar_paciente_seguro():
    """Maneja la entrada de datos con control de excepciones y código limpio."""
    try:
        print("\n--- NUEVO REGISTRO SIS ---")
        dni = input("Ingrese DNI (8 dígitos): ")
        
        if len(dni) != 8 or not dni.isdigit():
            raise ValueError("El DNI debe contener exactamente 8 caracteres numéricos.")
            
        nombres = input("Ingrese Nombres completos: ")
        numero_sis = input("Ingrese Código SIS (Ej. SIS-001): ")
        comunidad = input("Ingrese Comunidad de procedencia: ")
        
        nuevo_paciente = Paciente(dni, nombres, numero_sis, comunidad)
        
        print("\nProcesando y asegurando datos (Ley N.° 29733)...")
        time.sleep(0.5) 
        
        nuevo_paciente.ofuscar_datos()
        print("¡Registro exitoso y datos asegurados!")
        return nuevo_paciente
        
    except ValueError as error:
        print(f"\n[ERROR DE VALIDACIÓN]: {error}")
        return None
    except Exception as error:
        print(f"\n[ERROR INESPERADO]: {error}")
        return None

def menu_principal():
    """Bucle principal que mantiene el sistema activo."""
    base_datos_temporal = []
    
    while True:
        print("\n" + "="*40)
        print(" SISTEMA PUESTO DE SALUD - Nivel I-1")
        print("="*40)
        print("1. Registrar nuevo paciente")
        print("2. Ver pacientes registrados")
        print("3. Generar reporte por comunidad")
        print("4. Salir del sistema")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == '1':
            paciente = registrar_paciente_seguro()
            if paciente:
                base_datos_temporal.append(paciente)
        elif opcion == '2':
            print("\n--- PACIENTES EN BASE DE DATOS ---")
            if not base_datos_temporal:
                print("No hay pacientes registrados aún.")
            for p in base_datos_temporal:
                print(p)
        elif opcion == '3':
            comunidad = input("\nIngrese la comunidad a buscar: ")
            reporte = generar_reporte_por_comunidad(base_datos_temporal, comunidad)
            print(f"Códigos SIS atendidos en {comunidad}: {reporte}")
        elif opcion == '4':
            print("\nCerrando sistema de forma segura. ¡Hasta pronto!")
            break
        else:
            print("\n[ERROR] Opción no válida. Intente nuevamente.")

# ==========================================
# EJECUCIÓN DEL SISTEMA
# ==========================================
if __name__ == "__main__":
    menu_principal()