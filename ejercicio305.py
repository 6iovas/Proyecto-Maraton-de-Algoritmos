// Proyecto de Informatica
// Ejercicio 305
Título del Ejercicio: Implementar Pila con Array Dinámico
Análisis del Problema
? Descripción del Problema: Crear una pila (stack) usando un array dinámico con operaciones push, pop y mostrar.

? Entradas y Salidas:

? Entrada: Elementos a agregar o eliminar.

? Salida: Estado actual de la pila.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear array dinámico con tamaño n.

2. Mantener variable tope para el índice superior.

3. Implementar funciones push(), pop() y mostrar().

4. Mostrar resultados tras cada operación.

? Estructuras de Datos: Array dinámico y variable tope.

? Funciones Principales: main(), push(), pop(), mostrar().

Código Fuente (C++)
#include <iostream>
using namespace std;

class Pila {
    int* arr;
    int tope;
    int capacidad;
public:
    Pila(int n) {
        capacidad = n;
        arr = new int[capacidad];
        tope = -1;
    }
    void push(int valor) {
        if(tope >= capacidad-1) cout << "Pila llena\n";
        else arr[++tope] = valor;
    }
    void pop() {
        if(tope < 0) cout << "Pila vacia\n";
        else tope--;
    }
    void mostrar() {
        cout << "Pila: ";
        for(int i=0;i<=tope;i++) cout << arr[i] << " ";
        cout << endl;
    }
    ~Pila() { delete[] arr; }
};

int main() {
    Pila p(5);
    p.push(10); p.push(20); p.push(30);
    p.mostrar(); // 10 20 30
    p.pop();
    p.mostrar(); // 10 20
    return 0;
}

Pruebas
? Caso 1: push 10,20,30 ? Pila: 10 20 30

? Caso 2: pop ? Pila: 10 20

? Caso 3: push hasta 5 elementos ? Pila llena si excede capacidad