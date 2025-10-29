// Proyecto de Informatica
// Ejercicio 323
Título del Ejercicio: Suma de Elementos de Lista Enlazada Recursivamente
Análisis del Problema
? Descripción del Problema: Calcular la suma de los elementos de una lista enlazada usando recursión.

? Entradas y Salidas:

? Entrada: Lista enlazada de enteros.

? Salida: Suma de sus elementos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si nodo es nullptr ? retornar 0.

2. Retornar dato + sumaRec(siguiente).

? Estructuras de Datos: Lista enlazada simple.

? Funciones Principales: main() y sumaRec().

Código Fuente (C++)
#include <iostream>
using namespace std;

struct Nodo { int dato; Nodo* siguiente; };

int sumaRec(Nodo* cabeza) {
    if(!cabeza) return 0;
    return cabeza->dato + sumaRec(cabeza->siguiente);
}

int main() {
    Nodo* lista = new Nodo{5, new Nodo{10, new Nodo{3, nullptr}}};
    cout << "Suma de elementos: " << sumaRec(lista) << endl; // 18
    return 0;
}

Pruebas
? Caso 1: [5,10,3] ? 18

? Caso 2: [1,2,3,4] ? 10

? Caso 3: lista vacía ? 0