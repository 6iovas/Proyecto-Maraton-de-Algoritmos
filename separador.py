# SCRIPT DE PYTHON PARA DIVIDIR EJERCICIOS (VERSIÓN FINAL)

import os

# --- Configuración del Archivo y Ubicación ---
carpeta_base = 'C:\\1 Informatica' 
nombre_archivo_entrada = 'Proyecto de INFORMATICA.txt'
ruta_completa_entrada = os.path.join(carpeta_base, nombre_archivo_entrada)

# --- Variables de Configuración ---
PATRON_BUSQUEDA = 'ejercicio'            # Busca la palabra 'ejercicio' para separar.
extension_codigo = '.py'                 
limite_archivos = 500                   
# -----------------------------------------------------------------

def dividir_y_guardar():
    """Busca líneas de inicio de ejercicio y guarda los bloques de 1 a 500."""
    # VARIABLES LOCALES INICIALIZADAS DENTRO DE LA FUNCIÓN PARA EVITAR EL ERROR
    contador_actual = 1                     # ¡Empezamos en 1!
    archivos_generados = 0
    buffer_ejercicio = ""
    
    try:
        with open(ruta_completa_entrada, 'r', encoding='latin-1') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print(f"🚨 ERROR: No se encontró el archivo '{ruta_completa_entrada}'.")
        return

    # 1. Recorrer el archivo línea por línea
    for linea in lineas:
        # Si la línea contiene el patrón de inicio de ejercicio y no hemos llegado al límite
        if PATRON_BUSQUEDA in linea.lower() and contador_actual <= limite_archivos:
            
            # Si el buffer ya tiene contenido (terminó el ejercicio anterior)
            if buffer_ejercicio.strip():
                
                # 2. Guardar el archivo anterior (siempre será el contador anterior)
                contador_a_guardar = contador_actual - 1
                
                if contador_a_guardar >= 1:
                    nombre_archivo = f'ejercicio{contador_a_guardar:03d}{extension_codigo}'
                    ruta_salida = os.path.join(carpeta_base, nombre_archivo)
                    
                    # Añadir la cabecera del proyecto
                    cabecera = f'// Proyecto de Informatica\n// Ejercicio {contador_a_guardar}\n'
                    
                    with open(ruta_salida, 'w', encoding='utf-8') as archivo_salida:
                        archivo_salida.write(cabecera + buffer_ejercicio.strip())
                        
                    print(f"✅ Creado: {nombre_archivo}")
                    archivos_generados += 1

            # Si el contador excede el límite (500), salimos inmediatamente
            if contador_actual > limite_archivos:
                break
                
            # Limpiar el buffer e iniciar el nuevo ejercicio
            buffer_ejercicio = ""
            contador_actual += 1
        
        # 3. Añadir la línea al buffer del ejercicio actual
        buffer_ejercicio += linea

    # 4. Guardar el ÚLTIMO ejercicio después de salir del bucle
    if buffer_ejercicio.strip() and archivos_generados < limite_archivos:
        nombre_archivo = f'ejercicio{contador_actual - 1:03d}{extension_codigo}'
        ruta_salida = os.path.join(carpeta_base, nombre_archivo)
        cabecera = f'// Proyecto de Informatica\n// Ejercicio {contador_actual - 1}\n'

        with open(ruta_salida, 'w', encoding='utf-8') as archivo_salida:
            archivo_salida.write(cabecera + buffer_ejercicio.strip())
        
        print(f"✅ Creado: {nombre_archivo} (Último)")
        archivos_generados += 1

    print(f"\n✨ ¡División de archivos completada! Total de archivos generados: {archivos_generados} archivos .py")

if __name__ == "__main__":
    dividir_y_guardar()