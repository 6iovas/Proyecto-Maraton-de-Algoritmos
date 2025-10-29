// Proyecto de Informatica
// Ejercicio 359
Título del Ejercicio: Contar Elementos de una Cola
Análisis del Problema
? Descripción del Problema: Crear una cola y contar la cantidad de elementos que contiene.

? Entradas y Salidas:

? Entrada: Elementos a insertar en la cola.

? Salida: Cantidad de elementos en la cola.

Diseño de la Solución
? Algoritmo Propuesto:

1. Insertar elementos en la cola.

2. Usar un contador para cada elemento.

3. Mostrar resultado.

? Estructuras de Datos: Cola (queue).

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> cola;
    cola.push(1);
    cola.push(2);
    cola.push(3);

    int contador = 0;
    queue<int> temp = cola;
    while(!temp.empty()) {
        contador++;
        temp.pop();
    }

    cout << "Cantidad de elementos en la cola: " << contador << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [1,2,3] ? 3

? Caso 2: [5,6,7,8] ? 4

? Caso 3: Cola vacía ? 0