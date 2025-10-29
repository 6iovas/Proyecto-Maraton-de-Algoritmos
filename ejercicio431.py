// Proyecto de Informatica
// Ejercicio 431
Título del Ejercicio: Crear Clase Libro
Análisis del Problema
? Descripción del Problema: Implementar clase Libro con atributos titulo, autor y anio, y método mostrarInfo().

? Entradas y Salidas:

? Entrada: Datos del libro.

? Salida: Mostrar información del libro.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir clase Libro con atributos y método.

2. Crear objeto y llamar mostrarInfo().

? Estructuras de Datos: Clase y objeto.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

class Libro{
public:
    string titulo, autor;
    int anio;
    void mostrarInfo(){
        cout << titulo << " por " << autor << ", año " << anio << endl;
    }
};

int main() {
    Libro l;
    l.titulo="C++ Básico";
    l.autor="Juan Perez";
    l.anio=2025;
    l.mostrarInfo(); // C++ Básico por Juan Perez, año 2025
    return 0;
}

Pruebas
? Caso 1: C++ Básico ? correcto

? Caso 2: Historia ? correcto

? Caso 3: Ciencia ? correcto