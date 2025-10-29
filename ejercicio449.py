// Proyecto de Informatica
// Ejercicio 449
Título del Ejercicio: Convertir Minúsculas a Mayúsculas
Análisis del Problema
? Descripción del Problema: Convertir todos los caracteres de una cadena a mayúsculas.

? Entradas y Salidas:

? Entrada: Cadena s.

? Salida: Cadena en mayúsculas.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer cada carácter de la cadena.

2. Usar toupper() para convertirlo a mayúscula.

? Estructuras de Datos: Cadena de caracteres.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string s="Hola Mundo";
    for(int i=0;i<s.length();i++) s[i]=toupper(s[i]);
    cout << "Cadena en mayusculas: " << s << endl; // HOLA MUNDO
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? "HOLA MUNDO"

? Caso 2: "c++" ? "C++"

? Caso 3: "" ? ""