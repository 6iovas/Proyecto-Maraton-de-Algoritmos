// Proyecto de Informatica
// Ejercicio 297
Título del Ejercicio: Clase Libro con Método Mostrar Información
Análisis del Problema
? Descripción del Problema: Crear una clase Libro con atributos titulo, autor y anio, y un método mostrar() que imprima la información del libro.

? Entradas y Salidas:

? Entrada: Título, autor y año.

? Salida: Información del libro.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear clase Libro con atributos titulo, autor, anio.

2. Implementar método mostrar() que imprima los atributos.

3. Crear objeto Libro y llamar a mostrar().

? Estructuras de Datos: Clase con string e int.

? Funciones Principales: main() y mostrar().

Código Fuente (C++)
#include <iostream>
#include <string>

class Libro {
public:
    std::string titulo;
    std::string autor;
    int anio;

    void mostrar() {
        std::cout << "Titulo: " << titulo << ", Autor: " << autor << ", Año: " << anio << std::endl;
    }
};

int main() {
    Libro l;
    std::cout << "Ingresa el titulo del libro: ";
    std::getline(std::cin, l.titulo);
    std::cout << "Ingresa el autor: ";
    std::getline(std::cin, l.autor);
    std::cout << "Ingresa el año: ";
    std::cin >> l.anio;

    l.mostrar();
    return 0;
}

Pruebas
? Caso 1: "C++ Avanzado", "Juan Pérez", 2025 ? Salida: "Titulo: C++ Avanzado, Autor: Juan Pérez, Año: 2025"

? Caso 2: "POO", "Ana López", 2020 ? "Titulo: POO, Autor: Ana López, Año: 2020"

? Caso 3: "Algoritmos", "Luis Gómez", 2019 ? "Titulo: Algoritmos, Autor: Luis Gómez, Año: 2019"