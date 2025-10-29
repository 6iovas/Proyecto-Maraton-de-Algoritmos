// Proyecto de Informatica
// Ejercicio 110
Ejercicio 108: Contar frecuencias con std::map
Análisis del Problema
 Contar cuántas veces aparece cada palabra en un texto.
Diseño de la Solución
? Leer texto palabra por palabra.

? Incrementar el contador en std::map<string, int>.

Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    map<string, int> freq;
    string word;
    while (cin >> word) freq[word]++;
    for (auto& [w, c] : freq)
        cout << w << ": " << c << '\n';
}

Pruebas
? Entrada: "hola mundo hola"

Salida:

 hola: 2
mundo: 1
?