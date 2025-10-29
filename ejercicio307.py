// Proyecto de Informatica
// Ejercicio 307
Título del Ejercicio: Implementar Cola con Array Circular
Análisis del Problema
? Descripción del Problema: Implementar una cola (queue) usando un array circular con operaciones enqueue, dequeue y mostrar.

? Entradas y Salidas:

? Entrada: Elementos a agregar o eliminar.

? Salida: Estado actual de la cola.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear array con tamaño n y punteros frente y final.

2. Implementar enqueue() para insertar, dequeue() para eliminar y mostrar() para imprimir.

3. Verificar condiciones de cola llena y vacía.

? Estructuras de Datos: Array dinámico y dos índices.

? Funciones Principales: main(), enqueue(), dequeue(), mostrar().

Código Fuente (C++)
#include <iostream>
using namespace std;

class Cola {
    int* arr;
    int frente, final, capacidad;
public:
    Cola(int n) { arr = new int[n]; capacidad=n; frente=0; final=0; }
    bool llena() { return (final+1)%capacidad == frente; }
    bool vacia() { return frente == final; }
    void enqueue(int x) {
        if(llena()) cout << "Cola llena\n";
        else { arr[final]=x; final=(final+1)%capacidad; }
    }
    void dequeue() {
        if(vacia()) cout << "Cola vacia\n";
        else frente=(frente+1)%capacidad;
    }
    void mostrar() {
        cout << "Cola: ";
        for(int i=frente; i!=final; i=(i+1)%capacidad) cout << arr[i] << " ";
        cout << endl;
    }
    ~Cola(){ delete[] arr; }
};

int main() {
    Cola c(5);
    c.enqueue(1); c.enqueue(2); c.enqueue(3);
    c.mostrar(); // 1 2 3
    c.dequeue();
    c.mostrar(); // 2 3
    return 0;
}

Pruebas
? Caso 1: enqueue 1,2,3 ? Cola: 1 2 3

? Caso 2: dequeue ? Cola: 2 3

? Caso 3: enqueue hasta cola llena ? Mensaje "Cola llena"