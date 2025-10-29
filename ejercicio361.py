// Proyecto de Informatica
// Ejercicio 361
Título del Ejercicio: Buscar Elemento en Lista Enlazada
Análisis del Problema
? Descripción del Problema: Crear una lista enlazada y buscar un elemento dado.

? Entradas y Salidas:

? Entrada: Lista de enteros y valor a buscar.

? Salida: Posición del elemento o -1 si no se encuentra.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer la lista desde la cabeza.

2. Comparar cada nodo con el valor buscado.

3. Retornar posición si se encuentra o -1 si no.

? Estructuras de Datos: Lista enlazada simple.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

struct Nodo { int dato; Nodo* siguiente; };

int buscar(Nodo* cabeza, int valor) {
    int pos=0;
    while(cabeza != nullptr) {
        if(cabeza->dato == valor) return pos;
        cabeza = cabeza->siguiente;
        pos++;
    }
    return -1;
}

int main() {
    Nodo* lista = new Nodo{5, new Nodo{10, new Nodo{3, nullptr}}};
    cout << "Posicion del 10: " << buscar(lista,10) << endl; // 1
    cout << "Posicion del 7: " << buscar(lista,7) << endl;   // -1
    return 0;
}

Pruebas
? Caso 1: [5,10,3], buscar 10 ? 1

? Caso 2: [5,10,3], buscar 7 ? -1

? Caso 3: [1], buscar 1 ? 0