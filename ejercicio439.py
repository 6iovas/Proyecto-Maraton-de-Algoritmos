// Proyecto de Informatica
// Ejercicio 439
Título del Ejercicio: Contar Palabras en una Cadena
Análisis del Problema
? Descripción del Problema: Contar cuántas palabras contiene una cadena.

? Entradas y Salidas:

? Entrada: Cadena de texto.

? Salida: Número de palabras.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar stringstream para separar palabras.

2. Contar cada palabra.

? Estructuras de Datos: Cadena y stringstream.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <sstream>
using namespace std;

int main() {
    string texto="Hola mundo desde C++";
    string palabra;
    int contador=0;
    stringstream ss(texto);
    while(ss >> palabra) contador++;
    cout << "Cantidad de palabras: " << contador << endl; // 4
    return 0;
}

Pruebas
? Caso 1: "Hola mundo" ? 2

? Caso 2: "" ? 0

? Caso 3: "Una palabra más" ? 3