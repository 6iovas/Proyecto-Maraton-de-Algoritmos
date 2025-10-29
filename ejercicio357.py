// Proyecto de Informatica
// Ejercicio 357
Título del Ejercicio: Sumar los Elementos de una Pila
Análisis del Problema
? Descripción del Problema: Crear una pila (stack) y calcular la suma de todos sus elementos.

? Entradas y Salidas:

? Entrada: Elementos a insertar en la pila.

? Salida: Suma de todos los elementos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Insertar elementos en la pila.

2. Mientras la pila no esté vacía, sacar el elemento y sumarlo.

3. Mostrar resultado.

? Estructuras de Datos: Pila (stack).

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> pila;
    pila.push(5);
    pila.push(10);
    pila.push(3);
    
    int suma = 0;
    while(!pila.empty()) {
        suma += pila.top();
        pila.pop();
    }
    
    cout << "Suma de elementos de la pila: " << suma << endl; // 18
    return 0;
}

Pruebas
? Caso 1: [5,10,3] ? 18

? Caso 2: [1,2,3,4] ? 10

? Caso 3: Pila vacía ? 0