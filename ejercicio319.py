// Proyecto de Informatica
// Ejercicio 319
Título del Ejercicio: Invertir Cola usando Pila Auxiliar
Análisis del Problema
? Descripción del Problema: Invertir el orden de los elementos de una cola usando una pila auxiliar.

? Entradas y Salidas:

? Entrada: Números en la cola.

? Salida: Cola invertida.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear array para cola y stack para pila auxiliar.

2. Extraer elementos de la cola y push en pila.

3. Extraer de pila y push en cola.

4. Mostrar cola invertida.

? Estructuras de Datos: Array y stack.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <stack>
using namespace std;

int main() {
    int cola[5] = {1,2,3,4,5};
    int n=5;
    stack<int> pila;

    for(int i=0;i<n;i++) pila.push(cola[i]);
    for(int i=0;i<n;i++) { cola[i]=pila.top(); pila.pop(); }

    cout << "Cola invertida: ";
    for(int i=0;i<n;i++) cout << cola[i] << " ";
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: Cola [1,2,3,4,5] ? [5,4,3,2,1]

? Caso 2: Cola [10,20] ? [20,10]

? Caso 3: Cola vacía ? Salida vacía