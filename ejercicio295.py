// Proyecto de Informatica
// Ejercicio 295
Título del Ejercicio: Clase Persona con Método Saludar
Análisis del Problema
? Descripción del Problema: Crear una clase Persona con atributos nombre y edad y un método saludar() que imprima un mensaje de saludo.

? Entradas y Salidas:

? Entrada: Nombre y edad de la persona.

? Salida: Mensaje de saludo.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear clase Persona con atributos nombre y edad.

2. Implementar método saludar() que imprima: "Hola, soy [nombre] y tengo [edad] años".

3. Crear objeto Persona e invocar el método.

? Estructuras de Datos: Clase y variables de tipo string e int.

? Funciones Principales: main() y método de la clase.

Código Fuente (C++)
#include <iostream>
#include <string>

class Persona {
public:
    std::string nombre;
    int edad;

    void saludar() {
        std::cout << "Hola, soy " << nombre << " y tengo " << edad << " años." << std::endl;
    }
};

int main() {
    Persona p;
    std::cout << "Ingresa tu nombre: ";
    std::getline(std::cin, p.nombre);
    std::cout << "Ingresa tu edad: ";
    std::cin >> p.edad;

    p.saludar();
    return 0;
}

Pruebas
? Caso 1: "Juan", 20 ? "Hola, soy Juan y tengo 20 años."

? Caso 2: "Ana", 30 ? "Hola, soy Ana y tengo 30 años."

? Caso 3: "Luis", 0 ? "Hola, soy Luis y tengo 0 años."