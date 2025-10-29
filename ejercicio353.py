// Proyecto de Informatica
// Ejercicio 353
Título del Ejercicio: Clase Persona con Saludar
Análisis del Problema
? Descripción del Problema: Crear clase Persona con atributos nombre y edad y método saludar().

? Entradas y Salidas:

? Entrada: Nombre y edad.

? Salida: Mensaje de saludo por pantalla.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear clase Persona.

2. Implementar método saludar().

3. Crear objeto e invocar método.

? Estructuras de Datos: Clase con variables string y int.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

class Persona {
public:
    string nombre;
    int edad;
    void saludar() {
        cout << "Hola, soy " << nombre << " y tengo " << edad << " anos." << endl;
    }
};

int main() {
    Persona p;
    p.nombre="Juan";
    p.edad=25;
    p.saludar();
    return 0;
}

Pruebas
? Caso 1: "Juan", 25 ? Saludar correctamente

? Caso 2: "Ana", 30 ? Saludar correctamente

? Caso 3: "Pedro", 0 ? Saludar correctamente