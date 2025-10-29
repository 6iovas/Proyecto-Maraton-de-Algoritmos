// Proyecto de Informatica
// Ejercicio 349
Título del Ejercicio: Clase Libro con Mostrar Información
Análisis del Problema
? Descripción del Problema: Crear clase Libro con atributos titulo, autor y anio, y método para mostrar información.

? Entradas y Salidas:

? Entrada: Datos del libro.

? Salida: Información del libro por pantalla.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear clase Libro.

2. Implementar método mostrar().

3. Crear objeto e invocar mostrar().

? Estructuras de Datos: Clase con variables de tipo string y int.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

class Libro {
public:
    string titulo, autor;
    int anio;
    void mostrar() {
        cout << "Titulo: " << titulo << ", Autor: " << autor << ", Anio: " << anio << endl;
    }
};

int main() {
    Libro l;
    l.titulo="C++ para Todos";
    l.autor="Juan Perez";
    l.anio=2023;
    l.mostrar();
    return 0;
}

Pruebas
? Caso 1: "C++ para Todos", Juan Perez, 2023 ? Mostrar datos correctos

? Caso 2: "Libro A", Autor B, 2000 ? Mostrar datos correctos

? Caso 3: "Libro Vacío" ? Mostrar datos asignados