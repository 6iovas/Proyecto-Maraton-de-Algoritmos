// Proyecto de Informatica
// Ejercicio 363
Título del Ejercicio: Contar Palabras en una Cadena
Análisis del Problema
? Descripción del Problema: Contar cuántas palabras hay en una cadena separadas por espacios.

? Entradas y Salidas:

? Entrada: Cadena de texto.

? Salida: Número de palabras.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer la cadena caracter por caracter.

2. Incrementar contador cuando se encuentre un espacio seguido de letra.

3. Retornar contador +1 al final.

? Estructuras de Datos: Cadena de caracteres y contador entero.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    string texto = "Hola mundo desde C++";
    stringstream ss(texto);
    string palabra;
    int contador=0;

    while(ss >> palabra) contador++;

    cout << "Numero de palabras: " << contador << endl; // 4
    return 0;
}

Pruebas
? Caso 1: "Hola mundo desde C++" ? 4

? Caso 2: "Una palabra" ? 2

? Caso 3: "" ? 0