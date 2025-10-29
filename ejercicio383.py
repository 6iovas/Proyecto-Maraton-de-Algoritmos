// Proyecto de Informatica
// Ejercicio 383
Título del Ejercicio: Suma de Digitos de un Número (Recursivo)
Análisis del Problema
? Descripción del Problema: Calcular la suma de los dígitos de un número entero usando recursión.

? Entradas y Salidas:

? Entrada: Número entero positivo.

? Salida: Suma de los dígitos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si n==0 ? retornar 0.

2. Retornar (n%10 + sumaDigitos(n/10)).

? Estructuras de Datos: Variables enteras.

? Funciones Principales: main() y sumaDigitos().

Código Fuente (C++)
#include <iostream>
using namespace std;

int sumaDigitos(int n){
    if(n==0) return 0;
    return n%10 + sumaDigitos(n/10);
}

int main() {
    int n=1234;
    cout << "Suma de digitos de " << n << " = " << sumaDigitos(n) << endl; // 10
    return 0;
}

Pruebas
? Caso 1: 1234 ? 10

? Caso 2: 0 ? 0

? Caso 3: 987 ? 24