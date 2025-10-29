// Proyecto de Informatica
// Ejercicio 381
Título del Ejercicio: Invertir Palabras en una Cadena
Análisis del Problema
? Descripción del Problema: Invertir el orden de las palabras de una cadena.

? Entradas y Salidas:

? Entrada: Cadena de texto.

? Salida: Cadena con palabras invertidas.

Diseño de la Solución
? Algoritmo Propuesto:

1. Separar palabras usando stringstream.

2. Guardarlas en un array o vector.

3. Mostrar palabras en orden inverso.

? Estructuras de Datos: Vector o array de strings.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    string texto = "Hola mundo desde C++";
    stringstream ss(texto);
    string palabra;
    vector<string> palabras;

    while(ss >> palabra) palabras.push_back(palabra);

    cout << "Palabras invertidas: ";
    for(int i=palabras.size()-1;i>=0;i--) cout << palabras[i] << " ";
    cout << endl; // "C++ desde mundo Hola"
    return 0;
}

Pruebas
? Caso 1: "Hola mundo" ? "mundo Hola"

? Caso 2: "Una palabra" ? "palabra Una"

? Caso 3: "" ? ""