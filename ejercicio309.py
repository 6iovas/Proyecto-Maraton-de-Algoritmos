// Proyecto de Informatica
// Ejercicio 309
Título del Ejercicio: Lista Enlazada Simple con Inserción al Inicio y Fin
Análisis del Problema
? Descripción del Problema: Crear una lista enlazada simple que permita insertar nodos al inicio y al final, y mostrar la lista.

? Entradas y Salidas:

? Entrada: Valores enteros a insertar.

? Salida: Lista enlazada mostrada de inicio a fin.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir estructura Nodo con dato y siguiente.

2. Crear funciones insertarInicio(), insertarFin() y mostrar().

3. Insertar elementos según entrada y mostrar la lista.

? Estructuras de Datos: Lista enlazada simple.

? Funciones Principales: main(), insertarInicio(), insertarFin(), mostrar().

Código Fuente (C++)
#include <iostream>
using namespace std;

struct Nodo {
    int dato;
    Nodo* siguiente;
};

void insertarInicio(Nodo*& cabeza, int valor) {
    Nodo* nuevo = new Nodo{valor, cabeza};
    cabeza = nuevo;
}

void insertarFin(Nodo*& cabeza, int valor) {
    Nodo* nuevo = new Nodo{valor, nullptr};
    if(!cabeza) cabeza = nuevo;
    else {
        Nodo* temp = cabeza;
        while(temp->siguiente) temp = temp->siguiente;
        temp->siguiente = nuevo;
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
    insertarInicio(lista, 10);
    insertarFin(lista, 20);
    insertarInicio(lista, 5);
    mostrar(lista); // 5 10 20
    return 0;
}

Pruebas
? Caso 1: Insertar inicio 10, fin 20, inicio 5 ? Lista: 5 10 20

? Caso 2: Insertar fin 30 ? Lista: 5 10 20 30

? Caso 3: Lista vacía ? Mostrar ? Lista: