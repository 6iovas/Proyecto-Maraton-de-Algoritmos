// Proyecto de Informatica
// Ejercicio 311
Título del Ejercicio: Eliminar Nodo de Lista Enlazada por Valor
Análisis del Problema
? Descripción del Problema: Crear función que elimine un nodo específico en una lista enlazada simple según su valor.

? Entradas y Salidas:

? Entrada: Valor a eliminar.

? Salida: Lista actualizada.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer la lista hasta encontrar el nodo con valor buscado.

2. Modificar punteros para saltar el nodo y eliminarlo.

3. Mostrar la lista resultante.

? Estructuras de Datos: Lista enlazada simple.

? Funciones Principales: main() y eliminarNodo().

Código Fuente (C++)
#include <iostream>
using namespace std;

struct Nodo {
    int dato;
    Nodo* siguiente;
};

void eliminarNodo(Nodo*& cabeza, int valor) {
    if(!cabeza) return;
    if(cabeza->dato == valor) {
        Nodo* temp = cabeza;
        cabeza = cabeza->siguiente;
        delete temp;
        return;
    }
    Nodo* temp = cabeza;
    while(temp->siguiente && temp->siguiente->dato != valor) temp = temp->siguiente;
    if(temp->siguiente) {
        Nodo* aEliminar = temp->siguiente;
        temp->siguiente = temp->siguiente->siguiente;
        delete aEliminar;
    }
}

void mostrar(Nodo* cabeza) {
    Nodo* temp = cabeza;
    cout << "Lista: ";
    while(temp) { cout << temp->dato << " "; temp = temp->siguiente; }
    cout << endl;
}

int main() {
    Nodo* lista = nullptr;
    lista = new Nodo{10, nullptr};
    lista->siguiente = new Nodo{20, nullptr};
    lista->siguiente->siguiente = new Nodo{30, nullptr};

    eliminarNodo(lista, 20);
    mostrar(lista); // 10 30

    eliminarNodo(lista, 10);
    mostrar(lista); // 30
    return 0;
}

Pruebas
? Caso 1: Eliminar 20 ? Lista: 10 30

? Caso 2: Eliminar 10 ? Lista: 30

? Caso 3: Eliminar 40 (no existe) ? Lista: 30