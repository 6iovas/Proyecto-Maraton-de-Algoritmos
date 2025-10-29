// Proyecto de Informatica
// Ejercicio 425
Título del Ejercicio: Calcular Potencia de un Número (Recursivo)
Análisis del Problema
? Descripción del Problema: Calcular base^exponente usando recursión.

? Entradas y Salidas:

? Entrada: Base b y exponente e.

? Salida: Resultado de b^e.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si e == 0 ? retornar 1.

2. Retornar b * potencia(b, e-1).

? Estructuras de Datos: Variables enteras.

? Funciones Principales: main() y potencia().

Código Fuente (C++)
#include <iostream>
using namespace std;

int potencia(int b, int e){
    if(e==0) return 1;
    return b * potencia(b,e-1);
}

int main() {
    int base=2, exponente=4;
    cout << base << "^" << exponente << " = " << potencia(base,exponente) << endl; // 16
    return 0;
}

Pruebas
? Caso 1: 2^4 ? 16

? Caso 2: 5^0 ? 1

? Caso 3: 3^3 ? 27