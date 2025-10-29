// Proyecto de Informatica
// Ejercicio 443
Título del Ejercicio: Contar Vocales Recursivamente
Análisis del Problema
? Descripción del Problema: Contar la cantidad de vocales en una cadena usando recursión.

? Entradas y Salidas:

? Entrada: Cadena de caracteres.

? Salida: Número de vocales.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si la cadena está vacía ? retornar 0.

2. Si el primer carácter es vocal ? sumar 1 y llamar recursivamente al resto de la cadena.

3. Si no es vocal ? llamar recursivamente al resto de la cadena.

? Estructuras de Datos: Cadena y contador.

? Funciones Principales: main() y contarVocalesRecursivo().

Código Fuente (C++)
#include <iostream>
#include <string>
using namespace std;

bool esVocal(char c){
    c = tolower(c);
    return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
}

int contarVocalesRecursivo(string s){
    if(s.empty()) return 0;
    return esVocal(s[0]) + contarVocalesRecursivo(s.substr(1));
}

int main() {
    string texto="Hola Mundo";
    cout << "Cantidad de vocales: " << contarVocalesRecursivo(texto) << endl; // 4
    return 0;
}

Pruebas
? Caso 1: "Hola Mundo" ? 4

? Caso 2: "ABCDE" ? 2

? Caso 3: "xyz" ? 0