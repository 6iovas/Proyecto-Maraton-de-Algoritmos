// Proyecto de Informatica
// Ejercicio 365
Título del Ejercicio: Invertir Cadena
Análisis del Problema
? Descripción del Problema: Invertir el contenido de una cadena de caracteres.

? Entradas y Salidas:

? Entrada: Cadena de texto.

? Salida: Cadena invertida.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar un bucle desde el final hacia el inicio.

2. Construir cadena invertida.

3. Mostrar resultado.

? Estructuras de Datos: Cadena de caracteres.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

int main() {
    string texto = "Hola Mundo";
    string invertido="";

    for(int i=texto.length()-1;i>=0;i--) invertido += texto[i];

    cout << "Cadena invertida: " << invertido << endl; // "odnuM aloH"
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? "odnuM aloH"

? Caso 2: "ABC" ? "CBA"

? Caso 3: "" ? ""