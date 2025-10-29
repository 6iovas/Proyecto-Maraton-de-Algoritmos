// Proyecto de Informatica
// Ejercicio 385
Título del Ejercicio: Verificar Número Primo
Análisis del Problema
? Descripción del Problema: Determinar si un número entero positivo es primo.

? Entradas y Salidas:

? Entrada: Número entero n.

? Salida: Mensaje indicando si es primo o no.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si n < 2 ? no es primo.

2. Recorrer de 2 a ?n y verificar divisibilidad.

3. Si divisible ? no primo; si no ? primo.

? Estructuras de Datos: Variables enteras y boolean.

? Funciones Principales: main() y esPrimo().

Código Fuente (C++)
#include <iostream>
#include <cmath>
using namespace std;

bool esPrimo(int n){
    if(n<2) return false;
    for(int i=2;i<=sqrt(n);i++)
        if(n%i==0) return false;
    return true;
}

int main() {
    int n=17;
    if(esPrimo(n)) cout << n << " es primo" << endl;
    else cout << n << " no es primo" << endl;
    return 0;
}

Pruebas
? Caso 1: 17 ? primo

? Caso 2: 10 ? no primo

? Caso 3: 2 ? primo