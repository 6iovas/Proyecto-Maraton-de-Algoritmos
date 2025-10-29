// Proyecto de Informatica
// Ejercicio 479
Título del Ejercicio: Verificar Palíndromo
Análisis del Problema
? Descripción del Problema: Verificar si una cadena es palíndromo.

? Entradas y Salidas:

? Entrada: Cadena de caracteres.

? Salida: true si es palíndromo, false si no.

Diseño de la Solución
? Algoritmo Propuesto:

1. Comparar primer y último carácter.

2. Llamar recursivamente al sub-string interno.

? Estructuras de Datos: Cadena de caracteres.

? Funciones Principales: main() y esPalindromo().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

bool esPalindromo(string s, int start, int end){
    if(start>=end) return true;
    if(s[start]!=s[end]) return false;
    return esPalindromo(s,start+1,end-1);
}

int main() {
    string texto="radar";
    if(esPalindromo(texto,0,texto.length()-1))
        cout << texto << " es palindromo" << endl;
    else
        cout << texto << " no es palindromo" << endl;
    return 0;
}

Pruebas
? Caso 1: "radar" ? palíndromo

? Caso 2: "hola" ? no palíndromo

? Caso 3: "a" ? palíndromo