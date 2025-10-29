// Proyecto de Informatica
// Ejercicio 313
Título del Ejercicio: Buscar Elemento en Lista Enlazada Recursivamente
Análisis del Problema
? Descripción del Problema: Crear función recursiva que busque un valor en una lista enlazada y devuelva verdadero o falso.

? Entradas y Salidas:

? Entrada: Valor a buscar.

? Salida: true si se encuentra, false si no.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si nodo actual es nullptr ? retornar false.

2. Si nodo actual contiene valor ? retornar true.

3. Llamar recursivamente con siguiente nodo.

? Estructuras de Datos: Lista enlazada simple.

? Funciones Principales: main() y buscarRecursivo().

Código Fuente (C++)
#include <iostream>
using namespace std;

struct Nodo {
    int dato;
    Nodo* siguiente;
};

bool buscarRecursivo(Nodo* cabeza, int valor) {
    if(!cabeza) return false;
    if(cabeza->dato == valor) return true;
    return buscarRecursivo(cabeza->siguiente, valor);
}

int main() {
    Nodo* lista = new Nodo{10, new Nodo{20, new Nodo{30, nullptr}}};

    cout << boolalpha;
    cout << "Buscar 20: " << buscarRecursivo(lista, 20) << endl; // true
    cout << "Buscar 40: " << buscarRecursivo(lista, 40) << endl; // false

    return 0;
}

Pruebas
? Caso 1: Buscar 20 ? true

? Caso 2: Buscar 10 ? true

? Caso 3: Buscar 50 ? false